class MyQueue {
    private _s1: number[];
    private _s2: number[];
    constructor() {
        this._s1 = [];
        this._s2 = [];
    }

    push(x: number): void {
        this._s1.push(x);
    }

    pop(): number {
        if(this._s2.length === 0){
            while(this._s1.length > 0){
                this._s2.push(this._s1.pop());
            }
        }
        return this._s2.pop();
    }

    peek(): number {
        if(this._s2.length === 0){
            while(this._s1.length > 0){
                this._s2.push(this._s1.pop()!);
            }
        }
        return this._s2[this._s2.length - 1];
    }

    empty(): boolean {
        return this._s1.length === 0 && this._s2.length === 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */