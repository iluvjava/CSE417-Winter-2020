using System;
using System.Collections.Generic;
using System.Text;
using static System.Console;
namespace Problem5
{
    class Program
    {
        static void Main(string[] args)
        {
            WriteLine("Hello World!");

            IList<int>[] adjlist = KissMe.RandGraph(5, 1);
            for (int I = 0; I < adjlist.Length; I++)
            {
                Write($"{I}: ");
                foreach (int n in adjlist[I])
                {
                    Write($"{n} ");
                }
                WriteLine();
            }
            ReadLine();
        }
    }

    /// <summary>
    /// A class for static random methods. 
    /// The name is kinda random too. 
    /// Like... what if I just name classes and fields names as name of fictional characters.
    /// Then I name methods verbs and adverb.... 
    /// Will that make coding as fun as creative writing? 
    /// </summary>
    public static class KissMe
    {
        public static IList<int>[] RandGraph(int n, double p)
        {
            Random r = new Random();
            IList<int>[] G = new IList<int>[n];
            for (int I = 0; I < G.Length; G[I++] = new List<int>());
            for (int I = 0; I < n; I++)
                for (int J = I + 1; J < n; J++)
                {
                    if (r.NextDouble() <= p)
                    {
                        G[I].Add(J);
                        G[J].Add(I);
                    }
                }
            return G;
        }
    }

    public class SimpleGraphSearch
    {
        IList<int>[] G; // Graph represented by adjacency-list
        int[] Components; // maps vertex to connected component ID. 
        IDictionary<int, int> ComponentSize; // Maps component ID to component size. 

        public SimpleGraphSearch(IList<int>[] AdjList)
        {
            if (AdjList.Length <= 1) throw new Exception("Invalid Adjacency-List");
            G = AdjList;
            Components = new int[AdjList.Length];
            ComponentSize = new Dictionary<int, int>();
            ComponentsSearch();
        }

        /// <summary>
        /// Get a list of neighbors for vertex v. 
        /// </summary>
        /// <param name="v">
        /// An integer of the vertex. 
        /// </param>
        /// <returns>
        /// An IList containing all the vertex that v is linked to. s
        /// </returns>
        protected IList<int> N(int v)
        {
            return G[v];
        }

        /// <summary>
        /// Perform the DFS search on a certain index. 
        /// </summary>
        /// <param name="starting">
        /// The vertex that starts the search. 
        /// </param>
        /// <param name="com">
        /// The name of component you want to call for this DFS search
        /// </param>
        /// <returns>
        /// The size of the component of DFS search. 
        /// </returns>
        public int DFS(int starting = 0, int com = 1)
        {
            Queue<int> q = new Queue<int>();
            q.Enqueue(starting);
            Components[starting] = com;
            int res = 1;
            while (q.Count != 0)
                foreach (int v in N(q.Dequeue()))
                {
                    if (Components[v] == 0)
                    {
                        res++;
                        Components[v] = com;
                        q.Enqueue(v);
                    }
                }
            return res;
        }

        /// <summary>
        /// Performs a component search for this given graph. 
        /// </summary>
        /// </return>
        /// the total number of components involved.
        /// </return>
        public int ComponentsSearch()
        {
            ComponentSize[1] = DFS();
            int component = 2;
            for (int I = 1; I < G.Length; I++)
            {
                if (Components[I] == 0)
                {
                    ComponentSize[component] = DFS(I, component++);
                }
            }
            return component - 1;
        }

        public override string ToString()
        {
            string res = "adjlist:\n";
            StringBuilder sb = new StringBuilder(res);
            for(int I = 0; I < G.Length; I++)
            {
                sb.Append($"{I}:");
                foreach (int v in N(I))
                {
                    sb.Append($" {v}");
                }
                sb.Append("\n");
            }
            sb.Append("Components Assignments: \n");
            for (int I = 0; I < Components.Length; I++)
                sb.Append($"{I}: {Components[I]}\n");
            sb.Append("Components Sizes:\n");
            foreach (int c in ComponentSize.Keys)
            {
                sb.Append($"{c}: {ComponentSize[c]}\n");
            }
            return sb.ToString();
        }

        public IDictionary<int, int> GetComponentSize()
        {
            return ComponentSize;
        }

        /// <summary>
        /// Produce stats from the graph about the connectivity of the graph. 
        /// </summary>
        /// <returns>
        /// {
        ///     total number of connected component of g, 
        ///     average size of the connected component, 
        ///     max component size, 
        ///     min component size,
        ///     standard deviation of the connected component. 
        /// } 
        /// </returns>
        public double[] ProduceStats()
        {
            throw new NotImplementedException();
        }

    }

    
}
