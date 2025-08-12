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
    insect_values['D'] = 5;
    insect_values['x'] = 0;
    string toParse;
    ifstream a("input2.txt");
    a >> toParse;
    a.close();
    int pots_needed = 0;
    for (int i = 0; i < toParse.length(); i = i + 2){
        char insect1 = toParse[i];
        char insect2 = toParse[i+1];
        pots_needed = pots_needed + insect_values[insect1] + insect_values[insect2];
        if (insect1 != 'x' && insect2 != 'x'){
            pots_needed = pots_needed + 2;
        }
    }
    cout << pots_needed;
} 