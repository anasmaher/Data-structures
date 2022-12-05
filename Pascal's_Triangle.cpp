// LeetCode solution
class Solution {
public:
    vector<vector<int>> generate(int r) {
        vector<vector<int>>v(r);

        for(int i=0 ; i<r ; i++){
            for(int j=0 ; j<=i ; j++){
                if(j==0 || j==i) v[i].push_back(1);
                else v[i].push_back(v[i-1][j]+v[i-1][j-1]);
            }
        }
        return v;
    }
};
