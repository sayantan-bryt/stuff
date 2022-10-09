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

console.log("---\nRange\n---\n")
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

console.log("---\nPrintList\n---\n")
//printList(range(() => 3))


console.log("---\nTake\n---\n")
console.log("Take 10 numbers starting from 3:\n")

function take<T>(xs: lazyList<T>, n: number): lazyList<T> {
        const pair = xs()
        if (pair === null) {
            return () => null
        } else if(n < 0) {
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


console.log("---\nFilter\n---\n")
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

console.log("---\nSieve\n---\n")

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


export {}
