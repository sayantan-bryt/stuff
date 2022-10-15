console.log("############### Introduction ###############")

function sum(a: number, b: number) : number {
    return a + b;
}

console.log("Eager sum(5+10, 15) : ", sum(5 + 10, 15))

function lazySum(a: () => number, b: () => number) : () => number {
    return () => a() + b()
}

console.log("Lazy lazySum(5+10, 15) : ", lazySum(() => 5 + 10, () => 15))
console.log("Lazy lazySum(5+10, 15)() : ", lazySum(() => 5 + 10, () => 15)())

type lazy<T> = () => T

function lazySumType(a: lazy<number>, b: lazy<number>) : lazy<number> {
    return () => a() + b()
}

console.log("Lazy lazySumType(5+10, 15) : ",   lazySumType(() => 5 + 10, () => 15))
console.log("Lazy lazySumType(5+10, 15)() : ", lazySumType(() => 5 + 10, () => 15)())


console.log("############### Lazy  ###############")

// helper to check if param gets called
function logWrapper<T>(a: lazy<T>, message: string) : lazy<T> {
    return () => {
        console.log("[logWrapper]: Called ", message)
        return a()
    }
}

console.log("\n#### and (&&)  ####")

function and(a: lazy<boolean>, b: lazy<boolean>) : lazy<boolean> {
    return () => a() ? b() : false
}

console.log("true  && true : ", and(logWrapper(() => true , "true "), logWrapper(() => true , "true "))())
console.log("true  && false: ", and(logWrapper(() => true , "true "), logWrapper(() => false, "false"))())
console.log("false && true : ", and(logWrapper(() => false, "false"), logWrapper(() => true , "true "))())
console.log("false && false: ", and(logWrapper(() => false, "false"), logWrapper(() => false, "false"))())



console.log("\n#### or (||)  ####")

function or(a: lazy<boolean>, b: lazy<boolean>) : lazy<boolean> {
    return () => a() ? true : b()
}

console.log("true  || true : ", or(logWrapper(() => true , "true "), logWrapper(() => true , "true "))())
console.log("true  || false: ", or(logWrapper(() => true , "true "), logWrapper(() => false, "false"))())
console.log("false || true : ", or(logWrapper(() => false, "false"), logWrapper(() => true , "true "))())
console.log("false || false: ", or(logWrapper(() => false, "false"), logWrapper(() => false, "false"))())



console.log("\n#### first ####")

function hang<T>(): T {
    return hang()
}

function first<T>(a: T, b: T): T {
    return a
}

function lazyFirst<T>(a: lazy<T>, b: lazy<T>): lazy<T> {
    return () => a()
}

// hangs for ever since eager
//console.log(first(() => 5, hang()))
console.log(lazyFirst(logWrapper(() => 5, "first"), logWrapper(() => hang(), "second"))())

console.log("############### LazyLists ###############")

type lazyList<T> = lazy<{
    head: lazy<T>,
    tail: lazyList<T>
} | null>


function range(begin: lazy<number>): lazyList<number> {
    return () => {
        const x: number = begin()
        return {
            head: () => x,
            tail: range(() => x + 1)
        }
    }
}

console.log("\n---\nRange\n---\n")
console.log(range(() => 2)()!.head())
console.log(range(() => 2)()!.tail()!.head())
console.log(range(() => 2)()!.tail()!.tail()!.head())
console.log(range(() => 2)()!.tail()!.tail()!.tail()!.head())
console.log(range(() => 2)()!.tail()!.tail()!.tail()!.tail()!.head())

function printList<T>(xs : lazyList<T>) {
    let pair = xs();
    while(pair !== null) {
        let x = pair.head()
        console.log(x)
        pair = pair.tail()
    }
}

console.log("\n---\nPrintList\n---\n")
//printList(range(() => 3))


console.log("\n---\nTake\n---\n")
console.log("Take 10 numbers starting from 3:\n")

function take<T>(xs: lazyList<T>, n: number): lazyList<T> {
        const pair = xs()
        if (pair === null) {
            return () => null
        } else if(n <= 0) {
            return () => null
        }
        return () => {
            return {
                head: pair.head,
                tail: take(pair.tail, n-1)
            }
        }

}

printList(take(range(() => 3), 10))


