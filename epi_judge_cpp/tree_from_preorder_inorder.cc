#include <vector>
#include <unordered_map>
#include "binary_tree_node.h"
#include "test_framework/binary_tree_utils.h"
#include "test_framework/generic_test.h"
using std::vector;
using std::unordered_map;
unique_ptr<BinaryTreeNode<int>> BTFromPreInHelper(const vector<int>& pre, size_t pre_start, size_t pre_end, size_t in_start, size_t in_end, const unordered_map<int, size_t>& node_to_inorder_idx){
  if(pre_end<=pre_start || in_end<=in_start)
  return nullptr;

  size_t root_inorder_idx = node_to_inorder_idx.at(pre[pre_start]);
  size_t in_sub_size = root_inorder_idx - in_start;

  return std::make_unique<BinaryTreeNode<int>>(BinaryTreeNode<int>{pre[pre_start], BTFromPreInHelper(pre, pre_start+1, pre_start+1+in_sub_size, in_start, root_inorder_idx, node_to_inorder_idx), BTFromPreInHelper(pre, pre_start+1+in_sub_size, pre_end, root_inorder_idx+1, in_end, node_to_inorder_idx)});

}
unique_ptr<BinaryTreeNode<int>> BinaryTreeFromPreorderInorder(
    const vector<int>& preorder, const vector<int>& inorder) {
  std::unordered_map<int, size_t> mp;
for(size_t i = 0; i < inorder.size();++i){
  mp.insert({{inorder[i], i}});
}
  return BTFromPreInHelper(preorder, 0, preorder.size(), 0, inorder.size(), mp);
  
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"preorder", "inorder"};
  return GenericTestMain(
      args, "tree_from_preorder_inorder.cc", "tree_from_preorder_inorder.tsv",
      &BinaryTreeFromPreorderInorder, DefaultComparator{}, param_names);
}



