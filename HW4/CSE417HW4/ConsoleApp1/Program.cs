using System;
using System.Collections.Generic;
using System.Text;
using static System.Console;

namespace HW4
{
    /// <summary>
    /// A class for static random methods. The name is kinda random too. Like... what if I just name
    /// classes and fields names as name of fictional characters. Then I name methods verbs and
    /// adverb.... Will that make coding as fun as creative writing?
    /// </summary>
    public static class KissMe
    {
        public static IList<int>[] RandGraph(int n, double p)
        {
            Random r = new Random();
            IList<int>[] G = new IList<int>[n];
            for (int I = 0; I < G.Length; G[I++] = new List<int>()) ;
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


        /// <summary>
        /// The result will get printed out to the console and 
        /// you should copy then and get the image elsewhere. 
        /// </summary>
        public static void HW4P4Print(
            int n = 1000,
            double p_start = 0.002, 
            double p_end = 0.02,
            int N = 10)
        {
            double[] EdgeDensity = new double[N];
            for (double P = p_start, delta = (p_end - p_start) / N;
                P <= p_end;
                P += delta)
            {
                var G = new SimpleGraph(RandGraph(n, P));
                WriteLine($"Ded Distribution with p = {P}; n = {n};");
                foreach (KeyValuePair<int, int> kvp in G.GetDegStats())
                {
                    WriteLine($"Deg = {kvp.Key}, Frequency = {kvp.Value}");
                }
            }
        }
    }

    public class SimpleGraph
    {
        protected int Maxdeg;
        // The max degree of the graph. 
        protected int[] Components;
        // maps vertex to connected component ID.

        protected int[] Degree;
        // Maps the vertex to its degree. 

        protected IDictionary<int, int> DegFreq;
        // Maps the degree of vertex to its frequency of appearance in the graph. 

        protected IDictionary<int, int> ComponentSize;

        protected IList<int>[] G; // Graph represented by adjacency-list
                                  // Maps component ID to component size.
        protected int TotalComponent;


        public SimpleGraph(IList<int>[] AdjList)
        {
            if (AdjList.Length <= 1) throw new Exception("Invalid Adjacency-List");
            G = AdjList;
            Components = new int[AdjList.Length];
            ComponentSize = new Dictionary<int, int>();
            TotalComponent = ComponentsSearch();
            Degree = CountDegree();
        }

        /// <summary> Performs a component search for this given graph. </summary> </return> the
        /// total number of components involved. </return>
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

        /// <summary>
        /// Perform the DFS search on a certain index.
        /// </summary>
        /// <param name="starting">The vertex that starts the search.</param>
        /// <param name="com">The name of component you want to call for this DFS search</param>
        /// <returns>The size of the component of DFS search.</returns>
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

        public IDictionary<int, int> GetComponentSize()
        {
            return ComponentSize;
        }

        /// <summary>
        /// Produce stats from the graph about the connectivity of the graph.
        /// </summary>
        /// <returns>
        /// total number of connected component of g, average size of the connected component,
        /// max component size, min component size, standard deviation of the connected component. }
        /// </returns>
        public double[] ProduceStats()
        {
            double sum = 0, sumsq = 0,
                max = Double.NegativeInfinity,
                min = Double.PositiveInfinity;
            foreach (int k in ComponentSize.Keys)
            {
                int size = ComponentSize[k];
                sum += size;
                sumsq += Math.Pow(size, 2);
                max = Math.Max(max, size);
                min = Math.Min(min, size);
            }
            double[] res = new double[]
            {
                TotalComponent,
                sum/TotalComponent,
                max,
                min,
                Math.Sqrt(sumsq/TotalComponent - Math.Pow(sum/TotalComponent, 2))
            };
            return res;
        }

        public override string ToString()
        {
            string res = "adjlist:\n";
            StringBuilder sb = new StringBuilder(res);
            for (int I = 0; I < G.Length; I++)
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

        /// <summary>
        /// Get a list of neighbors for vertex v.
        /// </summary>
        /// <param name="v">An integer of the vertex.</param>
        /// <returns>An IList containing all the vertex that v is linked to. s</returns>
        protected IList<int> N(int v)
        {
            return G[v];
        }

        /// <summary>
        /// The method establish the degree filed for the class. 
        /// It will assume that the graph is a directed graph. 
        /// To get the degree for the undirected graph, 
        /// the degree needs to be divided by 2. 
        /// <returns>
        /// It will return an array that maps the vertex to its degree. 
        /// </returns>
        /// </summary>
        protected int[] CountDegree()
        {
            int[] res = new int[G.Length];
            for (int I = 0; I < G.Length; res[I] = G[I].Count, I++);
            return res;
        }

        /// <summary>
        /// It counts the frequency of different vertex degree in the graph. 
        /// The graph will be viewed as a directed graph. 
        /// </summary>
        /// <returns></returns>
        public IDictionary<int, int> GetDegStats(bool undirected = true)
        {
            var res = new SortedDictionary<int, int>();
            for (int I = 0; I < Degree.Length; I++)
            {
                int feq = 0;
                res.TryGetValue(I, out feq);
                res[I] = feq + 1;
            }
            if (undirected)
            {
                foreach (int K in res.Keys) res[K] /= 2;
            }
            return res; 
        }
    }

    internal class Program
    {
        private static void Main(string[] args)
        {
            // IList<int>[] adjlist = KissMe.RandGraph(5, 1); for (int I = 0; I < adjlist.Length;
            // I++) { Write($"{I}: "); foreach (int n in adjlist[I]) { Write($"{n} "); }
            // WriteLine(); }

            PrintResults();
            WriteLine("Press enter to exit.");
            ReadKey();
        }

        /// <summary>
        /// Function will print result for this experiment to the console.
        /// </summary>
        private static void PrintResults()
        {
            int n = (int)1e4;
            double range = 1.5e-3;

            int N = 30;
            double delta = range / N;
            double[] p = new double[N];
            for (int I = 0; I < N; I++)
            {
                p[I] = Math.Log(n) / n - range + (I + N / 2) * delta;
            }
            WriteLine("The graph has 10^4 vertex and it's randomly generated with different " +
                "edge density, here is the statistics regarding it's connected components: ");
            WriteLine("Vertex, Edge_Density, TotalComponents, Max_Component_Size" +
                ", Min_Component_size, Size_SD");
            for (int I = 0; I < p.Length; I++)
            {
                //0, 2, 3, 4
                var G = KissMe.RandGraph(n, p[I]);
                var g = new SimpleGraph(G);
                var res = g.ProduceStats();
                WriteLine($"{n}, {p[I]}, {res[0]}, {res[2]}, {res[3]}, {res[4]}");
            }
        }
    }
}