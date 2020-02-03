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
        /// <summary>
        /// The result will get printed out to the console and
        /// you should copy then and get the image elsewhere.
        ///
        /// The printed result will be formatted as json file for convenience.
        /// </summary>
        public static void HW4P4Print(
            int n = 1000,
            double p_start = 0.002,
            double p_end = 0.02,
            int N = 10)
        {
            double[] EdgeDensity = new double[N];
            StringBuilder sb = new StringBuilder();
            sb.AppendLine("[");

            for (double P = p_start, delta = (p_end - p_start) / N;
                P <= p_end;
                P += delta)
            {
                var G = new SimpleGraph(RandGraph(n, P));
                //output.WriteLine($"Ded Distribution with p = {P}; n = {n};");
                sb.AppendLine("{");
                sb.AppendLine($"\t\"p\":{P},");
                sb.AppendLine($"\t\"n\":{n},");
                foreach (KeyValuePair<int, int> kvp in G.GetDegStats())
                {
                    sb.AppendLine($"\t\"{kvp.Key}\": {kvp.Value},");
                }
                sb.Remove(sb.Length - 3, 2);
                sb.AppendLine("},");
            }
            sb.Remove(sb.Length - 3, 2);
            sb.AppendLine("]");
            WriteLine(sb.ToString());
        }

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
    }

    /// Simple graph, simple rick.
    /// Go watch Rick and Morty Season 4, I am going to 
    /// watch it during spring break. 
    public class SimpleGraph
    {
        // The max degree of the graph.
        protected int[] Components;
        protected IDictionary<int, int> ComponentSize;
        protected IDictionary<int, int> DegFreq;
        protected int[] Degree;

        // maps vertex to connected component ID.
        // Maps the vertex to its degree.
        // Maps the degree of vertex to its frequency of appearance in the graph.
        protected IList<int>[] G;

        protected int Maxdeg = -1;

        // Graph represented by adjacency-list
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

        [Obsolete]
        /// <summary>
        /// This method will return an array that contains all the coloring 
        /// information, it will maps each 
        /// of the vertex to a color. 
        /// The number of color is bounded by the max degree of vertex in the graph. 
        /// </summary>
        /// <returns>
        /// An int[] array. 
        /// </returns>
        public int[] GetColors()
        {
            int k = Maxdeg + 1;
            int[] vertexColoring = new int[G.Length];
            // Uncoloring all vertex. 
            for (int I = 0; I < G.Length; vertexColoring[I++] = -1);
            // For each vertex
            for (int I = 0; I < G.Length; I++)
            {
                var ColorNotUsed = new SortedSet<int>();
                for (int J = 0; J < k; J++) ColorNotUsed.Add(J);
                foreach (int v in N(I))
                {
                    if (vertexColoring[v] != -1 && ColorNotUsed.Contains(vertexColoring[v]))
                        ColorNotUsed.Remove(vertexColoring[v]);
                }
                // For each colored vertex, color it with the smallest color that is not used. 
                vertexColoring[I] = ColorNotUsed.Min;
            }
            return vertexColoring;
        }

        /// <summary> Performs a component search for this given graph. </summary> </return> the
        /// total number of components involved. </return>
        public int ComponentsSearch()
        {
            ComponentSize[1] = BFS();
            int component = 2;
            for (int I = 1; I < G.Length; I++)
            {
                if (Components[I] == 0)
                {
                    ComponentSize[component] = BFS(I, component++);
                }
            }
            return component - 1;
        }

        /// <summary>
        /// Perform the BFS search on a certain index.
        /// </summary>
        /// <param name="starting">The vertex that starts the search.</param>
        /// <param name="com">The name of component you want to call for this DFS search</param>
        /// <returns>The size of the component of DFS search.</returns>
        public int BFS(int starting = 0, int com = 1)
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
        /// It counts the frequency of different vertex degree in the graph.
        /// The graph will be viewed as a directed graph.
        /// </summary>
        /// <returns></returns>
        public IDictionary<int, int> GetDegStats()
        {
            var res = new SortedDictionary<int, int>();
            for (int I = 0; I < Degree.Length; I++)
            {
                if (res.ContainsKey(Degree[I]))
                    res[Degree[I]]++;
                else
                    res[Degree[I]] = 1;
            }
            return res;
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
        /// The method establish the degree filed for the class.
        /// <returns>
        /// It will return an array that maps the vertex to its degree.
        /// </returns>
        /// </summary>
        protected int[] CountDegree()
        {
            int[] res = new int[G.Length];
            for (int I = 0; I < G.Length; I++)
            {
                res[I] = G[I].Count;
                Maxdeg = Math.Max(res[I], Maxdeg);
            }
            return res;
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
        /// This is a factory method that will construct the undirected simple graph and then 
        /// you can use it for testing things easily. 
        /// 
        /// To construct a graph, simply specify total number of vertex, 
        /// use 2 arrray, such that, the ith edge in the graph is: {arr1[i], arr2[i]}
        /// 
        /// undirectedness, you don't need to swapp the number from arr1 to 
        /// make the algorithm to add them in both direction.
        /// </summary>
        /// <param name="n">
        /// The total number of vertices that are in the grapgh.
        /// </param>
        /// <param name="arr1">
        /// The vertex is indexed from 0 -> n -1
        /// </param>
        /// <param name="arr2">
        /// </param>
        /// The vertex is index from 0 -> n-1
        /// <returns>
        /// An instance of the simple graph. 
        /// </returns>
        public static SimpleGraph MakeGraph(int n, int[] arr1, int[] arr2)
        {
            IList<int>[] G = new IList<int>[n];
            for (int I = 0; I < n; G[I++] = new List<int>());
            if (arr1.Length != arr2.Length) throw new ArgumentException("Invalid Edges.");
            if (n <= 0) throw new ArgumentException("Number of vertices should be a natrual number.");
            for (int I = 0; I < arr1.Length; I++)
            {
                int v = arr1[I];
                int u = arr2[I];
                if (v >= n || u >= n) throw new ArgumentException("Edge index not in range. ");
                if (G[v].Contains(u)) continue;
                G[v].Add(u);
                G[u].Add(v);
            }
            return new SimpleGraph(G);
        }

        /// <summary>
        /// The method returns a copy of the adjacency list of the graph for testing 
        /// 
        /// </summary>
        /// <returns>
        /// IList<int>[]
        /// </returns>
        public IList<int>[] GetDeepCopyOfAdjList()
        {
            IList<int>[] thecopy = new IList<int>[G.Length];
            for (int I = 0; I < G.Length; thecopy[I++] = new List<int>()) ;
            for (int I = 0; I < G.Length; I++)
            {
                foreach (int v in G[I]) thecopy[I].Add(v);
            }
            return thecopy;
        }
    }

    internal class Program
    {
        private static void Main(string[] args)
        {
            // IList<int>[] adjlist = KissMe.RandGraph(5, 1); for (int I = 0; I < adjlist.Length;
            // I++) { Write($"{I}: "); foreach (int n in adjlist[I]) { Write($"{n} "); }
            // WriteLine(); }
            //PrintResults();
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