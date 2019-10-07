#include <string>
#include <memory>
#include <vector>
#include <variant>
#include <iostream>
#include <sstream>
#include <map>
#include <unordered_map>

namespace regex {

enum class ExprType {
    Literal = 0,
    Repeat,
    Plus,
    Or,
    Concat,
};

struct RegexExpr {
    virtual ExprType GetType() const = 0;

    virtual std::string ToStr(size_t indent_lvl) const = 0;
};

struct Literal : RegexExpr {
    Literal(char v) : value(v) {
    }
    char value;

    ExprType GetType() const override {
        return ExprType::Literal;
    }
    std::string ToStr(size_t indent_lvl) const override {
        return std::string{value};
    }
};

struct Repeat : RegexExpr {
    Repeat(std::unique_ptr<RegexExpr> e) : expr{std::move(e)} {
    }
    std::unique_ptr<RegexExpr> expr;

    ExprType GetType() const override {
        return ExprType::Repeat;
    }
    std::string ToStr(size_t indent_lvl) const override {
        return "repeat-> " + expr->ToStr(indent_lvl + 10) + " ";
    }
};

struct Plus : RegexExpr {
    Plus(std::unique_ptr<RegexExpr> e) : expr{std::move(e)} {
    }
    std::unique_ptr<RegexExpr> expr;

    ExprType GetType() const override {
        return ExprType::Plus;
    }
    std::string ToStr(size_t indent_lvl) const override {
        return "plus-> " + expr->ToStr(indent_lvl + 7) + " ";
    }
};

struct Or : RegexExpr {
    Or(std::unique_ptr<RegexExpr> left, std::unique_ptr<RegexExpr> right) : left_expr{std::move(left)},
                                                                            right_expr{std::move(right)} {
    }
    std::unique_ptr<RegexExpr> left_expr;
    std::unique_ptr<RegexExpr> right_expr;

    ExprType GetType() const override {
        return ExprType::Or;
    }
    std::string ToStr(size_t indent_lvl) const override {
        std::string indent(indent_lvl, ' ');
        indent_lvl += 5;
        return "or-> " + left_expr->ToStr(indent_lvl) + "\n" + indent + " \\-> " + right_expr->ToStr(indent_lvl);
    }

};

struct Concat : RegexExpr {
    Concat(std::unique_ptr<RegexExpr> left, std::unique_ptr<RegexExpr> right) : left_expr{std::move(left)},
                                                                                right_expr{std::move(right)} {
    }
    std::unique_ptr<RegexExpr> left_expr;
    std::unique_ptr<RegexExpr> right_expr;

    ExprType GetType() const override {
        return ExprType::Concat;
    }
    std::string ToStr(size_t indent_lvl) const override {
        std::string indent(indent_lvl, ' ');
        indent_lvl += 7;
        return "and-> " + left_expr->ToStr(indent_lvl) + "\n" + indent + "   \\-> " + right_expr->ToStr(indent_lvl);
    }
};

class AST {
 public:
    AST(std::string_view pattern) : pattern_{pattern} {
        root_ = AstBuilder(nullptr);
    }
    const RegexExpr *GetRoot() const {
        return root_.get();
    }

    std::string AstToStr() {
        return root_->ToStr(0);
    }
 private:
    std::unique_ptr<RegexExpr> AstBuilder(std::unique_ptr<RegexExpr> left_expr) {
        if (pattern_.empty()) {
            return left_expr;
        }
        char now_symbol = pattern_.front();
        pattern_ = pattern_.substr(1);
        switch (now_symbol) {
        case '(': {
            size_t this_level = current_level;
            ++current_level;
            std::unique_ptr<RegexExpr> right_expr;
            do {
                right_expr = AstBuilder(std::move(right_expr));
            } while (current_level >= this_level && !pattern_.empty());
            if (left_expr) {
                return std::make_unique<Concat>(std::move(left_expr), std::move(right_expr));
            } else {
                return right_expr;
            }
        }
        case ')': {
            --current_level;
            return left_expr;
        }
        case '+': {
            return AstBuilder(std::make_unique<Plus>(std::move(left_expr)));
        }
        case '*': {
            return AstBuilder(std::make_unique<Repeat>(std::move(left_expr)));
        }
        case '|': {
            return std::make_unique<Or>(std::move(left_expr), AstBuilder(nullptr));
        }
        default: {
            if (now_symbol == '\\') {
                now_symbol = pattern_.front();
                pattern_ = pattern_.substr(1);
            }
            if (left_expr) {
                return std::make_unique<Concat>(std::move(left_expr),
                                                AstBuilder(std::make_unique<Literal>(now_symbol)));
            } else {
                return AstBuilder(std::make_unique<Literal>(now_symbol));
            }
        }
        }
    }
    std::string_view pattern_;
    size_t current_level = 0;
    std::unique_ptr<RegexExpr> root_;
};

class NFA {
    using Node = std::size_t;
    using Edge = char;
 public:
    NFA(const AST &regex_parser) {
        auto temp = BuildGraph(regex_parser.GetRoot());
        start_ = temp.first;
        end_ = temp.second;
    }
    std::string NfaToStr() const {
        std::ostringstream out;
        out << "START: " << start_ << " END: " << end_ << "\n\n";
        for (auto&[s_node, edges]: graph) {
            for (auto&[value, e_node]:edges) {
                out << s_node << " " << value << " " << e_node << "\n";
            }
        }
        return out.str();
    }
    bool Match(std::string_view str) const {
        return Search(str, start_, str.size() * 10);

    }

