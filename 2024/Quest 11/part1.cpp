#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <map>
#include <vector>
using namespace std;

int main() {
    ifstream a("input.txt");
    string line = "";
    map<string, vector<string>> conversions;
    vector<string> beetleTypes;
    while (getline(a,line,'\n')) {
        string x = "";
        stringstream ss(line);
        string from;
        getline(ss, from, ':');
        beetleTypes.push_back(from);
        vector<string> to;
        while (getline(ss, x, ',')) {
            to.push_back(x);
        }
        conversions[from] = to;
    }
    int generations = 4;
    map<string, long int> beetles;
    beetles["A"] = 1;
    for (int i=0; i<generations; i++) {
        map<string, long int> newBeetles;
        for (string type: beetleTypes) {
            if (beetles[type] > 0) {
                int number = beetles[type];
                for (string newType: conversions[type]) {
                    newBeetles[type] += number;
                }
            }
        }
        beetles = newBeetles;
    }
    
}