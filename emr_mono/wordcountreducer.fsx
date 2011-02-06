open System.Net
open System
open System.IO

//let printSeq seq1 = Seq.iter (printf "%A") seq1; Console.WriteLine("")

//let sumReducer (key:String, values:seq<String[]>) : int =
let sumReducer (key:string, values:seq<string[]>) : int =
    let mutable mysum = 0
    for value in values do
        mysum <- mysum  + Convert.ToInt32(value.[1])
    mysum

let reduceInput (sr:TextReader) =
    Seq.initInfinite (fun _ -> sr.ReadLine())
    |> Seq.takeWhile (fun line -> line <> null)
    |> Seq.map (fun line -> line.Split('\t','\n',' '))
    |> Seq.groupBy (fun line -> line.[0].Trim())

let reduceRunner (sr:TextReader) (f:string * seq<string []> -> int) = 
    for line in reduceInput sr do
        let key,values = line
        //let mysum = sumReducer(key,values)
        let mysum = sumReducer(key,values)
        System.Console.WriteLine(key + "\t" + Convert.ToString(mysum))

reduceRunner Console.In sumReducer
