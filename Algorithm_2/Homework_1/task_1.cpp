#include <algorithm>
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

size_t find_new_substr(const std::string_view s, size_t pos) {
    size_t max = 0;
    std::vector<size_t> z(pos, 0);
    auto it = s.rbegin();
    for (size_t i = 1, l = 0, r = 0; i < pos; ++i) {
        if (i <= r) {
            z[i] = std::min(r - i + 1, z[i - l]);
        }
        while (i + z[i] < pos && *(it + z[i]) == *(it + i + z[i])) {
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
    std::cout << ans << std::endl;
    return 0;
}
