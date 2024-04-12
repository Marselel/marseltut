#include <bits/stdc++.h>

#define ll long long
using namespace std;

ll mod =  1000000007;

//dp[0/1][v] - оптимальное закрытие дорог в поддереве v
//dp[0][v] - если у города v уже закрыли дорогу
//dp[1][v] - если у города v все дороги открыты
template<typename T>
void add(T &a, T &b){
    for (auto item: a)b.push_back(item);
}

void DFS(int v, int p, vector<vector<int>> &g, vector<vector<vector<pair<int,int>>>> &dp){
    dp[0][v] = dp[1][v] = {};
    for (auto to: g[v]){
        if (to == p)continue;
        DFS(to, v, g, dp);
        add(dp[1][to], dp[0][v]);
    }

    dp[1][v] = dp[0][v];
    for (auto to: g[v]){
        if (to == p)continue;
        if (dp[1][v].size() < dp[0][v].size()-dp[1][to].size()+dp[0][to].size()+1){
            dp[1][v] = {};
            for (auto sosed: g[v]){
                if (sosed == p)continue;
                if (sosed == to)continue;
                add(dp[1][sosed], dp[1][v]);
            }
            add(dp[0][to], dp[1][v]);
            dp[1][v].emplace_back(v, to);
        }
    }
}



int main(){
    int n, m;cin >> n >> m;
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    vector<vector<vector<pair<int, int>>>> dp(2, vector<vector<pair<int, int>>>(n + 1));
    vector<pair<int, int>> ans = {};
    DFS(1, 0, g, dp);
    cout<<dp[1][1].size()<<'\n';
    for (auto [u, v]: dp[1][1]){
        cout<<u<<' '<<v<<'\n';
    }

}
