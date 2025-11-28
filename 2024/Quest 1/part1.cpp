#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;



int main() {

    map<char, int> insect_values;
    insect_values['A'] = 0;
    insect_values['B'] = 1;
    insect_values['C'] = 3;
    string toParse;
    ifstream a("input1.txt");
    a >> toParse;
    a.close();
    int pots_needed = 0;
    for (const char insect: toParse){
        pots_needed = pots_needed + insect_values[insect];
    }
    cout << pots_needed;
} 