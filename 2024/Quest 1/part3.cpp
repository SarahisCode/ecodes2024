#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <array>
using namespace std;


int main() {

    map<char, int> insect_values;
    insect_values['A'] = 0;
    insect_values['B'] = 1;
    insect_values['C'] = 3;
    insect_values['D'] = 5;
    insect_values['x'] = 0;
    string toParse;
    ifstream a("input3.txt");
    a >> toParse;
    a.close();
    int pots_needed = 0;
    for (int i = 0; i < toParse.length(); i = i + 3){
        char insect1 = toParse[i];
        char insect2 = toParse[i+1];
        char insect3 = toParse[i+2];
        const int num_insects = 3;
        int blanks = 0;
        array<char, num_insects> insects = {insect1, insect2, insect3};
        for (char insect: insects) {
            pots_needed += insect_values[insect];
            if (insect == 'x') {
                blanks++;
            }
        }
        cout << pots_needed << "\n";
        switch (blanks) {
            case 1:
                pots_needed += 2;
                break;
            case 0:
                pots_needed += 6;
                break;
        }
    }
    cout << pots_needed;
} 