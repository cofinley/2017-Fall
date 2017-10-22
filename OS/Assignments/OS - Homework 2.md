# OS - Homework 2

> Connor Finley
>
> 2017/10/21



## 1

> A system has a total of 8 resources of a particular type. There are 4 processes running with their maximum resources needs and current allocation of resources as shown below:

| Process | Current Allocation | Max. Need |
| ------- | :----------------: | :-------: |
| P1      |         1          |     3     |
| P2      |         1          |     2     |
| P3      |         2          |     5     |
| P4      |         2          |     6     |



### a

> Specify all the safe sequence from the state shown above.

m = 8

n = 4

Resources left over (m - allocated) = 8 - (1 + 1 + 2 + 2) = 2

Need = max - allocation

| Process | Need |
| ------- | ---- |
| P1      | 2    |
| P2      | 1    |
| P3      | 3    |
| P4      | 4    |

P1 first to get resources: (resources - P1 need >= 0), 0 resources left over

P1 finishes and releases resources (3), leaving 3 resources available in total



P2 is next to get resources (1), 2 resources now left over

P2 finishes and releases resources (2), leaving 4 resources available in total



P3 is next to get resources (3), 1 resource now left over

P3 finishes and releases resources (5), leaving 6 resources available in total



P4 is next to get resources (4), 2 resources now left over

P4 finishes and releases resources (6), leaving 8 resources available in total

Safe sequence: \<P1, P2, P3, P4>



### b.

> If P4 were to request 1 resource, should the request be granted? (Yes or No)
>
> If yes –then indicate a safe sequence from the resulting state
>
> If No –then indicate the sequence of steps that would lead to a deadlock

Yes, P4's request would be granted, the sequence can already accommodate P4. If its cost were less, it wouldn't be a problem. Safe sequence would still be \<P1, P2, P3, P4>.