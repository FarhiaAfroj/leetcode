int dfs(struct TreeNode* root, int num) {
    if (root == NULL)
        return 0;

    num = (num << 1) | root->val;

    if (root->left == NULL && root->right == NULL)
        return num;

    return dfs(root->left, num) + dfs(root->right, num);
}

int sumRootToLeaf(struct TreeNode* root) {
    return dfs(root, 0);
}