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
    cout << "ring size: "; cin >> ring_size;
    cout << "trials per starting position: "; cin >> trials;
    cout << "file name: "; cin >> filename;

    // Opening output file
    ofstream outfile(filename);
    if (! outfile) {
        cerr << "Failed to open file: " << filename << endl;
        return 1;
    }

    /* Setting the interval variable so it
    only runs simulations where it's possible for the
    frogs to meet given their starting positions */
    int interval;
    if (ring_size % 2 == 0) interval = 2;
    else interval = 1;

    outfile << "start,final,count\n";

    for (int startpos = interval; startpos < ring_size; startpos += interval) {
        for (int trial = 0; trial < trials; trial++) {
            // Initial movecount and positions of the two frogs, assuming frog A starts at 0
            int count = 0, f1 = 0, f2 = startpos;

            // Continue making moves until their positions are the same at the end of a turn
            while (f1 != f2) {
                // step1 and step2 are random integers modulo 2
                unsigned int step1 = rng() % 2;
                unsigned int step2 = rng() % 2;

                if (step1 == 0) f1++; // If even, add one to f1 position
                else f1--; // If odd, subtract one from f1 position

                if (step2 == 0) f2++; // If even, add one to f2 position
                else f2--; // If odd, subtract one from f2 position

                // Making sure that 0 <= position < n
                f1 = (f1+ring_size) % ring_size;
                f2 = (f2+ring_size) % ring_size;

                count++; // Increment move count
            }

            // Print data to the output file
            outfile << startpos << "," << f1 << "," << count << "\n";
        }
    }

    fclose(stdout);

    cout << "completed\n";

    return 0;
}