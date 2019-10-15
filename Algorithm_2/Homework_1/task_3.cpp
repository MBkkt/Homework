#include <iostream>
#include <string>
#include <string_view>
#include <cassert>
#include <vector>

template<typename BidirectionalIterator>
std::size_t compute_prefix(BidirectionalIterator begin, BidirectionalIterator end) {
    std::size_t size = end - begin;
    std::vector<std::size_t> prefix(size, 0);
    for (std::size_t i = 1; i < size; ++i) {
        auto j = prefix[i - 1];
        while (j != 0 && *(begin + j) != *(begin + i)) {
            j = prefix[j - 1];
        }
        if (*(begin + j) == *(begin + i)) {
            prefix[i] = j + 1;
        }
    }
    return prefix.back();
}

std::size_t period(const std::string_view str) {
    auto possible_period = str.size() - compute_prefix(str.begin(), str.end());
    if (str.size() % possible_period == 0) {
        return possible_period;
    }
    return str.size();
}

void TestAll() {
    assert(period("valera") == 6);
    assert(period("samesamesamesame") == 4);
    assert(period("aaaaaaaaaa") == 1);
    assert(period("lalal") == 5);
    assert(period("keke") == 2);
    assert(period("fuufuufuufuufuu") == 3);
    assert(period("abacaba") == 7);
}

int main() {
    TestAll();
    std::string input;
    std::cin >> input;
    std::cout << "Period size: " << period(input) << std::endl;
    return 0;
}
