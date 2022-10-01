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
function logWrapper(a: lazy<any>, message: string) : lazy<any> {
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



