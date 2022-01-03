#include <stack>
#include <string>
#include <sstream>
#include "test_framework/generic_test.h"
#include "test_framework/timed_executor.h"
using std::string;

void ReverseWords(string *s)
{
  std::reverse(std::begin(*s), std::end(*s));

  size_t start = 0, finish;

  while ((finish = s->find(" ", start)) != std::string::npos)
  {
    std::reverse(std::begin(*s) + start, std::begin(*s) + finish);

    start = finish + 1;
  }
  std::reverse(std::begin(*s) + start, std::end(*s));
}
string ReverseWordsWrapper(TimedExecutor &executor, string s)
{
  string s_copy = s;

  executor.Run([&]
               { ReverseWords(&s_copy); });

  return s_copy;
}

int main(int argc, char *argv[])
{
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "s"};
  return GenericTestMain(args, "reverse_words.cc", "reverse_words.tsv",
                         &ReverseWordsWrapper, DefaultComparator{},
                         param_names);
}