console.log("\n---\nFilter\n---\n")
console.log("Even numbers:\n")

function filter<T>(f: (x: T) => boolean, xs: lazyList<T>): lazyList<T> {
    const pair = xs()
    if(pair === null)
        return () => null;
    const x = pair.head()
    if(f(x)) {
        return () => {
            return {
                head: () => x,
                tail: filter(f, pair.tail)
            }
        }
    }
    return filter(f, pair.tail)
}

printList(
    take(
        filter(
            (x: number) => x % 2 == 0,
                range(() => 2)
        ),
        10
    )
)

console.log("\n---\nSieve\n---\n")

function sieve(xs: lazyList<number>) : lazyList<number> {
    const pair = xs()
    if (pair === null)
        return () => null
    const head = pair.head()
    return () => {
            return {
                head: () => head,
                tail: sieve(filter((x: number) => x % head !== 0, pair.tail))
            }
        }
}

//printList(sieve(range(() => 2)))
printList(take(sieve(range(() => 2)), 10))

console.log("\n---\nMersenne Primes\n---\n")

function mersenne(primes: lazyList<number>) : lazyList<number> {
    return filter((x: number) => ((x+1) & (x)) === 0, primes)
}


// FIXME:
/*

printList(take(mersenne(sieve(range(() => 2))), 4))

error: Uncaught RangeError: Maximum call stack size exceeded
            tail: range(() => x + 1)
                        ^
    at file:///Users/sayantan.samajpati/stuff/prac/stuff/lazyeval/src/index.ts:93:25
    at file:///Users/sayantan.samajpati/stuff/prac/stuff/lazyeval/src/index.ts:90:27
    at filter (file:///Users/sayantan.samajpati/stuff/prac/stuff/lazyeval/src/index.ts:144:18)
    at filter (file:///Users/sayantan.samajpati/stuff/prac/stuff/lazyeval/src/index.ts:156:12)
    at file:///Users/sayantan.samajpati/stuff/prac/stuff/lazyeval/src/index.ts:152:23
    at filter (file:///Users/sayantan.samajpati/stuff/prac/stuff/lazyeval/src/index.ts:144:18)
    at filter (file:///Users/sayantan.samajpati/stuff/prac/stuff/lazyeval/src/index.ts:156:12)
    at file:///Users/sayantan.samajpati/stuff/prac/stuff/lazyeval/src/index.ts:152:23
    at filter (file:///Users/sayantan.samajpati/stuff/prac/stuff/lazyeval/src/index.ts:144:18)
    at file:///Users/sayantan.samajpati/stuff/prac/stuff/lazyeval/src/index.ts:152:23
*/

printList(
    take(
        mersenne(
            sieve(range(() => 2))
        ),
        3
    )
)


console.log("\n---\nSampling\n---\n")
console.log("### Reservoir Sampling: \n")

// TODO: https://stackoverflow.com/questions/54059/efficiently-selecting-a-set-of-random-elements-from-a-linked-list
// implement efficient sampling from sieve

/*
Let R be the result array of size s
Let I be an input queue

> Fill the reservoir array
for j in the range [1,s]:
  R[j]=I.pop()

elements_seen=s
while I is not empty:
  elements_seen+=1
  j=random(1,elements_seen)       > This is inclusive
  if j<=s:
    R[j]=I.pop()
  else:
    I.pop()

*/

type Scale = {
    l: number,
    r: number
}

function r_rand(x: number, new_p: Scale, old_p: Scale = {l: 0, r: 1}): number {
    const slope: number = 1.0 * (new_p.r - new_p.l) / (old_p.r - old_p.l)
    const res: number = new_p.l + slope * (x - old_p.l)
    return res
}

function sample<T>(xs: lazyList<T>, n: number, k: number) : Array<T> {
    let res: Array<T> = new Array(k)
    let pair = xs()
    for(let i = 0; i < k; i++) {
        res[i] = pair!.head()
        pair = pair!.tail()
    }
    let seen = k
    while (seen < n) {
        seen += 1
        const pos = Math.round(r_rand(Math.random(), {l: 1, r: seen}))
        if (pos < k) {
            res[pos] = pair!.head()
        }
        pair = pair!.tail()
    }
    return res;
}

console.log(sample(range(() => 2), 120, 5))

export {}
