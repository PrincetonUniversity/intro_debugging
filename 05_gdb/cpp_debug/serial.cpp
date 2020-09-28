#include <iostream>

int doubler(int num) {
  return 2 * num;
}

void myfunc(double* x, int N) {
  double y = x[0] * x[1];
  x[2] = y;
}

int main(int argc, char* argv[]) {

  int mynum = 42;
  std::cout << mynum << " doubled is " << doubler(mynum) << std::endl;

  size_t N = 5;
  double x[5] = {10, 20, 30, 40, 50};
  myfunc(x, N);
  std::cout << "myfunc produced: " << x[2] << std::endl;

  int A[N][N];
  for (int i=0; i < N; i++)
    for (int j=0; j < N; j++) {
      A[i][j] = i * j + i + j;
      if (i == j) std::cout << "diagonal element of A[i][j]: " << A[i][j] << std::endl;
  }

  int mysum = 0;
  for (int i=0; i < 10; i++)
    mysum = mysum + i;
  std::cout << "mysum = " << mysum << std::endl;

  return 0;
}
