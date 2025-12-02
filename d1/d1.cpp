#include <cassert>
#include <fstream>
#include <iostream>
#include <string>

int solve(std::string filename) {
    std::ifstream in(filename);
    std::string rot;
    
    int curr = 50, res = 0;
    while (std::getline(in, rot)) {
        int num = std::stoi(rot.substr(1));

        if (rot[0] == 'L') {
            curr = (curr - num) % 100; 
            if (curr < 0) curr += 100;
        } else {
            curr = (curr + num) % 100;
        }

        res += curr == 0;
    }

    return res;
}

int solve2(std::string filename) {
    std::ifstream in(filename);
    std::string rot;
    
    int curr = 50, res = 0;
    while (std::getline(in, rot)) {
        int num = std::stoi(rot.substr(1));
        res += num / 100;

        if (rot[0] == 'L') {
            if (num % 100 >= curr && curr != 0) {
                res += 1;
            }
            curr = (curr - num) % 100; 
            if (curr < 0) curr += 100;
        } else {
            if (num % 100 >= 100 - curr && curr != 0) {
                res += 1;
            }
            curr = (curr + num) % 100;
        }
    }

    return res;
}

int main() {
    assert(solve("d1_test.in") == 3);
    assert(solve("d1.in") == 1040);

    assert(solve2("d1_test.in") == 6);
    assert(solve2("d1.in") == 6027);
}
