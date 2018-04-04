#include <iostream>
#include <cstdlib>
#include <ctime>

using std::cout;
using std::endl;

int fibonacci(int N);
float get_time(int N);

int main(){
  int i, N;
  float tiempoN;
  N = 35;
  
  for(i=0; i<=N; i++){
    fibonacci(i);
    tiempoN =  get_time(i);
    cout << i << ", " << tiempoN << endl;
  }
  return 0;
}

int fibonacci(int N){
  if(N== 0 || N==1){
    return N;
  }
  else{
    return fibonacci(N-1) + fibonacci(N-2);
  }
}

float get_time(int N){
  clock_t t;
  t = clock();
  fibonacci(N);
  t = clock() - t;
  float time = ((float)t)/CLOCKS_PER_SEC;
  return time;

}
 
  
  
