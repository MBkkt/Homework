#include <algorithm>
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

std::vector<size_t> z_function(const std::string_view s) {
    size_t n = s.length();
    std::vector<size_t> z(n, 0);
    for (size_t i = 1, l = 0, r = 0; i < n; ++i) {
        if (i <= r) {
            z[i] = std::min(r - i + 1, z[i - l]);
        }
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
            ++z[i];
        }
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    return z;
}

size_t find_max_z_func(std::string s) {
    std::reverse(s.begin(), s.end());
    auto temp = z_function(s);
    return *std::max_element(temp.begin(), temp.end());
}

int main() {
    size_t ans = 0;
    std::string s;
    std::cin >> s;
    for (size_t i = 0; i != s.size(); ++i) {
        ans += (i + 1 - find_max_z_func(s.substr(0, i + 1)));
    }
    std::cout << ans;
    return 0;
}