using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
 
public class WordCountMapper
{
	static public void Main ()
	{
		String line;
		while( (line = Console.ReadLine()) != null) {
		    try {
		        line.Trim().Split(' ')
			     .Where(s => !String.IsNullOrEmpty(s.Trim()))
			     .ToList()
			     .ForEach(term => Console.Write(term.ToLower().Trim() + "\t1\n"));
		    } catch( System.Exception e) {
		    }
		}
	}
}