 private:
    Node start_ = 0, end_ = 0;
    Node counter_ = 0;

    bool Search(std::string_view str, Node curr, std::size_t max_depth) const {
        if (max_depth == 0 || graph.count(curr) == 0) {
            return str.empty() && curr == end_;
        }
        bool ans = false;
        for (auto &neibor: graph.at(curr)) {
            if (!str.empty() && (neibor.first == '.' || neibor.first == str.front())) {
                ans = ans || Search(str.substr(1), neibor.second, max_depth - 1);
            } else if (neibor.first == '\0') {
                ans = ans || Search(str, neibor.second, max_depth - 1);
            }
            if (ans) {
                break;
            }
        }
        return ans;
    }

    Node CreateNode() {
        return counter_++;
    }

    std::pair<Node, Node> BuildGraph(const RegexExpr *expr) {
        if (!expr) {
            return {CreateNode(), CreateNode()};
        }
        switch (expr->GetType()) {
        case ExprType::Literal: {
            auto input = CreateNode();
            auto output = CreateNode();
            graph[input].emplace_back(dynamic_cast<const Literal *>(expr)->value, output);
            return {input, output};
        }
        case ExprType::Repeat: {
            expr = dynamic_cast<const Repeat *>(expr)->expr.get();
            auto input = CreateNode();
            auto[son_input, son_output] = BuildGraph(expr);
            auto output = CreateNode();
            graph[input].emplace_back('\0', son_input);
            graph[son_output].emplace_back('\0', input);
            graph[input].emplace_back('\0', output);
            return {input, output};
        }
        case ExprType::Plus: {
            expr = dynamic_cast<const Plus *>(expr)->expr.get();
            auto[son_input, son_output] = BuildGraph(expr);
            auto input = CreateNode();
            auto output = CreateNode();
            graph[son_output].emplace_back('\0', input);
            graph[input].emplace_back('\0', son_input);
            graph[input].emplace_back('\0', output);
            return {son_input, output};
        }
        case ExprType::Concat: {
            auto expr_temp = dynamic_cast<const Concat *>(expr);
            auto[left_input, left_output] = BuildGraph(expr_temp->left_expr.get());
            auto[right_input, right_output] = BuildGraph(expr_temp->right_expr.get());
            graph[left_output].emplace_back('\0', right_input);
            return {left_input, right_output};
        }
        case ExprType::Or: {
            auto expr_temp = dynamic_cast<const Or *>(expr);
            auto input = CreateNode();
            auto[left_input, left_output] = BuildGraph(expr_temp->left_expr.get());
            auto[right_input, right_output] = BuildGraph(expr_temp->right_expr.get());
            auto output = CreateNode();
            graph[input].emplace_back('\0', left_input);
            graph[input].emplace_back('\0', right_input);
            graph[left_output].emplace_back('\0', output);
            graph[right_output].emplace_back('\0', output);
            return {input, output};
        }
        }
    }

    std::unordered_map<Node, std::vector<std::pair<Edge, Node>>> graph;
};

}
int main() {
    std::string regex_expr = R"((sada)|(adasd)|((sdsd)*aa))";
    regex::AST parser{regex_expr};
    // std::cout << parser.AstToStr() << std::endl;
    regex::NFA nfa{parser};
    // std::cout << nfa.NfaToStr() << std::endl;
    std::string main_str = R"(sdsdsdsdaa)";
    std::cout << std::boolalpha << nfa.Match(main_str) << std::endl;

    return 0;
}