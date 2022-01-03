#include <string>
//#include <strstream>
#include <unordered_map>
//#include <algorithm>
#include "test_framework/generic_test.h"
using std::string;
int Evaluate(const string &expression)
{
  std::unordered_map<std::string, std::function<int(int, int)>> operations{
      {"+", [](int a, int b)
       { return a + b; }},
      {"-", [](int a, int b)
       { return a - b; }},
      {"/", [](int a, int b)
       { return a / b; }},
      {"*", [](int a, int b)
       { return a * b; }}};

  std::stack<int> values;
  const char delim = ',';
  std::stringstream ss(expression);
  std::string token;
  while (std::getline(ss, token, delim))
  {
    if (operations.count(token))
    {
      int v2 = values.top();
      values.pop();
      int v1 = values.top();
      values.pop();
      values.emplace(operations[token](v1,v2));
    }else{
      values.emplace(std::stoi(token));
    }
  }

  return values.top();
}

int main(int argc, char *argv[])
{
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"expression"};
  return GenericTestMain(args, "evaluate_rpn.cc", "evaluate_rpn.tsv", &Evaluate,
                         DefaultComparator{}, param_names);
}
