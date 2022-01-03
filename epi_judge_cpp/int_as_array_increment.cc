#include <vector>
#include "test_framework/generic_test.h"
using std::vector;
vector<int> PlusOne(vector<int> A)
{
  
  
  A.back()++;
  for (std::vector<int>::reverse_iterator it = std::rbegin(A); it !=std::rend(A)-1 &&  (*it)==10; it++)
  {
    (*it) =0 ;    
    (*(it+1))++;
  }

  if(A[0]==10){
    A[0] = 1;
    A.emplace_back(0);
  }


  

  return A;
}

int main(int argc, char *argv[])
{
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"A"};
  return GenericTestMain(args, "int_as_array_increment.cc",
                         "int_as_array_increment.tsv", &PlusOne,
                         DefaultComparator{}, param_names);
}
