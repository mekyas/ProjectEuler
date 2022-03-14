#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int orderOfLargestPlusSign(int n, vector<vector<int> >& mines) {
        int ans=0, l=0, r=0;
        while(l<n){
            for(r=l; r<n-ans; r++){
                cout << l << " " << r << "\n";
                int order = is_plus(l, r, n, mines);
                cout << order << "\n";
                if(order>ans){
                    ans=order;
                    l = ans-1;
                    break;
                }
            }
            l+=1;
        }
        return ans;
    }
    int is_plus(int l, int r, int n, vector<vector<int> >& mines){
        if (mines[l][r]==0) return 0;
        int order=1;
        cout << l+order << " " << l-order << " " << r+order << " " << r-order << "\n";
        while(l+order<n && l-order>=0 && r+order<n && r-order>=0){
            cout << l+order << " " << l-order << " " << r+order << " " << r-order << "\n";
            if(mines[l+order][r]==1 && mines[l][r+order]==1 && mines[l-order][r]==1 && mines[l][r-order]==1){
                order+=1;
            } else {
                break;
            }
        }
        return order;
    }
};

int main(){
    int n = 5;
    vector<vector<int> > mines(n, vector<int>(n, 1));
    // mines[4][2] = 0;
    Solution solution = Solution();
    int ans = solution.orderOfLargestPlusSign(n, mines);
    cout << ans << endl;
}