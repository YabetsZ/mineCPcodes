impl Solution {
    pub fn fib(n: i32) -> i32 {
        if n < 2 {
        return n;
        }
        let mut fib_vec = Vec::with_capacity(4 * (n as usize + 1));
        fib_vec.push(0);
        fib_vec.push(1);
        for i in 2..=n as usize {
            fib_vec.push(fib_vec[i - 1] + fib_vec[i - 2]);
        }
        fib_vec[n as usize]
    }
}