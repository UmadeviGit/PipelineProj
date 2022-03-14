#include <iostream>

#include <fstream>
using namespace std;
int main(){
	cout << "Hello, world!" << endl;
	cout << "Hello, world 2!" << endl;
	cout << "Hello, world 3!" << endl;
	cout << "Hello, world !4" << endl;
	cout << "Hello, world !5" << endl;

	ofstream file;
	file.open("readme.txt", ios::out);
	file << "Writing to a file in C++....";
	file.close();
	system("explorer.exe readme.txt");
	return 0;

return 1;
}
