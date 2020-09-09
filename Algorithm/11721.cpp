#include <iostream>
#include <string>
using namespace std;

int main() {
	int tmp = 0;
	string str = "";
	cin >> str;
	while (tmp < str.size()) {
		cout << str[tmp];
		tmp++;
		if (tmp % 10 == 0) {
			cout << endl;
		}
	}
	
	return 0;
}