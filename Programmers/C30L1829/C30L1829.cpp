#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;
int ds_find(map<int, int> &disjointset, int a) {
    if (a == disjointset[a]) {
        return a;
    }
    return disjointset[a] = ds_find(disjointset, disjointset[a]);
}
void ds_union(map<int, int> &disjointset, int a, int b) {
    auto pa = ds_find(disjointset, a);
    auto pb = ds_find(disjointset, b);
    if (pa == pb) {
        return;
    }
    disjointset[pa] = disjointset[pb];
}
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    vector<vector<int>> areas(m);
    map<int, int> counter{{0, 0}};
    map<int, int> disjointset{};
    int ntag = 0;
    int tag = ntag;
    generate(areas.begin(), areas.end(), [=]() { return vector<int>(n); });
    for (int y = 0; y < m; y++) {
        for (int x = 0; x < n; x++) {
            if (picture[y][x] == 0) {
                continue;
            }
            if (y > 0 && picture[y - 1][x] == picture[y][x]) {
                tag = areas[y - 1][x];
            } else if (x == 0 || picture[y][x - 1] != picture[y][x]) {
                tag = ++ntag;
                disjointset[tag] = tag;
            }
            areas[y][x] = tag;
            counter[tag]++;
            if (x > 0 && areas[y][x - 1] != areas[y][x] &&
                picture[y][x - 1] == picture[y][x]) {
                ds_union(disjointset, areas[y][x - 1], areas[y][x]);
            }
            if (y > 0 && areas[y - 1][x] != areas[y][x] &&
                picture[y - 1][x] == picture[y][x]) {
                ds_union(disjointset, areas[y][x - 1], areas[y][x]);
            }
        }
    }
    for_each(disjointset.cbegin(), disjointset.cend(), [&](auto &eq) {
        if (eq.first != eq.second) {
            counter[ds_find(disjointset, eq.first)] += counter[eq.first];
        }
    });
    return {
        int(count_if(disjointset.cbegin(), disjointset.cend(),
                     [](auto &eq) { return eq.first == eq.second; })),
        max_element(counter.cbegin(), counter.cend(),
                    [](auto &a, auto &b) { return a.second < b.second; })
            ->second,
    };
}

int main(int argc, char const *argv[]) {
    // auto a = solution(6, 4,
    //                   {{1, 1, 1, 0},
    //                    {1, 2, 2, 0},
    //                    {1, 0, 0, 1},
    //                    {0, 0, 0, 1},
    //                    {0, 0, 0, 3},
    //                    {0, 0, 0, 3}});
    // auto a = solution(3, 6,
    //                   {
    //                       {1, 1, 0, 0, 1, 1},
    //                       {3, 1, 1, 1, 1, 0},
    //                       {3, 3, 1, 0, 1, 0},
    //                   });
    // auto a = solution(3, 6,
    //                   {
    //                       {1, 0, 1, 0, 1, 0},
    //                       {1, 1, 1, 1, 1, 1},
    //                       {0, 0, 0, 0, 0, 1},
    //                   });
    // auto a = solution(2, 2, {{1, 1}, {0, 1}});
    // auto a = solution(6, 4,
    //              {{1, 1, 1, 0},
    //               {1, 2, 2, 0},
    //               {1, 0, 0, 1},
    //               {0, 0, 0, 1},
    //               {0, 0, 0, 3},
    //               {0, 0, 0, 3}});
    auto a = solution(6, 4,
                      {{1, 0, 0, 1},
                       {1, 0, 1, 1},
                       {1, 0, 0, 1},
                       {1, 0, 1, 1},
                       {1, 0, 0, 1},
                       {1, 1, 1, 1}});
    // auto a = solution(1, 1, {{0}});
    // auto a = solution(4, 4,
    //              {{1, 1, 1, 1}, {1, 4, 1, 1}, {1, 3, 2, 1}, {1, 1, 1, 1}});

    // auto apheche = solution(13, 16,
    //                         {
    //                             {
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 1,
    //                                 1,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                             },
    //                             {
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                             },
    //                             {
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                             },
    //                             {
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 0,
    //                                 0,
    //                                 0,
    //                             },
    //                             {
    //                                 0,
    //                                 0,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 0,
    //                                 0,
    //                             },
    //                             {
    //                                 0,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 2,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 2,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 0,
    //                             },
    //                             {
    //                                 0,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 2,
    //                                 1,
    //                                 2,
    //                                 1,
    //                                 1,
    //                                 2,
    //                                 1,
    //                                 2,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 0,
    //                             },
    //                             {
    //                                 0,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 0,
    //                             },
    //                             {
    //                                 0,
    //                                 1,
    //                                 3,
    //                                 3,
    //                                 3,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 3,
    //                                 3,
    //                                 3,
    //                                 1,
    //                                 0,
    //                             },
    //                             {
    //                                 0,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 2,
    //                                 1,
    //                                 1,
    //                                 2,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 0,
    //                             },
    //                             {
    //                                 0,
    //                                 0,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 2,
    //                                 2,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 0,
    //                                 0,
    //                             },
    //                             {
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 0,
    //                                 0,
    //                                 0,
    //                             },
    //                             {
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 1,
    //                                 0,
    //                                 0,
    //                                 0,
    //                                 0,
    //                             },
    //                         });
    return 0;
}
