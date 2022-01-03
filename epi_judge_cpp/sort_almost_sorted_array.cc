#include <functional>
#include <queue>
#include <vector>
#include "test_framework/generic_test.h"
using std::vector;
vector<int> SortApproximatelySortedData(
    vector<int>::const_iterator sequence_begin,
    const vector<int>::const_iterator& sequence_end, int k) {
  std::vector<int> result;
  std::priority_queue<int, std::vector<int>, std::function<bool(int,int)>> heap([](const int&a, const int&b){return a>=b;});
  
  for(sequence_begin; sequence_begin<sequence_end;sequence_begin=sequence_begin+k){

    for(size_t i = 0; i<k;++i){
      if(sequence_begin+i < sequence_end)
      heap.emplace(*(sequence_begin+i));
    }

    while (heap.size()>0)
    {
      result.emplace_back(heap.top());
      heap.pop();
    }
  

  }
  
  return result;
}
vector<int> SortApproximatelySortedDataWrapper(const vector<int>& sequence,
                                               int k) {
  return SortApproximatelySortedData(cbegin(sequence), cend(sequence), k);
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"sequence", "k"};
  return GenericTestMain(
      args, "sort_almost_sorted_array.cc", "sort_almost_sorted_array.tsv",
      &SortApproximatelySortedDataWrapper, DefaultComparator{}, param_names);
}
