#include <algorithm>
#include <unordered_set>
#include <string>
#include "test_framework/generic_test.h"
using std::string;

bool CanFormPalindrome(const string &s)
{

  std::unordered_set<char> set;

  for (char c : s)
  {
    if (set.find(c) == set.end())
    {
      set.insert(c);
    }
    else{
      set.erase(c);
    }
  }
  
  return set.size()<=1;
}

int main(int argc, char *argv[])
{
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"s"};
  return GenericTestMain(args, "is_string_permutable_to_palindrome.cc",
                         "is_string_permutable_to_palindrome.tsv",
                         &CanFormPalindrome, DefaultComparator{}, param_names);
}
