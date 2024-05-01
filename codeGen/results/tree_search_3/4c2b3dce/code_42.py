// BEGIN PLAN
// Use a sliding window approach to check if the string contains both 'AB' and 'BA' without any overlap.
bool found_ab = false, found_ba = false;
for (int i = 0; i < len(s); i++) {
    // Check for 'AB'
    if (i + 1 < len(s) && s.substr(i, 2) == "AB" && !found_ab) {
        found_ab = true;
        i++; // Skip the 'B' in 'AB' to avoid overlap
    }
    // Check for 'BA'
    if (i < len(s) - 1 && s.substr(i, 2) == "BA" && !found_ba) {
        found_ba = true;
        i++; // Skip the 'A' in 'BA' to avoid overlap
    }
}
// If both 'AB' and 'BA' are found, return 'YES'; otherwise, return 'NO'.
cout << (found_ab && found_ba ? "YES" : "NO") << endl;
