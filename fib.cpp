#include <iostream>
#include <unordered_map>
#include <chrono>

int maxfib = 10000;
int repeats = 10000;
auto fibrange(){
	for (int i=0;i<=maxfib;i++) {
		int fib(i);
	}
}
auto mapfibrange(){
	for (int i=0;i<=maxfib;i++) {
		int mapfib(i);
	}
}

int fib(int n) {
	if (n<=1){
		return n;
	}
	return fib(n-1) + fib(n-2);
}

std::unordered_map<int,int> fibs= {{0,1},{1,1}};
int mapfib(int n) {
	if ( fibs.find(n)!=fibs.end() ) { return fibs[n]; }
	fibs[n] = fibs[n-1]+fibs[n-2];
	return fibs[n];
}

int main() {
    auto start = std::chrono::high_resolution_clock::now();
		for (int i; i <= repeats; i++)
		{fibrange();}
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);
		std::cout << "Fibrange: " << duration.count() << "\n";

    auto mstart = std::chrono::high_resolution_clock::now();
		for (int i; i <= repeats; i++)
		{ mapfibrange(); }
    auto mend = std::chrono::high_resolution_clock::now();

    auto mduration = std::chrono::duration_cast<std::chrono::nanoseconds>(mend - mstart);
		std::cout <<"MapFibrange: " << mduration.count() << "\n";

		std::cout << "Difference (+ means map was faster): " << duration.count()-mduration.count() << std::endl;
		return 0;
}
