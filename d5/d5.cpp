#include <algorithm>
#include <climits>
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

#define ll long long

int solve(std::string filename) {
    std::ifstream in(filename);
    std::string line;
    
    std::vector<std::pair<ll, ll>> pairs;
    while (std::getline(in, line)) {
        if (line == "") break;
        ll l, r;
        sscanf(line.c_str(), "%lld-%lld", &l, &r);
        pairs.emplace_back(l, r);
    }

    sort(pairs.begin(), pairs.end());
    std::vector<std::pair<ll, ll>> ranges;
    for (auto &[l, r] : pairs) {
        if (ranges.empty() || ranges.back().second < l) {
            ranges.emplace_back(l, r);
        } else {
            ranges.back().second = std::max(ranges.back().second, r);
        }
    }

    int res = 0;
    while (std::getline(in, line)) {
        ll x;
        std::sscanf(line.c_str(), "%lld", &x);

        auto it = std::lower_bound(
            ranges.begin(), 
            ranges.end(), 
            std::make_pair(x + 1, LLONG_MAX), 
            [](const auto& val, const auto& elem) {
                return val.first < elem.first;
            }
        );

        if (it != ranges.begin()) {
            --it;
            if (it->first <= x && x <= it->second) ++res;
        }
    }

    return res;
}

ll solve2(std::string filename) {
    std::ifstream in(filename);
    std::string line;
    
    std::vector<std::pair<ll, ll>> pairs;
    while (std::getline(in, line)) {
        if (line == "") break;
        ll l, r;
        sscanf(line.c_str(), "%lld-%lld", &l, &r);
        pairs.emplace_back(l, r);
    }

    sort(pairs.begin(), pairs.end());
    std::vector<std::pair<ll, ll>> ranges;
    for (auto &[l, r] : pairs) {
        if (ranges.empty() || ranges.back().second < l) {
            ranges.emplace_back(l, r);
        } else {
            ranges.back().second = std::max(ranges.back().second, r);
        }
    }

    ll res = 0;
    for (auto &[l, r] : ranges) {
        res += r - l + 1;
    }
    return res;
}

int main() {
    assert(solve("d5_test.in") == 3);
    assert(solve("d5.in") == 617);

    assert(solve2("d5_test.in") == 14);
    assert(solve2("d5.in") == 338258295736104);
}
