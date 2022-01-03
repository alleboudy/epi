#include "binary_tree_node.h"
#include "test_framework/generic_test.h"
bool CheckSymmetry(const unique_ptr<BinaryTreeNode<int>> &l, const unique_ptr<BinaryTreeNode<int>> &r);

bool IsSymmetric(const unique_ptr<BinaryTreeNode<int>> &tree)
{
  return tree==nullptr || CheckSymmetry(tree->left,tree->right);
}

bool CheckSymmetry(const unique_ptr<BinaryTreeNode<int>> &l, const unique_ptr<BinaryTreeNode<int>> &r){

  if(nullptr==l && nullptr==r)
  return true;

  if(l!=nullptr && r!=nullptr)
  return l->data==r->data && CheckSymmetry(l->left, r->right) && CheckSymmetry(l->right, r->left);

  return false;

}

int main(int argc, char *argv[])
{
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"tree"};
  return GenericTestMain(args, "is_tree_symmetric.cc", "is_tree_symmetric.tsv",
                         &IsSymmetric, DefaultComparator{}, param_names);
}
