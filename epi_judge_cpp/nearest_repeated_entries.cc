#include <unordered_map>
#include <string>
#include <vector>
#include "test_framework/generic_test.h"
using std::string;
using std::vector;

int FindNearestRepetition(const vector<string> &paragraph)
{

  std::unordered_map<std::string, size_t> map;
  size_t min_diff = std::numeric_limits<size_t>::max();
  //std::string word;
  for (size_t i = 0; i < paragraph.size(); ++i)
  {
    if (map.find(paragraph[i]) != map.end())
    {
      if ((i - map[paragraph[i]]) < min_diff)
      {
        min_diff = i - map[paragraph[i]];
        //word = paragraph[i];
      }
    }
    map[paragraph[i]] = i;
  }

  return min_diff == std::numeric_limits<size_t>::max() ? -1 : min_diff;
}

int main(int argc, char *argv[])
{
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"paragraph"};
  return GenericTestMain(args, "nearest_repeated_entries.cc",
                         "nearest_repeated_entries.tsv", &FindNearestRepetition,
                         DefaultComparator{}, param_names);
}
