#include <algorithm>
#include <climits>
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

#define ll long long

ll solve(std::string filename) {
    std::ifstream in(filename);
    std::string line;
    
    std::vector<std::pair<ll, ll>> tiles;
    while (std::getline(in, line)) {
        if (line == "") break;
        ll l, r;
        sscanf(line.c_str(), "%lld,%lld", &l, &r);
        tiles.emplace_back(l, r);
    }

    ll res = 0;
    for (int i = 0; i < tiles.size(); ++i) {
        for (int j = i + 1; j < tiles.size(); ++j) {
            ll dr = abs(tiles[i].first - tiles[j].first) + 1;
            ll dc = abs(tiles[i].second - tiles[j].second) + 1;
            res = std::max(res, dr * dc);
        }
    }

    return res;
}

// Ray casting function to check if point is inside polygon
bool point_in_polygon(ll x, ll y, const std::vector<std::pair<ll, ll>>& polygon) {
    int crossings = 0;
    int n = polygon.size();
    
    for (int i = 0; i < n; ++i) {
        ll x1 = polygon[i].first;
        ll y1 = polygon[i].second;
        ll x2 = polygon[(i + 1) % n].first;
        ll y2 = polygon[(i + 1) % n].second;
        
        // Check if ray from (x,y) going right crosses edge (x1,y1)-(x2,y2)
        if (y1 == y2) continue;  // Horizontal edge, skip
        
        if (y < std::min(y1, y2) || y >= std::max(y1, y2)) continue;
        
        // Calculate x-coordinate where edge crosses horizontal line at y
        double x_intersect = x1 + (double)(y - y1) * (x2 - x1) / (y2 - y1);
        
        if (x < x_intersect) {
            crossings++;
        }
    }
    
    return crossings % 2 == 1;
}

ll solve2(std::string filename) {
    // some polygon thing im too lazy to do
    return 67;
}

int main() {
    assert(solve("d9_test.in") == 50);
    assert(solve("d9.in") == 4733727792);
}
