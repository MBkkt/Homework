#include <algorithm>
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

size_t find_new_substr(std::string s, size_t pos) {
    std::reverse(s.begin(), s.end());
    size_t n = pos, max = 0;
    std::vector<size_t> z(n, 0);
    for (size_t i = 1, l = 0, r = 0; i < pos; ++i) {
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
        if (z[i] > max) {
            max = z[i];
        }
    }
    return pos - max;
}

int main() {
    size_t ans = 0;
    std::string s;
    std::cin >> s;
    for (size_t i = 0; i < s.size(); ++i) {
        ans += find_new_substr(s, i + 1);
    }
    std::cout << ans;
    return 0;
}