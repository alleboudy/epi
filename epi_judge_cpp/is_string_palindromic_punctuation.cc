#include <string>
#include "test_framework/generic_test.h"
using std::string;

bool IsPalindrome(const string &s)
{
  int start = 0, end = s.size() - 1;

  while (start < end)
  {
    while (!isalnum(s[end]) && start < end)
      end--;
    while (!isalnum(s[start]) && start < end)
      start++;

    if (tolower(s[start++]) != tolower(s[end--]))
    {
      return false;
    }
  }

  return true;
}

int main(int argc, char *argv[])
{
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"s"};
  return GenericTestMain(args, "is_string_palindromic_punctuation.cc",
                         "is_string_palindromic_punctuation.tsv", &IsPalindrome,
                         DefaultComparator{}, param_names);
}
