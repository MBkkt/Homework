#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cassert>

template<typename BidirectionalIterator>
std::size_t max_prefix(BidirectionalIterator begin, BidirectionalIterator end) {
    std::size_t size = end - begin;
    std::vector<std::size_t> prefix(size, 0);
    auto result = prefix[0];
    for (std::size_t i = 1; i < size; ++i) {
        auto j = prefix[i - 1];
        while (j != 0 && *(begin + j) != *(begin + i)) {
            j = prefix[j - 1];
        }
        if (*(begin + j) == *(begin + i)) {
            prefix[i] = j + 1;
            result = std::max(result, prefix[i]);
        }
    }
    return result;
}

std::size_t count_different_substr(const std::string_view str) {
    std::size_t count = 0;
    for (std::size_t i = 1; i <= str.size(); ++i) {
        count += i - max_prefix(str.rbegin() + (str.size() - i), str.rend());
    }
    return count;
}

void TestAll() {
    assert(count_different_substr("") == 0);
    assert(count_different_substr("abacaba") == 21);
    assert(count_different_substr("aaaaaaa") == 7);
    assert(count_different_substr("cd") == 3);
    assert(count_different_substr("c") == 1);
    assert(count_different_substr("ccdc") == 8);
}

int main() {
    TestAll();
    std::string str;
    std::cin >> str;
    std::cout << count_different_substr(str);
    return 0;
}
