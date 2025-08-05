#include <iostream>
#include <fstream>
#include <random>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    // Initializing random number generator
    random_device rd;
    mt19937 rng(rd());

    // Taking user input
    int trials, ring_size;
    string filename;
    cout << "trials: "; cin >> trials;
    cout << "ring size: "; cin >> ring_size;
    cout << "file name: "; cin >> filename;

    // Opening output file
    ofstream outfile(filename);
    if (! outfile) {
        cerr << "Failed to open file: " << filename << endl;
        return 1;
    }

    outfile << "count\n";

    // Repeat simulation 'trials' times
    for (int trial = 1; trial <= trials; trial++) {
        // Setting initial position and move count to 0
        int pos = 0, count=0;

        // Keep taking steps until it hits n or -n
        while (pos < ring_size && pos > -ring_size) {
            unsigned int step = rng() % 2; // step is a random integer modulo 2
            if (step % 2 == 0) pos++; // Add 1 if step is even
            else pos--; // Subtract 1 if step is odd
            count++; // Increment move count
        }

        // Print data to the output file
        outfile << count << "\n"; 
    }

    outfile.close();
    cout << "completed\n";

    return 0;
}