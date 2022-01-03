#include <memory>
#include "list_node.h"
#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/timed_executor.h"
using std::shared_ptr;

int getListLength(std::shared_ptr<ListNode<int>> l)
{

  int result = 0;

  while (l)
  {
    result += 1;
    l = l->next;
  }
  return result;
}

shared_ptr<ListNode<int>> OverlappingNoCycleLists(
    shared_ptr<ListNode<int>> l0, shared_ptr<ListNode<int>> l1)
{
  int len0 = getListLength(l0);
  int len1 = getListLength(l1);
  std::shared_ptr<ListNode<int>> matchStart;
  
  if(len0>len1){
    int diff = len0 - len1;
    while (diff>0)
    {
      l0=l0->next;
      diff--;
    }
    
  }else if(len1>len0){
    int diff = len1 - len0;
    while (diff>0)
    {
      l1=l1->next;
      diff--;
    }
  }

  bool areMatching = false;
    
    for (auto curL0 = l0, curL1 = l1; curL0 && curL1; curL0 = curL0->next, curL1 = curL1->next)
    {
      if (curL0.get() == curL1.get())
      {
        if (!areMatching)
        {
          matchStart = curL1;
        }
        areMatching = true;
      }
      else
      {
        areMatching = false;
      }
    }

  return matchStart;
}
void OverlappingNoCycleListsWrapper(TimedExecutor &executor,
                                    shared_ptr<ListNode<int>> l0,
                                    shared_ptr<ListNode<int>> l1,
                                    shared_ptr<ListNode<int>> common)
{
  if (common)
  {
    if (l0)
    {
      auto i = l0;
      while (i->next)
      {
        i = i->next;
      }
      i->next = common;
    }
    else
    {
      l0 = common;
    }

    if (l1)
    {
      auto i = l1;
      while (i->next)
      {
        i = i->next;
      }
      i->next = common;
    }
    else
    {
      l1 = common;
    }
  }

  auto result = executor.Run([&]
                             { return OverlappingNoCycleLists(l0, l1); });

  if (result != common)
  {
    throw TestFailure("Invalid result");
  }
}

int main(int argc, char *argv[])
{
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "l0", "l1", "common"};
  return GenericTestMain(
      args, "do_terminated_lists_overlap.cc", "do_terminated_lists_overlap.tsv",
      &OverlappingNoCycleListsWrapper, DefaultComparator{}, param_names);
}
