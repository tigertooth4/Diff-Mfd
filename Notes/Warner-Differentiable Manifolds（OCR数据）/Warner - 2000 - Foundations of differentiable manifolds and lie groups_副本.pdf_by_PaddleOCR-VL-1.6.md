FOUNDATIONS

of DIFFERENTIABLE MANIFOLDS

and LIE GROUPS

FRANK W. WARNER

University of Pennsylvania

CATEDRA DE

GEOMETRIA DIPERENCIAL

F. I. U.

Scott, Foresman and Company

Glenview, Illinois London

# Editor's Preface

This textbook fills a long-standing gap. The beginning graduate student finds it hard to learn the basic material on differentiable manifolds. All the books he is referred to give a cursory treatment and quickly move on to more specialized topics. For this reason, Professor Warner's book is especially welcome. Here is a clear, detailed, and careful development of the fundamental facts on manifold theory and Lie groups. Numerous problems extend the theory and help the student master the subject. An added bonus is the sheaf-theoretic proof of the de Rham theorem and an elementary proof of the Hodge theorem. As far as I know, the latter proof is the only one in the literature easily accessible to the novice in analysis.

1. M. Singer

### Preface

This book provides the necessary foundation for students interested in any of the diverse areas of mathematics which require the notion of a differentiable manifold. It is designed as a beginning graduate-level textbook and presumes a good undergraduate training in algebra and analysis plus some knowledge of point set topology, covering spaces, and the fundamental group. It is also intended for use as a reference book since it includes a number of items which are difficult to ferret out of the literature, in particular, the complete and self-contained proofs of the fundamental theorems of Hodge and de Rham.

The core material is contained in Chapters 1, 2, and 4. This includes differentiable manifolds, tangent vectors, submanifolds, implicit function theorems, vector fields, distributions and the Frobenius theorem, differential forms, integration, Stokes' theorem, and de Rham cohomology.

Chapter 3 treats the foundations of Lie group theory, including the relationship between Lie groups and their Lie algebras, the exponential map, the adjoint representation, and the closed subgroup theorem. Many examples are given, and many properties of the classical groups are derived. The chapter concludes with a discussion of homogeneous manifolds. The standard reference for Lie group theory for over two decades has been Chevalley's Theory of Lie Groups, to which I am greatly indebted.

For the de Rham theorem, which is the main goal of Chapter 5, axiomatic sheaf cohomology theory is developed. In addition to a proof of the strong form of the de Rham theorem—the de Rham homomorphism given by integration is a ring isomorphism from the de Rham cohomology ring to the differentiable singular cohomology ring—it is proved that there are canonical isomorphisms of all the classical cohomology theories on manifolds. The pertinent parts of all these theories are developed in the text. The approach which I have followed for axiomatic sheaf cohomology is due to H. Cartan, who gave an exposition in his Séminaire 1950/1951.

For the Hodge theorem, a complete treatment of the local theory of elliptic operators is presented in Chapter 6, using Fourier series as the basic tool. Only a slight acquaintance with Hilbert spaces is presumed. I wish to thank Jerry Kazdan, who spent a large portion of the summer of 1969 educating me to the whys and wherefores of inequalities and who provided considerable assistance with the preparation of this chapter. I also benefited from notes on lectures by J. J. Kohn and Stephen Andrea, from several papers of Louis Nirenberg, and from Partial Differential

Equations by Bers, John, and Schechter, which the reader might wish to consult for further references to the literature.

At the end of each chapter is a set of exercises. These are an integral part of the text. Often where a claim in a chapter has been left to the reader, there is a reminder in the Exercises that the reader should provide a proof of the claim. Some exercises are routine and test general understanding of the chapter. Many present significant extensions of the text. In some cases the exercises contain major theorems. Two notable examples are properties of the eigenfunctions of the Laplacian and the Peter-Weyl theorem, which are developed in the Exercises for Chapter 6. Hints are provided for many of the difficult exercises.

There are a few notable omissions in the text. I have not treated complex manifolds, although the sheaf theory developed in Chapter 5 will provide the reader with one of the basic tools for the study of complex manifolds. Neither have I treated infinite dimensional manifolds, for which I refer the reader to Lang's Introduction to Differentiable Manifolds, nor Sard's theorem and imbedding theorems, which the reader can find in Sternberg's Lectures on Differential Geometry.

Several possible courses can be based on this text. Typical one-semester courses would cover the core material of Chapters 1, 2, and 4, and then either Chapter 3 or 5 or 6, depending on the interests of the class. The entire text can be covered in a one-year course.

Students who wish to continue with further study in differential geometry should consult such advanced texts as Differential Geometry and Symmetric Spaces by Helgason, Geometry of Manifolds by Bishop and Crittenden, and Foundations of Differential Geometry (2 vols.) by Kobayashi and Nomizu.

I am happy to express my gratitude to Professor I. M. Singer, from whom I learned much of the material in this book and whose courses have always generated a great excitement and enthusiasm for the subject.

Many people generously devoted considerable time and effort to reading early versions of the manuscript and making many corrections and helpful suggestions. I particularly wish to thank Manfredo do Carmo, Jerry Kazdan, Stuart Newberger, Marc Riefel, John Thorpe, Nolan Wallach, Hung-Hsi Wu, and the students in my classes at the University of California at Berkeley and at the University of Pennsylvania. My special thanks to Jeanne Robinson, Marian Griffiths, and Mary Ann Hipple for their excellent job of typing, and to Nat Weintraub of Scott, Foresman and Company for his cooperation and excellent guidance and assistance in the final preparation of the manuscript.

Frank Warner

## Contents

## 1 MANIFOLDS

MANIFOLDS    
2 Preliminaries    
5 Differentiable Manifolds    
8 The Second Axiom of Countability    
11 Tangent Vectors and Differentials    
22 Submanifolds, Diffeomorphisms, and the Inverse Function Theorem    
30 Implicit Function Theorems    
34 Vector Fields    
41 Distributions and the Frobenius Theorem    
50 Exercises    
2 TENSORS AND DIFFERENTIAL FORMS    
54 Tensor and Exterior Algebras    
62 Tensor Fields and Differential Forms    
69 The Lie Derivative    
73 Differential Ideals    
77 Exercises    
3 LIE GROUPS    
82 Lie Groups and Their Lie Algebras    
89 Homomorphisms    
92 Lie Subgroups    
98 Coverings    
101 Simply Connected Lie Groups    
102 Exponential Map    
109 Continuous Homomorphisms    
110 Closed Subgroups    
112 The Adjoint Representation    
117 Automorphisms and Derivations of Bilinear Operations and Forms    
120 Homogeneous Manifolds    
132 Exercises

#### INTEGRATION ON MANIFOLDS

138 Orientation

140 Integration on Manifolds

153 de Rham Cohomology

157 Exercises

5 SHEAVES, COHOMOLOGY, AND THE DE RHAM THEOREM

163 Sheaves and Presheaves

173 Cochain Complexes

176 Axiomatic Sheaf Cohomology

The Classical Cohomology Theories

186 Alexander-Spanier Cohomology

189 de Rham Cohomology

191 Singular Cohomology

200 Čech Cohomology

205 The de Rham Theorem

207 Multiplicative Structure

214 Supports

216 Exercises

#### ⑥ THE HODGE THEOREM

220 The Laplace-Beltrami Operator

222 The Hodge Theorem

227 Some Calculus

240 Elliptic Operators

243 Reduction to the Periodic Case

250 Ellipticity of the Laplace-Beltrami Operator

251 Exercises

260 BIBLIOGRAPHY

262 INDEX OF NOTATION

265 INDEX



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>15</td><td style='text-align: center; word-wrap: break-word;'>16</td><td style='text-align: center; word-wrap: break-word;'>17</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>19</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>22</td><td style='text-align: center; word-wrap: break-word;'>23</td><td style='text-align: center; word-wrap: break-word;'>24</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'>26</td><td style='text-align: center; word-wrap: break-word;'>27</td><td style='text-align: center; word-wrap: break-word;'>28</td><td style='text-align: center; word-wrap: break-word;'>29</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>31</td><td style='text-align: center; word-wrap: break-word;'>32</td><td style='text-align: center; word-wrap: break-word;'>33</td><td style='text-align: center; word-wrap: break-word;'>34</td><td style='text-align: center; word-wrap: break-word;'>35</td><td style='text-align: center; word-wrap: break-word;'>36</td><td style='text-align: center; word-wrap: break-word;'>37</td><td style='text-align: center; word-wrap: break-word;'>38</td><td style='text-align: center; word-wrap: break-word;'>39</td><td style='text-align: center; word-wrap: break-word;'>40</td><td style='text-align: center; word-wrap: break-word;'>41</td><td style='text-align: center; word-wrap: break-word;'>42</td><td style='text-align: center; word-wrap: break-word;'>43</td><td style='text-align: center; word-wrap: break-word;'>44</td><td style='text-align: center; word-wrap: break-word;'>45</td><td style='text-align: center; word-wrap: break-word;'>46</td><td style='text-align: center; word-wrap: break-word;'>47</td><td style='text-align: center; word-wrap: break-word;'>48</td><td style='text-align: center; word-wrap: break-word;'>49</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>51</td><td style='text-align: center; word-wrap: break-word;'>52</td><td style='text-align: center; word-wrap: break-word;'>53</td><td style='text-align: center; word-wrap: break-word;'>54</td><td style='text-align: center; word-wrap: break-word;'>55</td><td style='text-align: center; word-wrap: break-word;'>56</td><td style='text-align: center; word-wrap: break-word;'>57</td><td style='text-align: center; word-wrap: break-word;'>58</td><td style='text-align: center; word-wrap: break-word;'>59</td><td style='text-align: center; word-wrap: break-word;'>60</td><td style='text-align: center; word-wrap: break-word;'>61</td><td style='text-align: center; word-wrap: break-word;'>62</td><td style='text-align: center; word-wrap: break-word;'>63</td><td style='text-align: center; word-wrap: break-word;'>64</td><td style='text-align: center; word-wrap: break-word;'>65</td><td style='text-align: center; word-wrap: break-word;'>66</td><td style='text-align: center; word-wrap: break-word;'>67</td><td style='text-align: center; word-wrap: break-word;'>68</td><td style='text-align: center; word-wrap: break-word;'>69</td><td style='text-align: center; word-wrap: break-word;'>70</td><td style='text-align: center; word-wrap: break-word;'>71</td><td style='text-align: center; word-wrap: break-word;'>72</td><td style='text-align: center; word-wrap: break-word;'>73</td><td style='text-align: center; word-wrap: break-word;'>74</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>76</td><td style='text-align: center; word-wrap: break-word;'>77</td><td style='text-align: center; word-wrap: break-word;'>78</td><td style='text-align: center; word-wrap: break-word;'>79</td><td style='text-align: center; word-wrap: break-word;'>80</td><td style='text-align: center; word-wrap: break-word;'>81</td><td style='text-align: center; word-wrap: break-word;'>82</td><td style='text-align: center; word-wrap: break-word;'>83</td><td style='text-align: center; word-wrap: break-word;'>84</td><td style='text-align: center; word-wrap: break-word;'>85</td><td style='text-align: center; word-wrap: break-word;'>86</td><td style='text-align: center; word-wrap: break-word;'>87</td><td style='text-align: center; word-wrap: break-word;'>88</td><td style='text-align: center; word-wrap: break-word;'>89</td><td style='text-align: center; word-wrap: break-word;'>90</td><td style='text-align: center; word-wrap: break-word;'>91</td><td style='text-align: center; word-wrap: break-word;'>92</td><td style='text-align: center; word-wrap: break-word;'>93</td><td style='text-align: center; word-wrap: break-word;'>94</td><td style='text-align: center; word-wrap: break-word;'>95</td><td style='text-align: center; word-wrap: break-word;'>96</td><td style='text-align: center; word-wrap: break-word;'>97</td><td style='text-align: center; word-wrap: break-word;'>98</td><td style='text-align: center; word-wrap: break-word;'>99</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>101</td><td style='text-align: center; word-wrap: break-word;'>102</td><td style='text-align: center; word-wrap: break-word;'>103</td><td style='text-align: center; word-wrap: break-word;'>104</td><td style='text-align: center; word-wrap: break-word;'>105</td><td style='text-align: center; word-wrap: break-word;'>106</td><td style='text-align: center; word-wrap: break-word;'>107</td><td style='text-align: center; word-wrap: break-word;'>108</td><td style='text-align: center; word-wrap: break-word;'>109</td><td style='text-align: center; word-wrap: break-word;'>110</td><td style='text-align: center; word-wrap: break-word;'>111</td><td style='text-align: center; word-wrap: break-word;'>112</td><td style='text-align: center; word-wrap: break-word;'>113</td><td style='text-align: center; word-wrap: break-word;'>114</td><td style='text-align: center; word-wrap: break-word;'>115</td><td style='text-align: center; word-wrap: break-word;'>116</td><td style='text-align: center; word-wrap: break-word;'>117</td><td style='text-align: center; word-wrap: break-word;'>118</td><td style='text-align: center; word-wrap: break-word;'>119</td><td style='text-align: center; word-wrap: break-word;'>120</td><td style='text-align: center; word-wrap: break-word;'>121</td><td style='text-align: center; word-wrap: break-word;'>122</td><td style='text-align: center; word-wrap: break-word;'>123</td><td style='text-align: center; word-wrap: break-word;'>124</td><td style='text-align: center; word-wrap: break-word;'>125</td><td style='text-align: center; word-wrap: break-word;'>126</td><td style='text-align: center; word-wrap: break-word;'>127</td><td style='text-align: center; word-wrap: break-word;'>128</td><td style='text-align: center; word-wrap: break-word;'>129</td><td style='text-align: center; word-wrap: break-word;'>130</td><td style='text-align: center; word-wrap: break-word;'>131</td><td style='text-align: center; word-wrap: break-word;'>132</td><td style='text-align: center; word-wrap: break-word;'>133</td><td style='text-align: center; word-wrap: break-word;'>134</td><td style='text-align: center; word-wrap: break-word;'>135</td><td style='text-align: center; word-wrap: break-word;'>136</td><td style='text-align: center; word-wrap: break-word;'>137</td><td style='text-align: center; word-wrap: break-word;'>138</td><td style='text-align: center; word-wrap: break-word;'>139</td><td style='text-align: center; word-wrap: break-word;'>140</td><td style='text-align: center; word-wrap: break-word;'>141</td><td style='text-align: center; word-wrap: break-word;'>142</td><td style='text-align: center; word-wrap: break-word;'>143</td><td style='text-align: center; word-wrap: break-word;'>144</td><td style='text-align: center; word-wrap: break-word;'>145</td><td style='text-align: center; word-wrap: break-word;'>146</td><td style='text-align: center; word-wrap: break-word;'>147</td><td style='text-align: center; word-wrap: break-word;'>148</td><td style='text-align: center; word-wrap: break-word;'>149</td><td style='text-align: center; word-wrap: break-word;'>150</td><td style='text-align: center; word-wrap: break-word;'>151</td><td style='text-align: center; word-wrap: break-word;'>152</td><td style='text-align: center; word-wrap: break-word;'>153</td><td style='text-align: center; word-wrap: break-word;'>154</td><td style='text-align: center; word-wrap: break-word;'>155</td><td style='text-align: center; word-wrap: break-word;'>156</td><td style='text-align: center; word-wrap: break-word;'>157</td><td style='text-align: center; word-wrap: break-word;'>158</td><td style='text-align: center; word-wrap: break-word;'>159</td><td style='text-align: center; word-wrap: break-word;'>160</td><td style='text-align: center; word-wrap: break-word;'>161</td><td style='text-align: center; word-wrap: break-word;'>162</td><td style='text-align: center; word-wrap: break-word;'>163</td><td style='text-align: center; word-wrap: break-word;'>164</td><td style='text-align: center; word-wrap: break-word;'>165</td><td style='text-align: center; word-wrap: break-word;'>166</td><td style='text-align: center; word-wrap: break-word;'>167</td><td style='text-align: center; word-wrap: break-word;'>168</td><td style='text-align: center; word-wrap: break-word;'>169</td><td style='text-align: center; word-wrap: break-word;'>170</td><td style='text-align: center; word-wrap: break-word;'>171</td><td style='text-align: center; word-wrap: break-word;'>172</td><td style='text-align: center; word-wrap: break-word;'>173</td><td style='text-align: center; word-wrap: break-word;'>174</td><td style='text-align: center; word-wrap: break-word;'>175</td><td style='text-align: center; word-wrap: break-word;'>176</td><td style='text-align: center; word-wrap: break-word;'>177</td><td style='text-align: center; word-wrap: break-word;'>178</td><td style='text-align: center; word-wrap: break-word;'>179</td><td style='text-align: center; word-wrap: break-word;'>180</td><td style='text-align: center; word-wrap: break-word;'>181</td><td style='text-align: center; word-wrap: break-word;'>182</td><td style='text-align: center; word-wrap: break-word;'>183</td><td style='text-align: center; word-wrap: break-word;'>184</td><td style='text-align: center; word-wrap: break-word;'>185</td><td style='text-align: center; word-wrap: break-word;'>186</td><td style='text-align: center; word-wrap: break-word;'>187</td><td style='text-align: center; word-wrap: break-word;'>188</td><td style='text-align: center; word-wrap: break-word;'>189</td><td style='text-align: center; word-wrap: break-word;'>190</td><td style='text-align: center; word-wrap: break-word;'>191</td><td style='text-align: center; word-wrap: break-word;'>192</td><td style='text-align: center; word-wrap: break-word;'>193</td><td style='text-align: center; word-wrap: break-word;'>194</td><td style='text-align: center; word-wrap: break-word;'>195</td><td style='text-align: center; word-wrap: break-word;'>196</td><td style='text-align: center; word-wrap: break-word;'>197</td><td style='text-align: center; word-wrap: break-word;'>198</td><td style='text-align: center; word-wrap: break-word;'>199</td><td style='text-align: center; word-wrap: break-word;'>200</td><td style='text-align: center; word-wrap: break-word;'>201</td><td style='text-align: center; word-wrap: break-word;'>202</td><td style='text-align: center; word-wrap: break-word;'>203</td><td style='text-align: center; word-wrap: break-word;'>204</td><td style='text-align: center; word-wrap: break-word;'>205</td><td style='text-align: center; word-wrap: break-word;'>206</td><td style='text-align: center; word-wrap: break-word;'>207</td><td style='text-align: center; word-wrap: break-word;'>208</td><td style='text-align: center; word-wrap: break-word;'>209</td><td style='text-align: center; word-wrap: break-word;'>210</td><td style='text-align: center; word-wrap: break-word;'>211</td><td style='text-align: center; word-wrap: break-word;'>212</td><td style='text-align: center; word-wrap: break-word;'>213</td><td style='text-align: center; word-wrap: break-word;'>214</td><td style='text-align: center; word-wrap: break-word;'>215</td><td style='text-align: center; word-wrap: break-word;'>216</td><td style='text-align: center; word-wrap: break-word;'>217</td><td style='text-align: center; word-wrap: break-word;'>218</td><td style='text-align: center; word-wrap: break-word;'>219</td><td style='text-align: center; word-wrap: break-word;'>220</td><td style='text-align: center; word-wrap: break-word;'>221</td><td style='text-align: center; word-wrap: break-word;'>222</td><td style='text-align: center; word-wrap: break-word;'>223</td><td style='text-align: center; word-wrap: break-word;'>224</td><td style='text-align: center; word-wrap: break-word;'>225</td><td style='text-align: center; word-wrap: break-word;'>226</td><td style='text-align: center; word-wrap: break-word;'>227</td><td style='text-align: center; word-wrap: break-word;'>228</td><td style='text-align: center; word-wrap: break-word;'>229</td><td style='text-align: center; word-wrap: break-word;'>230</td><td style='text-align: center; word-wrap: break-word;'>231</td><td style='text-align: center; word-wrap: break-word;'>232</td><td style='text-align: center; word-wrap: break-word;'>233</td><td style='text-align: center; word-wrap: break-word;'>234</td><td style='text-align: center; word-wrap: break-word;'>235</td><td style='text-align: center; word-wrap: break-word;'>236</td><td style='text-align: center; word-wrap: break-word;'>237</td><td style='text-align: center; word-wrap: break-word;'>238</td><td style='text-align: center; word-wrap: break-word;'>239</td><td style='text-align: center; word-wrap: break-word;'>240</td><td style='text-align: center; word-wrap: break-word;'>241</td><td style='text-align: center; word-wrap: break-word;'>242</td><td style='text-align: center; word-wrap: break-word;'>243</td><td style='text-align: center; word-wrap: break-word;'>244</td><td style='text-align: center; word-wrap: break-word;'>245</td><td style='text-align: center; word-wrap: break-word;'>246</td><td style='text-align: center; word-wrap: break-word;'>247</td><td style='text-align: center; word-wrap: break-word;'>248</td><td style='text-align: center; word-wrap: break-word;'>249</td><td style='text-align: center; word-wrap: break-word;'>250</td><td style='text-align: center; word-wrap: break-word;'>251</td><td style='text-align: center; word-wrap: break-word;'>252</td><td style='text-align: center; word-wrap: break-word;'>253</td><td style='text-align: center; word-wrap: break-word;'>254</td><td style='text-align: center; word-wrap: break-word;'>255</td><td style='text-align: center; word-wrap: break-word;'>256</td><td style='text-align: center; word-wrap: break-word;'>257</td><td style='text-align: center; word-wrap: break-word;'>258</td><td style='text-align: center; word-wrap: break-word;'>259</td><td style='text-align: center; word-wrap: break-word;'>260</td><td style='text-align: center; word-wrap: break-word;'>261</td><td style='text-align: center; word-wrap: break-word;'>262</td><td style='text-align: center; word-wrap: break-word;'>263</td><td style='text-align: center; word-wrap: break-word;'>264</td><td style='text-align: center; word-wrap: break-word;'>265</td><td style='text-align: center; word-wrap: break-word;'>266</td><td style='text-align: center; word-wrap: break-word;'>267</td><td style='text-align: center; word-wrap: break-word;'>268</td><td style='text-align: center; word-wrap: break-word;'>269</td><td style='text-align: center; word-wrap: break-word;'>270</td><td style='text-align: center; word-wrap: break-word;'>271</td><td style='text-align: center; word-wrap: break-word;'>272</td><td style='text-align: center; word-wrap: break-word;'>273</td><td style='text-align: center; word-wrap: break-word;'>274</td><td style='text-align: center; word-wrap: break-word;'>275</td><td style='text-align: center; word-wrap: break-word;'>276</td><td style='text-align: center; word-wrap: break-word;'>277</td><td style='text-align: center; word-wrap: break-word;'>278</td><td style='text-align: center; word-wrap: break-word;'>279</td><td style='text-align: center; word-wrap: break-word;'>280</td><td style='text-align: center; word-wrap: break-word;'>281</td><td style='text-align: center; word-wrap: break-word;'>282</td><td style='text-align: center; word-wrap: break-word;'>283</td><td style='text-align: center; word-wrap: break-word;'>284</td><td style='text-align: center; word-wrap: break-word;'>285</td><td style='text-align: center; word-wrap: break-word;'>286</td><td style='text-align: center; word-wrap: break-word;'>287</td><td style='text-align: center; word-wrap: break-word;'>288</td><td style='text-align: center; word-wrap: break-word;'>289</td><td style='text-align: center; word-wrap: break-word;'>290</td><td style='text-align: center; word-wrap: break-word;'>291</td><td style='text-align: center; word-wrap: break-word;'>292</td><td style='text-align: center; word-wrap: break-word;'>293</td><td style='text-align: center; word-wrap: break-word;'>294</td><td style='text-align: center; word-wrap: break-word;'>295</td><td style='text-align: center; word-wrap: break-word;'>296</td><td style='text-align: center; word-wrap: break-word;'>297</td><td style='text-align: center; word-wrap: break-word;'>298</td><td style='text-align: center; word-wrap: break-word;'>299</td><td style='text-align: center; word-wrap: break-word;'>300</td><td style='text-align: center; word-wrap: break-word;'>301</td><td style='text-align: center; word-wrap: break-word;'>302</td><td style='text-align: center; word-wrap: break-word;'>303</td><td style='text-align: center; word-wrap: break-word;'>304</td><td style='text-align: center; word-wrap: break-word;'>305</td><td style='text-align: center; word-wrap: break-word;'>306</td><td style='text-align: center; word-wrap: break-word;'>307</td><td style='text-align: center; word-wrap: break-word;'>308</td><td style='text-align: center; word-wrap: break-word;'>309</td><td style='text-align: center; word-wrap: break-word;'>310</td><td style='text-align: center; word-wrap: break-word;'>311</td><td style='text-align: center; word-wrap: break-word;'>312</td><td style='text-align: center; word-wrap: break-word;'>313</td><td style='text-align: center; word-wrap: break-word;'>314</td><td style='text-align: center; word-wrap: break-word;'>315</td><td style='text-align: center; word-wrap: break-word;'>316</td><td style='text-align: center; word-wrap: break-word;'>317</td><td style='text-align: center; word-wrap: break-word;'>318</td><td style='text-align: center; word-wrap: break-word;'>319</td><td style='text-align: center; word-wrap: break-word;'>320</td><td style='text-align: center; word-wrap: break-word;'>321</td><td style='text-align: center; word-wrap: break-word;'>322</td><td style='text-align: center; word-wrap: break-word;'>323</td><td style='text-align: center; word-wrap: break-word;'>324</td><td style='text-align: center; word-wrap: break-word;'>325</td><td style='text-align: center; word-wrap: break-word;'>326</td><td style='text-align: center; word-wrap: break-word;'>327</td><td style='text-align: center; word-wrap: break-word;'>328</td><td style='text-align: center; word-wrap: break-word;'>329</td><td style='text-align: center; word-wrap: break-word;'>330</td><td style='text-align: center; word-wrap: break-word;'>331</td><td style='text-align: center; word-wrap: break-word;'>332</td><td style='text-align: center; word-wrap: break-word;'>333</td><td style='text-align: center; word-wrap: break-word;'>334</td><td style='text-align: center; word-wrap: break-word;'>335</td><td style='text-align: center; word-wrap: break-word;'>336</td><td style='text-align: center; word-wrap: break-word;'>337</td><td style='text-align: center; word-wrap: break-word;'>338</td><td style='text-align: center; word-wrap: break-word;'>339</td><td style='text-align: center; word-wrap: break-word;'>340</td><td style='text-align: center; word-wrap: break-word;'>341</td><td style='text-align: center; word-wrap: break-word;'>342</td><td style='text-align: center; word-wrap: break-word;'>343</td><td style='text-align: center; word-wrap: break-word;'>344</td><td style='text-align: center; word-wrap: break-word;'>345</td><td style='text-align: center; word-wrap: break-word;'>346</td><td style='text-align: center; word-wrap: break-word;'>347</td><td style='text-align: center; word-wrap: break-word;'>348</td><td style='text-align: center; word-wrap: break-word;'>349</td><td style='text-align: center; word-wrap: break-word;'>350</td><td style='text-align: center; word-wrap: break-word;'>351</td><td style='text-align: center; word-wrap: break-word;'>352</td><td style='text-align: center; word-wrap: break-word;'>353</td><td style='text-align: center; word-wrap: break-word;'>354</td><td style='text-align: center; word-wrap: break-word;'>355</td><td style='text-align: center; word-wrap: break-word;'>356</td><td style='text-align: center; word-wrap: break-word;'>357</td><td style='text-align: center; word-wrap: break-word;'>358</td><td style='text-align: center; word-wrap: break-word;'>359</td><td style='text-align: center; word-wrap: break-word;'>360</td><td style='text-align: center; word-wrap: break-word;'>361</td><td style='text-align: center; word-wrap: break-word;'>362</td><td style='text-align: center; word-wrap: break-word;'>363</td><td style='text-align: center; word-wrap: break-word;'>364</td><td style='text-align: center; word-wrap: break-word;'>365</td><td style='text-align: center; word-wrap: break-word;'>366</td><td style='text-align: center; word-wrap: break-word;'>367</td><td style='text-align: center; word-wrap: break-word;'>368</td><td style='text-align: center; word-wrap: break-word;'>369</td><td style='text-align: center; word-wrap: break-word;'>370</td><td style='text-align: center; word-wrap: break-word;'>371</td><td style='text-align: center; word-wrap: break-word;'>372</td><td style='text-align: center; word-wrap: break-word;'>373</td><td style='text-align: center; word-wrap: break-word;'>374</td><td style='text-align: center; word-wrap: break-word;'>375</td><td style='text-align: center; word-wrap: break-word;'>376</td><td style='text-align: center; word-wrap: break-word;'>377</td><td style='text-align: center; word-wrap: break-word;'>378</td><td style='text-align: center; word-wrap: break-word;'>379</td><td style='text-align: center; word-wrap: break-word;'>380</td><td style='text-align: center; word-wrap: break-word;'>381</td><td style='text-align: center; word-wrap: break-word;'>382</td><td style='text-align: center; word-wrap: break-word;'>383</td><td style='text-align: center; word-wrap: break-word;'>384</td><td style='text-align: center; word-wrap: break-word;'>385</td><td style='text-align: center; word-wrap: break-word;'>386</td><td style='text-align: center; word-wrap: break-word;'>387</td><td style='text-align: center; word-wrap: break-word;'>388</td><td style='text-align: center; word-wrap: break-word;'>389</td><td style='text-align: center; word-wrap: break-word;'>390</td><td style='text-align: center; word-wrap: break-word;'>391</td><td style='text-align: center; word-wrap: break-word;'>392</td><td style='text-align: center; word-wrap: break-word;'>393</td><td style='text-align: center; word-wrap: break-word;'>394</td><td style='text-align: center; word-wrap: break-word;'>395</td><td style='text-align: center; word-wrap: break-word;'>396</td><td style='text-align: center; word-wrap: break-word;'>397</td><td style='text-align: center; word-wrap: break-word;'>398</td><td style='text-align: center; word-wrap: break-word;'>399</td><td style='text-align: center; word-wrap: break-word;'>400</td><td style='text-align: center; word-wrap: break-word;'>401</td><td style='text-align: center; word-wrap: break-word;'>402</td><td style='text-align: center; word-wrap: break-word;'>403</td><td style='text-align: center; word-wrap: break-word;'>404</td><td style='text-align: center; word-wrap: break-word;'>405</td><td style='text-align: center; word-wrap: break-word;'>406</td><td style='text-align: center; word-wrap: break-word;'>407</td><td style='text-align: center; word-wrap: break-word;'>408</td><td style='text-align: center; word-wrap: break-word;'>409</td><td style='text-align: center; word-wrap: break-word;'>410</td><td style='text-align: center; word-wrap: break-word;'>411</td><td style='text-align: center; word-wrap: break-word;'>412</td><td style='text-align: center; word-wrap: break-word;'>413</td><td style='text-align: center; word-wrap: break-word;'>414</td><td style='text-align: center; word-wrap: break-word;'>415</td><td style='text-align: center; word-wrap: break-word;'>416</td><td style='text-align: center; word-wrap: break-word;'>417</td><td style='text-align: center; word-wrap: break-word;'>418</td><td style='text-align: center; word-wrap: break-word;'>419</td><td style='text-align: center; word-wrap: break-word;'>420</td><td style='text-align: center; word-wrap: break-word;'>421</td><td style='text-align: center; word-wrap: break-word;'>422</td><td style='text-align: center; word-wrap: break-word;'>423</td><td style='text-align: center; word-wrap: break-word;'>424</td><td style='text-align: center; word-wrap: break-word;'>425</td><td style='text-align: center; word-wrap: break-word;'>426</td><td style='text-align: center; word-wrap: break-word;'>427</td><td style='text-align: center; word-wrap: break-word;'>428</td><td style='text-align: center; word-wrap: break-word;'>429</td><td style='text-align: center; word-wrap: break-word;'>430</td><td style='text-align: center; word-wrap: break-word;'>431</td><td style='text-align: center; word-wrap: break-word;'>432</td><td style='text-align: center; word-wrap: break-word;'>433</td><td style='text-align: center; word-wrap: break-word;'>434</td><td style='text-align: center; word-wrap: break-word;'>435</td><td style='text-align: center; word-wrap: break-word;'>436</td><td style='text-align: center; word-wrap: break-word;'>437</td><td style='text-align: center; word-wrap: break-word;'>438</td><td style='text-align: center; word-wrap: break-word;'>439</td><td style='text-align: center; word-wrap: break-word;'>440</td><td style='text-align: center; word-wrap: break-word;'>441</td><td style='text-align: center; word-wrap: break-word;'>442</td><td style='text-align: center; word-wrap: break-word;'>443</td><td style='text-align: center; word-wrap: break-word;'>444</td><td style='text-align: center; word-wrap: break-word;'>445</td><td style='text-align: center; word-wrap: break-word;'>446</td><td style='text-align: center; word-wrap: break-word;'>447</td><td style='text-align: center; word-wrap: break-word;'>448</td><td style='text-align: center; word-wrap: break-word;'>449</td><td style='text-align: center; word-wrap: break-word;'>450</td><td style='text-align: center; word-wrap: break-word;'>451</td><td style='text-align: center; word-wrap: break-word;'>452</td><td style='text-align: center; word-wrap: break-word;'>453</td><td style='text-align: center; word-wrap: break-word;'>454</td><td style='text-align: center; word-wrap: break-word;'>455</td><td style='text-align: center; word-wrap: break-word;'>456</td><td style='text-align: center; word-wrap: break-word;'>457</td><td style='text-align: center; word-wrap: break-word;'>458</td><td style='text-align: center; word-wrap: break-word;'>459</td><td style='text-align: center; word-wrap: break-word;'>460</td><td style='text-align: center; word-wrap: break-word;'>461</td><td style='text-align: center; word-wrap: break-word;'>462</td><td style='text-align: center; word-wrap: break-word;'>463</td><td style='text-align: center; word-wrap: break-word;'>464</td><td style='text-align: center; word-wrap: break-word;'>465</td><td style='text-align: center; word-wrap: break-word;'>466</td><td style='text-align: center; word-wrap: break-word;'>467</td><td style='text-align: center; word-wrap: break-word;'>468</td><td style='text-align: center; word-wrap: break-word;'>469</td><td style='text-align: center; word-wrap: break-word;'>470</td><td style='text-align: center; word-wrap: break-word;'>471</td><td style='text-align: center; word-wrap: break-word;'>472</td><td style='text-align: center; word-wrap: break-word;'>473</td><td style='text-align: center; word-wrap: break-word;'>474</td><td style='text-align: center; word-wrap: break-word;'>475</td><td style='text-align: center; word-wrap: break-word;'>476</td><td style='text-align: center; word-wrap: break-word;'>477</td><td style='text-align: center; word-wrap: break-word;'>478</td><td style='text-align: center; word-wrap: break-word;'>479</td><td style='text-align: center; word-wrap: break-word;'>480</td><td style='text-align: center; word-wrap: break-word;'>481</td><td style='text-align: center; word-wrap: break-word;'>482</td><td style='text-align: center; word-wrap: break-word;'>483</td><td style='text-align: center; word-wrap: break-word;'>484</td><td style='text-align: center; word-wrap: break-word;'>485</td><td style='text-align: center; word-wrap: break-word;'>486</td><td style='text-align: center; word-wrap: break-word;'>487</td><td style='text-align: center; word-wrap: break-word;'>488</td><td style='text-align: center; word-wrap: break-word;'>489</td><td style='text-align: center; word-wrap: break-word;'>490</td><td style='text-align: center; word-wrap: break-word;'>491</td><td style='text-align: center; word-wrap: break-word;'>492</td><td style='text-align: center; word-wrap: break-word;'>493</td><td style='text-align: center; word-wrap: break-word;'>494</td><td style='text-align: center; word-wrap: break-word;'>495</td><td style='text-align: center; word-wrap: break-word;'>496</td><td style='text-align: center; word-wrap: break-word;'>497</td><td style='text-align: center; word-wrap: break-word;'>498</td><td style='text-align: center; word-wrap: break-word;'>499</td><td style='text-align: center; word-wrap: break-word;'>500</td><td style='text-align: center; word-wrap: break-word;'>501</td><td style='text-align: center; word-wrap: break-word;'>502</td><td style='text-align: center; word-wrap: break-word;'>503</td><td style='text-align: center; word-wrap: break-word;'>504</td><td style='text-align: center; word-wrap: break-word;'>505</td><td style='text-align: center; word-wrap: break-word;'>506</td><td style='text-align: center; word-wrap: break-word;'>507</td><td style='text-align: center; word-wrap: break-word;'>508</td><td style='text-align: center; word-wrap: break-word;'>509</td><td style='text-align: center; word-wrap: break-word;'>510</td><td style='text-align: center; word-wrap: break-word;'>511</td><td style='text-align: center; word-wrap: break-word;'>512</td><td style='text-align: center; word-wrap: break-word;'>513</td><td style='text-align: center; word-wrap: break-word;'>514</td><td style='text-align: center; word-wrap: break-word;'>515</td><td style='text-align: center; word-wrap: break-word;'>516</td><td style='text-align: center; word-wrap: break-word;'>517</td><td style='text-align: center; word-wrap: break-word;'>518</td><td style='text-align: center; word-wrap: break-word;'>519</td><td style='text-align: center; word-wrap: break-word;'>520</td><td style='text-align: center; word-wrap: break-word;'>521</td><td style='text-align: center; word-wrap: break-word;'>522</td><td style='text-align: center; word-wrap: break-word;'>523</td><td style='text-align: center; word-wrap: break-word;'>524</td><td style='text-align: center; word-wrap: break-word;'>525</td><td style='text-align: center; word-wrap: break-word;'>526</td><td style='text-align: center; word-wrap: break-word;'>527</td><td style='text-align: center; word-wrap: break-word;'>528</td><td style='text-align: center; word-wrap: break-word;'>529</td><td style='text-align: center; word-wrap: break-word;'>530</td><td style='text-align: center; word-wrap: break-word;'>531</td><td style='text-align: center; word-wrap: break-word;'>532</td><td style='text-align: center; word-wrap: break-word;'>533</td><td style='text-align: center; word-wrap: break-word;'>534</td><td style='text-align: center; word-wrap: break-word;'>535</td><td style='text-align: center; word-wrap: break-word;'>536</td><td style='text-align: center; word-wrap: break-word;'>537</td><td style='text-align: center; word-wrap: break-word;'>538</td><td style='text-align: center; word-wrap: break-word;'>539</td><td style='text-align: center; word-wrap: break-word;'>540</td><td style='text-align: center; word-wrap: break-word;'>541</td><td style='text-align: center; word-wrap: break-word;'>542</td><td style='text-align: center; word-wrap: break-word;'>543</td><td style='text-align: center; word-wrap: break-word;'>544</td><td style='text-align: center; word-wrap: break-word;'>545</td><td style='text-align: center; word-wrap: break-word;'>546</td><td style='text-align: center; word-wrap: break-word;'>547</td><td style='text-align: center; word-wrap: break-word;'>548</td><td style='text-align: center; word-wrap: break-word;'>549</td><td style='text-align: center; word-wrap: break-word;'>550</td><td style='text-align: center; word-wrap: break-word;'>551</td><td style='text-align: center; word-wrap: break-word;'>552</td><td style='text-align: center; word-wrap: break-word;'>553</td><td style='text-align: center; word-wrap: break-word;'>554</td><td style='text-align: center; word-wrap: break-word;'>555</td><td style='text-align: center; word-wrap: break-word;'>556</td><td style='text-align: center; word-wrap: break-word;'>557</td><td style='text-align: center; word-wrap: break-word;'>558</td><td style='text-align: center; word-wrap: break-word;'>559</td><td style='text-align: center; word-wrap: break-word;'>560</td><td style='text-align: center; word-wrap: break-word;'>561</td><td style='text-align: center; word-wrap: break-word;'>562</td><td style='text-align: center; word-wrap: break-word;'>563</td><td style='text-align: center; word-wrap: break-word;'>564</td><td style='text-align: center; word-wrap: break-word;'>565</td><td style='text-align: center; word-wrap: break-word;'>566</td><td style='text-align: center; word-wrap: break-word;'>567</td><td style='text-align: center; word-wrap: break-word;'>568</td><td style='text-align: center; word-wrap: break-word;'>569</td><td style='text-align: center; word-wrap: break-word;'>570</td><td style='text-align: center; word-wrap: break-word;'>571</td><td style='text-align: center; word-wrap: break-word;'>572</td><td style='text-align: center; word-wrap: break-word;'>573</td><td style='text-align: center; word-wrap: break-word;'>574</td><td style='text-align: center; word-wrap: break-word;'>575</td><td style='text-align: center; word-wrap: break-word;'>576</td><td style='text-align: center; word-wrap: break-word;'>577</td><td style='text-align: center; word-wrap: break-word;'>578</td><td style='text-align: center; word-wrap: break-word;'>579</td><td style='text-align: center; word-wrap: break-word;'>580</td><td style='text-align: center; word-wrap: break-word;'>581</td><td style='text-align: center; word-wrap: break-word;'>582</td><td style='text-align: center; word-wrap: break-word;'>583</td><td style='text-align: center; word-wrap: break-word;'>584</td><td style='text-align: center; word-wrap: break-word;'>585</td><td style='text-align: center; word-wrap: break-word;'>586</td><td style='text-align: center; word-wrap: break-word;'>587</td><td style='text-align: center; word-wrap: break-word;'>588</td><td style='text-align: center; word-wrap: break-word;'>589</td><td style='text-align: center; word-wrap: break-word;'>590</td><td style='text-align: center; word-wrap: break-word;'>591</td><td style='text-align: center; word-wrap: break-word;'>592</td><td style='text-align: center; word-wrap: break-word;'>593</td><td style='text-align: center; word-wrap: break-word;'>594</td><td style='text-align: center; word-wrap: break-word;'>595</td><td style='text-align: center; word-wrap: break-word;'>596</td><td style='text-align: center; word-wrap: break-word;'>597</td><td style='text-align: center; word-wrap: break-word;'>598</td><td style='text-align: center; word-wrap: break-word;'>599</td><td style='text-align: center; word-wrap: break-word;'>600</td><td style='text-align: center; word-wrap: break-word;'>601</td><td style='text-align: center; word-wrap: break-word;'>602</td><td style='text-align: center; word-wrap: break-word;'>603</td><td style='text-align: center; word-wrap: break-word;'>604</td><td style='text-align: center; word-wrap: break-word;'>605</td><td style='text-align: center; word-wrap: break-word;'>606</td><td style='text-align: center; word-wrap: break-word;'>607</td><td style='text-align: center; word-wrap: break-word;'>608</td><td style='text-align: center; word-wrap: break-word;'>609</td><td style='text-align: center; word-wrap: break-word;'>610</td><td style='text-align: center; word-wrap: break-word;'>611</td><td style='text-align: center; word-wrap: break-word;'>612</td><td style='text-align: center; word-wrap: break-word;'>613</td><td style='text-align: center; word-wrap: break-word;'>614</td><td style='text-align: center; word-wrap: break-word;'>615</td><td style='text-align: center; word-wrap: break-word;'>616</td><td style='text-align: center; word-wrap: break-word;'>617</td><td style='text-align: center; word-wrap: break-word;'>618</td><td style='text-align: center; word-wrap: break-word;'>619</td><td style='text-align: center; word-wrap: break-word;'>620</td><td style='text-align: center; word-wrap: break-word;'>621</td><td style='text-align: center; word-wrap: break-word;'>622</td><td style='text-align: center; word-wrap: break-word;'>623</td><td style='text-align: center; word-wrap: break-word;'>624</td><td style='text-align: center; word-wrap: break-word;'>625</td><td style='text-align: center; word-wrap: break-word;'>626</td><td style='text-align: center; word-wrap: break-word;'>627</td><td style='text-align: center; word-wrap: break-word;'>628</td><td style='text-align: center; word-wrap: break-word;'>629</td><td style='text-align: center; word-wrap: break-word;'>630</td><td style='text-align: center; word-wrap: break-word;'>631</td><td style='text-align: center; word-wrap: break-word;'>632</td><td style='text-align: center; word-wrap: break-word;'>633</td><td style='text-align: center; word-wrap: break-word;'>634</td><td style='text-align: center; word-wrap: break-word;'>635</td><td style='text-align: center; word-wrap: break-word;'>636</td><td style='text-align: center; word-wrap: break-word;'>637</td><td style='text-align: center; word-wrap: break-word;'>638</td><td style='text-align: center; word-wrap: break-word;'>639</td><td style='text-align: center; word-wrap: break-word;'>640</td><td style='text-align: center; word-wrap: break-word;'>641</td><td style='text-align: center; word-wrap: break-word;'>642</td><td style='text-align: center; word-wrap: break-word;'>643</td><td style='text-align: center; word-wrap: break-word;'>644</td><td style='text-align: center; word-wrap: break-word;'>645</td><td style='text-align: center; word-wrap: break-word;'>646</td><td style='text-align: center; word-wrap: break-word;'>647</td><td style='text-align: center; word-wrap: break-word;'>648</td><td style='text-align: center; word-wrap: break-word;'>649</td><td style='text-align: center; word-wrap: break-word;'>650</td><td style='text-align: center; word-wrap: break-word;'>651</td><td style='text-align: center; word-wrap: break-word;'>652</td><td style='text-align: center; word-wrap: break-word;'>653</td><td style='text-align: center; word-wrap: break-word;'>654</td><td style='text-align: center; word-wrap: break-word;'>655</td><td style='text-align: center; word-wrap: break-word;'>656</td><td style='text-align: center; word-wrap: break-word;'>657</td><td style='text-align: center; word-wrap: break-word;'>658</td><td style='text-align: center; word-wrap: break-word;'>659</td><td style='text-align: center; word-wrap: break-word;'>660</td><td style='text-align: center; word-wrap: break-word;'>661</td><td style='text-align: center; word-wrap: break-word;'>662</td><td style='text-align: center; word-wrap: break-word;'>663</td><td style='text-align: center; word-wrap: break-word;'>664</td><td style='text-align: center; word-wrap: break-word;'>665</td><td style='text-align: center; word-wrap: break-word;'>666</td><td style='text-align: center; word-wrap: break-word;'>667</td><td style='text-align: center; word-wrap: break-word;'>668</td><td style='text-align: center; word-wrap: break-word;'>669</td><td style='text-align: center; word-wrap: break-word;'>670</td><td style='text-align: center; word-wrap: break-word;'>671</td><td style='text-align: center; word-wrap: break-word;'>672</td><td style='text-align: center; word-wrap: break-word;'>673</td><td style='text-align: center; word-wrap: break-word;'>674</td><td style='text-align: center; word-wrap: break-word;'>675</td><td style='text-align: center; word-wrap: break-word;'>676</td><td style='text-align: center; word-wrap: break-word;'>677</td><td style='text-align: center; word-wrap: break-word;'>678</td><td style='text-align: center; word-wrap: break-word;'>679</td><td style='text-align: center; word-wrap: break-word;'>680</td><td style='text-align: center; word-wrap: break-word;'>681</td><td style='text-align: center; word-wrap: break-word;'>682</td><td style='text-align: center; word-wrap: break-word;'>683</td><td style='text-align: center; word-wrap: break-word;'>684</td><td style='text-align: center; word-wrap: break-word;'>685</td><td style='text-align: center; word-wrap: break-word;'>686</td><td style='text-align: center; word-wrap: break-word;'>687</td><td style='text-align: center; word-wrap: break-word;'>688</td><td style='text-align: center; word-wrap: break-word;'>689</td><td style='text-align: center; word-wrap: break-word;'>690</td><td style='text-align: center; word-wrap: break-word;'>691</td><td style='text-align: center; word-wrap: break-word;'>692</td><td style='text-align: center; word-wrap: break-word;'>693</td><td style='text-align: center; word-wrap: break-word;'>694</td><td style='text-align: center; word-wrap: break-word;'>695</td><td style='text-align: center; word-wrap: break-word;'>696</td><td style='text-align: center; word-wrap: break-word;'>697</td><td style='text-align: center; word-wrap: break-word;'>698</td><td style='text-align: center; word-wrap: break-word;'>699</td><td style='text-align: center; word-wrap: break-word;'>700</td><td style='text-align: center; word-wrap: break-word;'>701</td><td style='text-align: center; word-wrap: break-word;'>702</td><td style='text-align: center; word-wrap: break-word;'>703</td><td style='text-align: center; word-wrap: break-word;'>704</td><td style='text-align: center; word-wrap: break-word;'>705</td><td style='text-align: center; word-wrap: break-word;'>706</td><td style='text-align: center; word-wrap: break-word;'>707</td><td style='text-align: center; word-wrap: break-word;'>708</td><td style='text-align: center; word-wrap: break-word;'>709</td><td style='text-align: center; word-wrap: break-word;'>710</td><td style='text-align: center; word-wrap: break-word;'>711</td><td style='text-align: center; word-wrap: break-word;'>712</td><td style='text-align: center; word-wrap: break-word;'>713</td><td style='text-align: center; word-wrap: break-word;'>714</td><td style='text-align: center; word-wrap: break-word;'>715</td><td style='text-align: center; word-wrap: break-word;'>716</td><td style='text-align: center; word-wrap: break-word;'>717</td><td style='text-align: center; word-wrap: break-word;'>718</td><td style='text-align: center; word-wrap: break-word;'>719</td><td style='text-align: center; word-wrap: break-word;'>720</td><td style='text-align: center; word-wrap: break-word;'>721</td><td style='text-align: center; word-wrap: break-word;'>722</td><td style='text-align: center; word-wrap: break-word;'>723</td><td style='text-align: center; word-wrap: break-word;'>724</td><td style='text-align: center; word-wrap: break-word;'>725</td><td style='text-align: center; word-wrap: break-word;'>726</td><td style='text-align: center; word-wrap: break-word;'>727</td><td style='text-align: center; word-wrap: break-word;'>728</td><td style='text-align: center; word-wrap: break-word;'>729</td><td style='text-align: center; word-wrap: break-word;'>730</td><td style='text-align: center; word-wrap: break-word;'>731</td><td style='text-align: center; word-wrap: break-word;'>732</td><td style='text-align: center; word-wrap: break-word;'>733</td><td style='text-align: center; word-wrap: break-word;'>734</td><td style='text-align: center; word-wrap: break-word;'>735</td><td style='text-align: center; word-wrap: break-word;'>736</td><td style='text-align: center; word-wrap: break-word;'>737</td><td style='text-align: center; word-wrap: break-word;'>738</td><td style='text-align: center; word-wrap: break-word;'>739</td><td style='text-align: center; word-wrap: break-word;'>740</td><td style='text-align: center; word-wrap: break-word;'>741</td><td style='text-align: center; word-wrap: break-word;'>742</td><td style='text-align: center; word-wrap: break-word;'>743</td><td style='text-align: center; word-wrap: break-word;'>744</td><td style='text-align: center; word-wrap: break-word;'>745</td><td style='text-align: center; word-wrap: break-word;'>746</td><td style='text-align: center; word-wrap: break-word;'>747</td><td style='text-align: center; word-wrap: break-word;'>748</td><td style='text-align: center; word-wrap: break-word;'>749</td><td style='text-align: center; word-wrap: break-word;'>750</td><td style='text-align: center; word-wrap: break-word;'>751</td><td style='text-align: center; word-wrap: break-word;'>752</td><td style='text-align: center; word-wrap: break-word;'>753</td><td style='text-align: center; word-wrap: break-word;'>754</td><td style='text-align: center; word-wrap: break-word;'>755</td><td style='text-align: center; word-wrap: break-word;'>756</td><td style='text-align: center; word-wrap: break-word;'>757</td><td style='text-align: center; word-wrap: break-word;'>758</td><td style='text-align: center; word-wrap: break-word;'>759</td><td style='text-align: center; word-wrap: break-word;'>760</td><td style='text-align: center; word-wrap: break-word;'>761</td><td style='text-align: center; word-wrap: break-word;'>762</td><td style='text-align: center; word-wrap: break-word;'>763</td><td style='text-align: center; word-wrap: break-word;'>764</td><td style='text-align: center; word-wrap: break-word;'>765</td><td style='text-align: center; word-wrap: break-word;'>766</td><td style='text-align: center; word-wrap: break-word;'>767</td><td style='text-align: center; word-wrap: break-word;'>768</td><td style='text-align: center; word-wrap: break-word;'>769</td><td style='text-align: center; word-wrap: break-word;'>770</td><td style='text-align: center; word-wrap: break-word;'>771</td><td style='text-align: center; word-wrap: break-word;'>772</td><td style='text-align: center; word-wrap: break-word;'>773</td><td style='text-align: center; word-wrap: break-word;'>774</td><td style='text-align: center; word-wrap: break-word;'>775</td><td style='text-align: center; word-wrap: break-word;'>776</td><td style='text-align: center; word-wrap: break-word;'>777</td><td style='text-align: center; word-wrap: break-word;'>778</td><td style='text-align: center; word-wrap: break-word;'>779</td><td style='text-align: center; word-wrap: break-word;'>780</td><td style='text-align: center; word-wrap: break-word;'>781</td><td style='text-align: center; word-wrap: break-word;'>782</td><td style='text-align: center; word-wrap: break-word;'>783</td><td style='text-align: center; word-wrap: break-word;'>784</td><td style='text-align: center; word-wrap: break-word;'>785</td><td style='text-align: center; word-wrap: break-word;'>786</td><td style='text-align: center; word-wrap: break-word;'>787</td><td style='text-align: center; word-wrap: break-word;'>788</td><td style='text-align: center; word-wrap: break-word;'>789</td><td style='text-align: center; word-wrap: break-word;'>790</td><td style='text-align: center; word-wrap: break-word;'>791</td><td style='text-align: center; word-wrap: break-word;'>792</td><td style='text-align: center; word-wrap: break-word;'>793</td><td style='text-align: center; word-wrap: break-word;'>794</td><td style='text-align: center; word-wrap: break-word;'>795</td><td style='text-align: center; word-wrap: break-word;'>796</td><td style='text-align: center; word-wrap: break-word;'>797</td><td style='text-align: center; word-wrap: break-word;'>798</td><td style='text-align: center; word-wrap: break-word;'>799</td><td style='text-align: center; word-wrap: break-word;'>800</td><td style='text-align: center; word-wrap: break-word;'>801</td><td style='text-align: center; word-wrap: break-word;'>802</td><td style='text-align: center; word-wrap: break-word;'>803</td><td style='text-align: center; word-wrap: break-word;'>804</td><td style='text-align: center; word-wrap: break-word;'>805</td><td style='text-align: center; word-wrap: break-word;'>806</td><td style='text-align: center; word-wrap: break-word;'>807</td><td style='text-align: center; word-wrap: break-word;'>808</td><td style='text-align: center; word-wrap: break-word;'>809</td><td style='text-align: center; word-wrap: break-word;'>810</td><td style='text-align: center; word-wrap: break-word;'>811</td><td style='text-align: center; word-wrap: break-word;'>812</td><td style='text-align: center; word-wrap: break-word;'>813</td><td style='text-align: center; word-wrap: break-word;'>814</td><td style='text-align: center; word-wrap: break-word;'>815</td><td style='text-align: center; word-wrap: break-word;'>816</td><td style='text-align: center; word-wrap: break-word;'>817</td><td style='text-align: center; word-wrap: break-word;'>818</td><td style='text-align: center; word-wrap: break-word;'>819</td><td style='text-align: center; word-wrap: break-word;'>820</td><td style='text-align: center; word-wrap: break-word;'>821</td><td style='text-align: center; word-wrap: break-word;'>822</td><td style='text-align: center; word-wrap: break-word;'>823</td><td style='text-align: center; word-wrap: break-word;'>824</td><td style='text-align: center; word-wrap: break-word;'>825</td><td style='text-align: center; word-wrap: break-word;'>826</td><td style='text-align: center; word-wrap: break-word;'>827</td><td style='text-align: center; word-wrap: break-word;'>828</td><td style='text-align: center; word-wrap: break-word;'>829</td><td style='text-align: center; word-wrap: break-word;'>830</td><td style='text-align: center; word-wrap: break-word;'>831</td><td style='text-align: center; word-wrap: break-word;'>832</td><td style='text-align: center; word-wrap: break-word;'>833</td><td style='text-align: center; word-wrap: break-word;'>834</td><td style='text-align: center; word-wrap: break-word;'>835</td><td style='text-align: center; word-wrap: break-word;'>836</td><td style='text-align: center; word-wrap: break-word;'>837</td><td style='text-align: center; word-wrap: break-word;'>838</td><td style='text-align: center; word-wrap: break-word;'>839</td><td style='text-align: center; word-wrap: break-word;'>840</td><td style='text-align: center; word-wrap: break-word;'>841</td><td style='text-align: center; word-wrap: break-word;'>842</td><td style='text-align: center; word-wrap: break-word;'>843</td><td style='text-align: center; word-wrap: break-word;'>844</td><td style='text-align: center; word-wrap: break-word;'>845</td><td style='text-align: center; word-wrap: break-word;'>846</td><td style='text-align: center; word-wrap: break-word;'>847</td><td style='text-align: center; word-wrap: break-word;'>848</td><td style='text-align: center; word-wrap: break-word;'>849</td><td style='text-align: center; word-wrap: break-word;'>850</td><td style='text-align: center; word-wrap: break-word;'>851</td><td style='text-align: center; word-wrap: break-word;'>852</td><td style='text-align: center; word-wrap: break-word;'>853</td><td style='text-align: center; word-wrap: break-word;'>854</td><td style='text-align: center; word-wrap: break-word;'>855</td><td style='text-align: center; word-wrap: break-word;'>856</td><td style='text-align: center; word-wrap: break-word;'>857</td><td style='text-align: center; word-wrap: break-word;'>858</td><td style='text-align: center; word-wrap: break-word;'>859</td><td style='text-align: center; word-wrap: break-word;'>860</td><td style='text-align: center; word-wrap: break-word;'>861</td><td style='text-align: center; word-wrap: break-word;'>862</td><td style='text-align: center; word-wrap: break-word;'>863</td><td style='text-align: center; word-wrap: break-word;'>864</td><td style='text-align: center; word-wrap: break-word;'>865</td><td style='text-align: center; word-wrap: break-word;'>866</td><td style='text-align: center; word-wrap: break-word;'>867</td><td style='text-align: center; word-wrap: break-word;'>868</td><td style='text-align: center; word-wrap: break-word;'>869</td><td style='text-align: center; word-wrap: break-word;'>870</td><td style='text-align: center; word-wrap: break-word;'>871</td><td style='text-align: center; word-wrap: break-word;'>872</td><td style='text-align: center; word-wrap: break-word;'>873</td><td style='text-align: center; word-wrap: break-word;'>874</td><td style='text-align: center; word-wrap: break-word;'>875</td><td style='text-align: center; word-wrap: break-word;'>876</td><td style='text-align: center; word-wrap: break-word;'>877</td><td style='text-align: center; word-wrap: break-word;'>878</td><td style='text-align: center; word-wrap: break-word;'>879</td><td style='text-align: center; word-wrap: break-word;'>880</td><td style='text-align: center; word-wrap: break-word;'>881</td><td style='text-align: center; word-wrap: break-word;'>882</td><td style='text-align: center; word-wrap: break-word;'>883</td><td style='text-align: center; word-wrap: break-word;'>884</td><td style='text-align: center; word-wrap: break-word;'>885</td><td style='text-align: center; word-wrap: break-word;'>886</td><td style='text-align: center; word-wrap: break-word;'>887</td><td style='text-align: center; word-wrap: break-word;'>888</td><td style='text-align: center; word-wrap: break-word;'>889</td><td style='text-align: center; word-wrap: break-word;'>890</td><td style='text-align: center; word-wrap: break-word;'>891</td><td style='text-align: center; word-wrap: break-word;'>892</td><td style='text-align: center; word-wrap: break-word;'>893</td><td style='text-align: center; word-wrap: break-word;'>894</td><td style='text-align: center; word-wrap: break-word;'>895</td><td style='text-align: center; word-wrap: break-word;'>896</td><td style='text-align: center; word-wrap: break-word;'>897</td><td style='text-align: center; word-wrap: break-word;'>898</td><td style='text-align: center; word-wrap: break-word;'>899</td><td style='text-align: center; word-wrap: break-word;'>900</td><td style='text-align: center; word-wrap: break-word;'>901</td><td style='text-align: center; word-wrap: break-word;'>902</td><td style='text-align: center; word-wrap: break-word;'>903</td><td style='text-align: center; word-wrap: break-word;'>904</td><td style='text-align: center; word-wrap: break-word;'>905</td><td style='text-align: center; word-wrap: break-word;'>906</td><td style='text-align: center; word-wrap: break-word;'>907</td><td style='text-align: center; word-wrap: break-word;'>908</td><td style='text-align: center; word-wrap: break-word;'>909</td><td style='text-align: center; word-wrap: break-word;'>910</td><td style='text-align: center; word-wrap: break-word;'>911</td><td style='text-align: center; word-wrap: break-word;'>912</td><td style='text-align: center; word-wrap: break-word;'>913</td><td style='text-align: center; word-wrap: break-word;'>914</td><td style='text-align: center; word-wrap: break-word;'>915</td><td style='text-align: center; word-wrap: break-word;'>916</td><td style='text-align: center; word-wrap: break-word;'>917</td><td style='text-align: center; word-wrap: break-word;'>918</td><td style='text-align: center; word-wrap: break-word;'>919</td><td style='text-align: center; word-wrap: break-word;'>920</td><td style='text-align: center; word-wrap: break-word;'>921</td><td style='text-align: center; word-wrap: break-word;'>922</td><td style='text-align: center; word-wrap: break-word;'>923</td><td style='text-align: center; word-wrap: break-word;'>924</td><td style='text-align: center; word-wrap: break-word;'>925</td><td style='text-align: center; word-wrap: break-word;'>926</td><td style='text-align: center; word-wrap: break-word;'>927</td><td style='text-align: center; word-wrap: break-word;'>928</td><td style='text-align: center; word-wrap: break-word;'>929</td><td style='text-align: center; word-wrap: break-word;'>930</td><td style='text-align: center; word-wrap: break-word;'>931</td><td style='text-align: center; word-wrap: break-word;'>932</td><td style='text-align: center; word-wrap: break-word;'>933</td><td style='text-align: center; word-wrap: break-word;'>934</td><td style='text-align: center; word-wrap: break-word;'>935</td><td style='text-align: center; word-wrap: break-word;'>936</td><td style='text-align: center; word-wrap: break-word;'>937</td><td style='text-align: center; word-wrap: break-word;'>938</td><td style='text-align: center; word-wrap: break-word;'>939</td><td style='text-align: center; word-wrap: break-word;'>940</td><td style='text-align: center; word-wrap: break-word;'>941</td><td style='text-align: center; word-wrap: break-word;'>942</td><td style='text-align: center; word-wrap: break-word;'>943</td><td style='text-align: center; word-wrap: break-word;'>944</td><td style='text-align: center; word-wrap: break-word;'>945</td><td style='text-align: center; word-wrap: break-word;'>946</td><td style='text-align: center; word-wrap: break-word;'>947</td><td style='text-align: center; word-wrap: break-word;'>948</td><td style='text-align: center; word-wrap: break-word;'>949</td><td style='text-align: center; word-wrap: break-word;'>950</td><td style='text-align: center; word-wrap: break-word;'>951</td><td style='text-align: center; word-wrap: break-word;'>952</td><td style='text-align: center; word-wrap: break-word;'>953</td><td style='text-align: center; word-wrap: break-word;'>954</td><td style='text-align: center; word-wrap: break-word;'>955</td><td style='text-align: center; word-wrap: break-word;'>956</td><td style='text-align: center; word-wrap: break-word;'>957</td><td style='text-align: center; word-wrap: break-word;'>958</td><td style='text-align: center; word-wrap: break-word;'>959</td><td style='text-align: center; word-wrap: break-word;'>960</td><td style='text-align: center; word-wrap: break-word;'>961</td><td style='text-align: center; word-wrap: break-word;'>962</td><td style='text-align: center; word-wrap: break-word;'>963</td><td style='text-align: center; word-wrap: break-word;'>964</td><td style='text-align: center; word-wrap: break-word;'>965</td><td style='text-align: center; word-wrap: break-word;'>966</td><td style='text-align: center; word-wrap: break-word;'>967</td><td style='text-align: center; word-wrap: break-word;'>968</td><td style='text-align: center; word-wrap: break-word;'>969</td><td style='text-align: center; word-wrap: break-word;'>970</td><td style='text-align: center; word-wrap: break-word;'>971</td><td style='text-align: center; word-wrap: break-word;'>972</td><td style='text-align: center; word-wrap: break-word;'>973</td><td style='text-align: center; word-wrap: break-word;'>974</td><td style='text-align: center; word-wrap: break-word;'>975</td><td style='text-align: center; word-wrap: break-word;'>976</td><td style='text-align: center; word-wrap: break-word;'>977</td><td style='text-align: center; word-wrap: break-word;'>978</td><td style='text-align: center; word-wrap: break-word;'>979</td><td style='text-align: center; word-wrap: break-word;'>980</td><td style='text-align: center; word-wrap: break-word;'>981</td><td style='text-align: center; word-wrap: break-word;'>982</td><td style='text-align: center; word-wrap: break-word;'>983</td><td style='text-align: center; word-wrap: break-word;'>984</td><td style='text-align: center; word-wrap: break-word;'>985</td><td style='text-align: center; word-wrap: break-word;'>986</td><td style='text-align: center; word-wrap: break-word;'>987</td><td style='text-align: center; word-wrap: break-word;'>988</td><td style='text-align: center; word-wrap: break-word;'>989</td><td style='text-align: center; word-wrap: break-word;'>990</td><td style='text-align: center; word-wrap: break-word;'>991</td><td style='text-align: center; word-wrap: break-word;'>992</td><td style='text-align: center; word-wrap: break-word;'>993</td><td style='text-align: center; word-wrap: break-word;'>994</td><td style='text-align: center; word-wrap: break-word;'>995</td><td style='text-align: center; word-wrap: break-word;'>996</td><td style='text-align: center; word-wrap: break-word;'>997</td><td style='text-align: center; word-wrap: break-word;'>998</td><td style='text-align: center; word-wrap: break-word;'>999</td><td style='text-align: center; word-wrap: break-word;'>1000</td><td style='text-align: center; word-wrap: break-word;'>1001</td><td style='text-align: center; word-wrap: break-word;'>1002</td><td style='text-align: center; word-wrap: break-word;'>1003</td><td style='text-align: center; word-wrap: break-word;'>1004</td><td style='text-align: center; word-wrap: break-word;'>1005</td><td style='text-align: center; word-wrap: break-word;'>1006</td><td style='text-align: center; word-wrap: break-word;'>1007</td><td style='text-align: center; word-wrap: break-word;'>1008</td><td style='text-align: center; word-wrap: break-word;'>1009</td><td style='text-align: center; word-wrap: break-word;'>1010</td><td style='text-align: center; word-wrap: break-word;'>1011</td><td style='text-align: center; word-wrap: break-word;'>1012</td><td style='text-align: center; word-wrap: break-word;'>1013</td><td style='text-align: center; word-wrap: break-word;'>1014</td><td style='text-align: center; word-wrap: break-word;'>1015</td><td style='text-align: center; word-wrap: break-word;'>1016</td><td style='text-align: center; word-wrap: break-word;'>1017</td><td style='text-align: center; word-wrap: break-word;'>1018</td><td style='text-align: center; word-wrap: break-word;'>1019</td><td style='text-align: center; word-wrap: break-word;'>1020</td><td style='text-align: center; word-wrap: break-word;'>1021</td><td style='text-align: center; word-wrap: break-word;'>1022</td><td style='text-align: center; word-wrap: break-word;'>1023</td><td style='text-align: center; word-wrap: break-word;'>1024</td><td style='text-align: center; word-wrap: break-word;'>1025</td><td style='text-align: center; word-wrap: break-word;'>1026</td><td style='text-align: center; word-wrap: break-word;'>1027</td><td style='text-align: center; word-wrap: break-word;'>1028</td><td style='text-align: center; word-wrap: break-word;'>1029</td><td style='text-align: center; word-wrap: break-word;'>1030</td><td style='text-align: center; word-wrap: break-word;'>1031</td><td style='text-align: center; word-wrap: break-word;'>1032</td><td style='text-align: center; word-wrap: break-word;'>1033</td><td style='text-align: center; word-wrap: break-word;'>1034</td><td style='text-align: center; word-wrap: break-word;'>1035</td><td style='text-align: center; word-wrap: break-word;'>1036</td><td style='text-align: center; word-wrap: break-word;'>1037</td><td style='text-align: center; word-wrap: break-word;'>1038</td><td style='text-align: center; word-wrap: break-word;'>1039</td><td style='text-align: center; word-wrap: break-word;'>1040</td><td style='text-align: center; word-wrap: break-word;'>10</td></tr></table>

After establishing some notational conventions which will be used throughout the book, we will begin with the notion of a differentiable manifold. These are spaces which are locally like Euclidean space and which have enough structure so that the basic concepts of calculus can be carried over. In this first chapter we shall primarily be concerned with the analogs and implications for manifolds of the fundamental theorems of differential calculus. Later, in Chapter 4, we shall consider the theory of integration on manifolds.

From the notion of directional derivative in Euclidean space we will obtain the notion of a tangent vector to a differentiable manifold. We will study mappings between manifolds and the effect that mappings have on tangent vectors. We will investigate the implications for mappings of manifolds of the classical inverse and implicit function theorems. We will see that the fundamental existence and uniqueness theorems for ordinary differential equations translate into existence and uniqueness statements for integral curves of vector fields. The chapter closes with the Frobenius theorem, which pertains to the existence and uniqueness of integral manifolds of involutive distributions on manifolds.

##### PRELIMINARIES

1.1 Some Basic Notation and Terminology Throughout this text we will describe sets either by listings of their elements, for example

 $$ \{a_{1},\ldots,a_{n}\}, $$ 

or by expressions of the form

 $$ \{x\colon P\}, $$ 

which denote the set of all $x$ satisfying property $P$. The expression $a\in A$ means that $a$ is an element of the set $A$. If a set $A$ is a subset of a set $B$ (that is, $a\in B$ whenever $a\in A$), we write $A\subset B$. If $A\subset B$ and $B\subset A$, then $A$ equals $B$, denoted $A=B$. The negations of $\in$, $\subset$ and $=$ are denoted by $\notin$, $\notin$, and $\neq$ respectively. $A$ set $A$ is a proper subset of $B$ if $A\subset B$ but $A\neq B$.

We will denote the empty set by $\varnothing$. We will often denote a collection $\{U_a : \alpha \in A\}$ of sets $U_a$ indexed by the set $A$ simply by $\{U_a\}$ if explicit mention of the index set is not necessary. The union of the sets in the collection $\{U_a : \alpha \in A\}$ will be denoted $\bigcup_{a \in A} U_a$ or simply $\bigcup U_a$. Similarly, their intersection will be denoted $\bigcap_{a \in A} U_a$ or simply $\bigcap U_a$.

 $$ \bigcup_{\alpha\in A}U_{\alpha}=\{a\colon a{~b e l o n g s~t o~s o m e~}U_{\alpha}\}. $$ 

 $$ \bigcap_{a\in A}U_{a}=\{a\colon a{~b e l o n g s~t o~e v e r y~}U_{a}\}. $$ 

The expression $f\colon A\to B$ means that $f$ is a mapping of the set $A$ into the set $B$. When describing a mapping by describing its effect on individual elements, we use the special arrow $\mapsto$; thus “the mapping $m\mapsto f(m)$ of $A$ into $B$” means that $f$ is a mapping of the set $A$ into the set $B$ taking the element $m$ of $A$ into the element $f(m)$ of $B$. If $U\subset A$, then $f\mid U$ denotes the restriction of $f$ to $U$, and $f(U)=\{b\in B: f(a)=b$ for some $a\in U\}$. If $C\subset B$, then $f^{-1}(C)=\{a\in A: f(a)\in C\}$. A mapping $f$ is one-to-one (also denoted 1:1), or injective, if whenever $a$ and $b$ are distinct elements of $A$, then $f(a)\neq f(b)$. A mapping $f$ is onto, or surjective, if $f(A)=B$.

If $f\colon A \to B$ and $g\colon C \to D$, then the composition $g\circ f$ is the map

 $$ g\circ f\colon f^{-1}(B\cap C)\to D $$ 

defined by $g \circ f(a) = g(f(a))$ for every $a \in f^{-1}(B \cap C)$. For notational convenience, we shall not exclude the case in which $f^{-1}(B \cap C) = \varnothing$. That is, given any two mappings $f$ and $g$, we shall consider their composition $g \circ f$ as being defined, with the understanding that the domain of $g \circ f$ may well be the empty set.

The cartesian product  $ A \times B $ of two sets  $ A $ and  $ B $ is the set of all pairs  $ (a, b) $ of points  $ a \in A $ and  $ b \in B $. If  $ f: A \to C $ and  $ g: B \to D $, then the cartesian product  $ f \times g $ of the maps  $ f $ and  $ g $ is the map  $ (a, b) \mapsto (f(a), g(b)) $ of  $ A \times B $ into  $ C \times D $.

We shall denote the identity map on any set by “id.”

A diagram of maps such as

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//70c03fd3-9bd4-4d08-8396-413c3dc5c0ea/markdown_2/imgs/img_in_image_box_394_882_575_1063.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A11Z%2F-1%2F%2F46dbfc2b18f5dcaf548bd4d8ac856d9d5c58a9958180b31e3426fff2426aca28" alt="Image" width="19%" /></div>


is called commutative if  $ g \circ f = h $.

We shall always use the term function to mean a mapping into the real numbers.

## 4 Manifolds

Let  $ d \geq 1 $ be an integer, and let

 $  \mathbb{R}^d = \{a: a = (a_1, \ldots, a_d) \text{ where the } a_i \text{ are real numbers}\}  $.

Then $\mathbb{R}^d$ is the $d$-dimensional Euclidean space. In the case $d=1$, we denote the real line $\mathbb{R}^1$ simply by $\mathbb{R}$. The origin $(0,\ldots,0)$ in Euclidean space of any dimension will be denoted 0. The notations $[a,b]$ and $(a,b)$ denote as usual the intervals of the real line $a\leq t\leq b$ and $a<t<b$ respectively. The function $r_t:\mathbb{R}^d\to\mathbb{R}$ defined by

 $$ r_{i}(a)=a_{i}\;, $$ 

where  $ a = (a_1, \ldots, a_d) \in \mathbb{R}^d $, is called the  $ i $th (canonical) coordinate function on  $ \mathbb{R}^d $. The canonical coordinate function  $ r_1 $ on  $ \mathbb{R} $ will be denoted simply by  $ r $. Thus  $ r(a) = a $ for each  $ a \in \mathbb{R} $. If  $ f: X \to \mathbb{R}^d $, then we let

 $$ f_{t}=r_{t}\circ f, $$ 

where $f_{i}$ is called the $i$th component function of $f$.

If $f\colon \mathbb{R} \to \mathbb{R}$ and $t \in \mathbb{R}$, then we denote the derivative of $f$ at $t$ by

 $$ \begin{array}{r}{\frac{d}{d r}\bigg\vert_{t}(f)=\frac{d f}{d r}\bigg\vert_{t}=\operatorname*{l i m}_{h\to0}\frac{f(t+h)-f(t)}{h}.}\end{array} $$ 

If $f: \mathbb{R}^n \to \mathbb{R}$, if $1 \leq i \leq n$, and if $t = (t_1, \ldots, t_n) \in \mathbb{R}^n$, then we denote the partial derivative of $f$ with respect to $r_t$ at $t$ by

 $$ \frac{\partial}{\partial r_{\mathfrak{t}}}\Big\vert_{t}(f)=\frac{\partial f}{\partial r_{\mathfrak{t}}}\Big\vert_{t}=\operatorname*{l i m}_{\hbar\to0}\frac{f(t_{1},\ldots,t_{\mathfrak{t}-1},t_{\mathfrak{t}}+\hbar,t_{\mathfrak{t}+1},\ldots,t_{n})-f(t)}{\hbar}. $$ 

If $p \in \mathbb{R}^d$, then $B_p(r)$ will denote the open ball of radius $r$ about $p$. The open ball of radius $r$ about the origin will be denoted simply by $B(r)$. $C(r)$ will denote the open cube with sides of length $2r$ about the origin in $\mathbb{R}^d$. That is,

 $$ C(r)=\{(a_{1},\ldots,a_{d})\in\mathbb{R}^{d}\colon|a_{i}|<r\mathrm{f o r~a l l}i\}. $$ 

We shall use C to denote the complex number field and  $ C^{*} $ to denote complex n-space.

 $$ \mathbb{C}^{n}=\{(z_{1},\ldots,z_{n})\colon z_{i}\in\mathbb{C}\mathrm{~f o r~}1\leq i\leq n\}. $$ 

Unless we indicate otherwise, we shall always use the term neighborhood in the sense of open neighborhood. If $A$ is a subset of a topological space, its closure will be denoted by $\widetilde{A}$. If $\varphi$ is a function on a topological space $X$, the support of $\varphi$ is the subset of $X$ defined by

 $$ \mathrm{s u p p}\varphi=\overline{{\varphi^{-1}(\mathbb{R}-\{0\})}}. $$ 

We use the Kronecker index

 $$ \delta_{i j}=\left\{\begin{aligned}{}&{{}1,\quad}&{i=j}\\ {}&{{}0,\quad}&{i\neq j.}\\ \end{aligned}\right. $$ 

If  $ \alpha=(\alpha_{1},\ldots,\alpha_{d}) $ is a d-tuple of non-negative integers, then we set

 $$ [\alpha]=\textstyle\sum\alpha_{i}, $$ 

 $$ \alpha_{1}=\alpha_{1}\alpha_{2}\cdots\alpha_{d}, $$ 

and

 $$ \frac{\partial^{\alpha}}{\partial r^{\alpha}}=\frac{\partial^{[\alpha]}}{\partial r_{1}^{\alpha_{1}}\cdots\partial r_{d}^{\alpha_{d}}}. $$ 

If  $ \alpha = (0, \ldots, 0) $, then we let

 $$ \frac{\partial^{a}}{\partial r^{a}}(f)=f. $$ 

##### DIFFERENTIABLE MANIFOLDS

1.2 Definitions Let $U \subset \mathbb{R}^d$ be open, and let $f: U \to \mathbb{R}$. We say that $f$ is differentiable of class $C^k$ on $U$ (or simply that $f$ is $C^k$), for $k$ a non-negative integer, if the partial derivatives $\partial^n f / \partial r^n$ exist and are continuous on $U$ for $|\alpha| \leq k$. In particular, $f$ is $C^0$ if $f$ is continuous. If $f: U \to \mathbb{R}^n$, then $f$ is differentiable of class $C^k$ if each of the component functions $f_i = r_i \circ f$ is $C^k$. We say that $f$ is $C^\infty$ if it is $C^k$ for all $k \geq 0$.

1.3 Definitions A locally Euclidean space M of dimension d is a Hausdorff topological space M for which each point has a neighborhood homeomorphic to an open subset of Euclidean space  $ R^{\ell} $. If  $ \varphi $ is a homeomorphism of a connected open set  $ U \subset M $ onto an open subset of  $ R^{\ell} $,  $ \varphi $ is called a coordinate map, the functions  $ x_t = r_t \circ \varphi $ are called the coordinate functions, and the pair  $ (U, \varphi) $ (sometimes denoted by  $ (U, x_1, \ldots, x_d) $) is called a coordinate system. A coordinate system  $ (U, \varphi) $ is called a cubic coordinate system if  $ \varphi(U) $ is an open cube about the origin in  $ R^{\ell} $. If  $ m \in U $ and  $ \varphi(m) = 0 $, then the coordinate system is said to be centered at m.

1.4 Definitions A differentiable structure  $ \mathcal{F} $ of class  $ C^k $ ( $ 1 \leq k \leq \infty $) on a locally Euclidean space  $ M $ is a collection of coordinate systems  $ \{(U_a, \varphi_a): a \in A\} $ satisfying the following three properties:

(a)  $ \bigcup_{a\in A} U_a = M $.

(b)  $ \varphi_{\alpha} \circ \varphi_{\beta}^{-1} $ is  $ C^{k} $ for all  $ \alpha, \beta \in A $.

(c) The collection $\mathcal{F}$ is maximal with respect to (b); that is, if $(U,\varphi)$ is a coordinate system such that $\varphi\circ\varphi_{x}^{-1}$ and $\varphi_{x}\circ\varphi^{-1}$ are $C^{k}$ for all $\alpha\in A$, then $(U,\varphi)\in\mathcal{F}$.

## 6 Manifolds

If  $ \mathcal{F}_{0}=\{(U_{a},\varphi_{a})\colon a\in A\} $ is any collection of coordinate systems satisfying properties (a) and (b), then there is a unique differentiable structure  $ \mathcal{F} $ containing  $ \mathcal{F}_{0} $. Namely, let

 $$ \mathcal{F}=\{(U,\varphi)\colon\varphi\circ\varphi_{a}^{-1}\mathrm{~a n d~}\varphi_{a}\circ\varphi^{-1}\stackrel{\circ}{{\mathbf{a r e}}}C^{k}\mathrm{~f o r~a l l~}\varphi_{a}\in\mathcal{F}_{0}\}. $$ 

Then $\mathcal{F}$ contains $\mathcal{F}_{0}$, clearly satisfies (a), and it is easily checked that $\mathcal{F}$ satisfies (b). Now $\mathcal{F}$ is maximal by construction, and so $\mathcal{F}$ is a differentiable structure containing $\mathcal{F}_{0}$. Clearly $\mathcal{F}$ is the unique such structure.

We mention two other fundamental types of differentiable structures on locally Euclidean spaces, types that we shall not treat in this text, namely, the structure of class  $ C^{\infty} $ and the complex analytic structure. For a differentiable structure of class  $ C^{\infty} $, one requires that the compositions in (b) are locally given by convergent power series. For a complex analytic structure on a 2d-dimensional locally Euclidean space, one requires that the coordinate systems have range in complex d-space  $ C^{d} $ and overlap holomorphically.

$\hat{A}$ d-dimensional differentiable manifold of class $C^{k}$ (similarly $C^{k}$ or complex analytic) is a pair $(M,\mathcal{F})$ consisting of a $d$-dimensional, second countable, locally Euclidean space $M$ together with a differentiable structure $\mathcal{F}$ of class $C^{k}$. We shall usually denote the differentiable manifold $(M,\mathcal{F})$ simply by $M$, with the understanding that when we speak of the “differentiable manifold $M$” we are considering the locally Euclidean space $M$ with some given differentiable structure $\mathcal{F}$. Our attention will be restricted solely to the case of class $C^{k}$, so by differentiable we will always mean differentiable of class $C^{k}$. We also use the terminology smooth to indicate differentiability of class $C^{k}$. We often refer to differentiable manifolds simply as manifolds, with differentiability of class $C^{k}$ always implicitly assumed. A manifold can be viewed as a triple consisting of an underlying point set, a second countable locally Euclidean topology for this set, and a differentiable structure. If $X$ is a set, by a manifold structure on $X$ we shall mean a choice of both a second countable locally Euclidean topology for $X$ and a differentiable structure.

Even though we shall restrict our attention to the $C^\infty$ case, many of our theorems do, however, have $C^k$ versions for $k < \infty$, which are essentially no more complicated than the ones we shall obtain. They simply require that one keep track of degrees of differentiability, for differentiating a $C^k$ function may only yield a function of class $C^{k-1}$ if $1 \leq k < \infty$.

Unless we indicate otherwise, we shall always use M and N to denote differentiable manifolds, and  $ M^{d} $ will indicate that M is a manifold of dimension d.

### 1.5 Examples

(a) The standard differentiable structure on Euclidean space $\mathbb{R}^d$ is obtained by taking $\mathcal{F}$ to be the maximal collection (with respect to $1.4(b)$) containing $(\mathbb{R}^d, i)$, where $i: \mathbb{R}^d \to \mathbb{R}^d$ is the identity map.

(b) Let $V$ be a finite dimensional real vector space. Then $V$ has a natural manifold structure. Indeed, if $\{e_i\}$ is a basis of $V$, then the elements of the dual basis $\{r_i\}$ are the coordinate functions of a global coordinate system on $V$. Such a global coordinate system uniquely determines a differentiable structure $\mathcal{F}$ on $V$. This differentiable structure is independent of the choice of basis, since different bases give $C^\infty$ overlapping coordinate systems. In fact, the change of coordinates is given simply by a constant non-singular matrix.

(c) Complex $n$-space $\mathbb{C}^{n}$ is a real $2n$-dimensional vector space, and so, by Example (b), has a natural structure as a $2n$-dimensional real manifold. If $\{e_{i}\}$ is the canonical complex basis in which $e_{i}$ is the $n$-tuple consisting of zeros except for a $1$ in the $i$th spot, then

 $$ \{e_{1},\ldots,e_{n},\sqrt{-1}e_{1},\ldots,\sqrt{-1}e_{n}\} $$ 

is a real basis for $C^{n}$, and its dual basis is the canonical global coordinate system on $C^{n}$.

(d) The d-sphere is the set

 $$ S^{d}=\{a\in\mathbb{R}^{d+1}\colon\sum_{i=1}^{d+1}a_{i}^{\sharp}=1\}. $$ 

Let $n = (0, \ldots, 0, 1)$ and $s = (0, \ldots, 0, -1)$. Then the standard differentiable structure on $S^d$ is obtained by taking $\mathcal{F}$ to be the maximal collection containing $(S^d - n, p_n)$ and $(S^d - s, p_s)$, where $p_n$ and $p_s$ are stereographic projections from $n$ and $s$ respectively.

(e) An open subset $U$ of a differentiable manifold $(M,\mathcal{F}_{M})$ is itself a differentiable manifold with differentiable structure

 $$ \mathcal{F}_{U}=\{(U_{\alpha}\cap U,\varphi_{\alpha}\big|U_{\alpha}\cap U)\colon(U_{\alpha},\varphi_{\alpha})\in\mathcal{F}_{M}\}. $$ 

Unless specified otherwise, open subsets of differentiable manifolds will always be given this natural differentiable structure.

(f) The general linear group $Gl(n,\mathbb{R})$ is the set of all $n\times n$ non-singular real matrices. If we identify in the obvious way the points of $\mathbb{R}^{n^{3}}$ with $n\times n$ real matrices, then the determinant becomes a continuous function on $\mathbb{R}^{n^{3}}$. $Gl(n,\mathbb{R})$ receives a manifold structure as the open subset of $\mathbb{R}^{n^{3}}$ where the determinant function does not vanish.

(g) Product manifolds. Let $(M_{1},\mathcal{F}_{1})$ and $(M_{2},\mathcal{F}_{2})$ be differentiable manifolds of dimensions $d_{1}$ and $d_{2}$ respectively. Then $M_{1}\times M_{2}$ becomes a differentiable manifold of dimension $d_{1}+d_{2}$, with differentiable structure $\mathcal{F}$ the maximal collection containing

 $$ \{U_{\alpha}\times V_{\beta},\varphi_{\alpha}\times\psi_{\beta}\colon U_{\alpha}\times V_{\beta}\to $$ 

 $$ \mathbb{R}^{d_{1}}\times\mathbb{R}^{d_{2}})\colon(U_{\alpha},\varphi_{\alpha})\in\mathcal{F}_{1},(V_{\beta},\psi_{\beta})\in\mathcal{F}_{2}\}. $$ 

## 8 Manifolds

1.6 Definitions Let $U \subset M$ be open. We say that $f: U \to \mathbb{R}$ is a $C^\infty$ function on $U$ (denoted $f \in C^\infty(U)$) if $f \circ \varphi^{-1}$ is $C^\infty$ for each coordinate map $\varphi$ on $M$. A continuous map $\psi: M \to N$ is said to be differentiable of class $C^\infty$ (denoted $\psi \in C^\infty(M,N)$ or simply $\psi \in C^\infty$) if $g \circ \psi$ is a $C^\infty$ function on $\psi^{-1}$ (domain of $g$) for all $C^\infty$ functions $g$ defined on open sets in $N$. Equivalently, the continuous map $\psi$ is $C^\infty$ if and only if $\varphi \circ \psi \circ \tau^{-1}$ is $C^\infty$ for each coordinate map $\tau$ on $M$ and $\omega$ on $N$.

Clearly the composition of two differentiable maps is again differentiable. Observe that a mapping $\psi: M \to N$ is $C^\infty$ if and only if for each $m \in M$ there exists an open neighborhood $U$ of $m$ such that $\psi \mid U$ is $C^\infty$.

##### THE SECOND AXIOM OF COUNTABILITY

The second axiom of countability has many consequences for manifolds. Among them, manifolds are normal, metrizable, and paracompact. Paracompactness implies the existence of partitions of unity, an extremely useful tool for piecing together global functions and structures out of local ones, and conversely for representing global structures as locally finite sums of local ones. After giving the necessary definitions, we shall give a simple direct proof of paracompactness for manifolds, and shall then derive the existence of partitions of unity. It is evident that manifolds are regular topological spaces and their normality follows easily from this and the paracompactness. We shall leave the proof that manifolds are normal as an exercise. For the fact that manifolds are metrizable, see [13].

1.7 Definitions A collection $\{U_e\}$ of subsets of $M$ is a cover of a set $W \subset M$ if $W \subset \bigcup U_e$. It is an open cover if each $U_e$ is open. A subcollection of the $U_e$ which still covers is called a subcover. A refinement $\{V_\beta\}$ of the cover $\{U_e\}$ is a cover such that for each $\beta$ there is an $\alpha$ such that $V_\beta \subset U_e$. A collection $\{A_e\}$ of subsets of $M$ is locally finite if whenever $m \in M$ there exists a neighborhood $W_m$ of $m$ such that $W_m \cap A_e \neq \varnothing$ for only finitely many $\alpha$. A topological space is paracompact if every open cover has an open locally finite refinement.

1.8 Definition A partition of unity on $M$ is a collection $\{\varphi_i: i \in I\}$ of $C^\infty$ functions on $M$ such that

(a) The collection of supports {supp $\varphi_{i}$: $i \in I\}$ is locally finite.

(b)  $ \sum_{i\in I}\varphi_i(p)=1 $ for all  $ p\in M $, and  $ \varphi_i(p)\geq0 $ for all  $ p\in M $ and  $ i\in I $.

A partition of unity $\{\varphi_i: i \in I\}$ is subordinate to the cover $\{U_e: \alpha \in A\}$ if for each $i$ there exists an $\alpha$ such that $\text{supp} \varphi_i \subset U_e$. We say that it is subordinate to the cover $\{U_i: i \in I\}$ with the same index set as the partition of unity if $\text{supp} \varphi_i \subset U_i$ for each $i \in I$.

1.9 Lemma Let X be a topological space which is locally compact (each point has at least one compact neighborhood), Hausdorff, and second countable (manifolds, for example). Then X is paracompact. In fact, each open cover has a countable, locally finite refinement consisting of open sets with compact closures.

PROOF We prove first that there exists a sequence  $ \{G_{i}: i = 1, 2, \ldots\} $ of open sets such that

 $$ \begin{aligned}{\overline{{G_{i}}}}&{{}{~i s~c o m p a c t,}}\\ {\overline{{G_{i}}}}&{{}\subset G_{i+1},}\\ {X}&{{}=\bigcup_{i=1}^{\infty}G_{i}.}\\ \end{aligned} $$ 

Let $\{U_{i}: i=1,2,\ldots\}$ be a countable basis of the topology of $X$ consisting of open sets with compact closures. Such a basis can be obtained by starting with any countable basis and selecting the subcollection consisting of basic sets with compact closures. The fact that $X$ is Hausdorff and locally compact implies that this subcollection is itself a basis. Now, let $G_{1}=U_{1}$. Suppose that

 $$ G_{k}=U_{1}\cup\cdots\cup U_{j_{k}}. $$ 

Then let  $ j_{k+1} $ be the smallest positive integer greater than  $ j_{k} $ such that

 $$ \overline{{G}}_{k}\subset\bigcup_{i=1}^{j_{k+1}}U_{i}, $$ 

 $$ G_{k+1}=\bigcup_{i=1}^{j_{k+1}}U_{i}. $$ 

and define

This defines inductively a sequence  $ \{G_{k}\} $ satisfying (1).

 $$ \bigcirc_{G_{1}\atop G_{i}}\quad\cdots\quad\bigcirc_{G_{i-1}\atop G_{i-1}}\quad\vdots\quad\bigcirc_{G_{i-1}\atop G_{i}}\quad\vdots\quad\bigcirc_{G_{i+1}\atop G_{i+1}} $$ 

## 10 Manifolds

Let $\{U_n : \alpha \in A\}$ be an arbitrary open cover. The set $\overline{G_i} - G_{i-1}$ is compact and contained in the open set $G_{i+1} - \overline{G_{i-1}}$. For each $i \geq 3$ choose a finite subcover of the open cover $\{U_n \cap (G_{i+1} - \overline{G_{i-1}}): \alpha \in A\}$ of $\overline{G_i} - G_{i-1}$, and choose a finite subcover of the open cover $\{U_n \cap G_i : \alpha \in A\}$ of the compact set $\overline{G_i}$. This collection of open sets is easily seen to be a countable, locally finite refinement of the open cover $\{U_n\}$, and consists of open sets with compact closures.

1.10 Lemma There exists a non-negative $C^{\infty}$ function $\varphi$ on $\mathbb{R}^{d}$ which equals 1 on the closed cube $\overline{C(1)}$ and zero on the complement of the open cube $C(2)$.

PROOF We need only let $\varphi$ be the product

 $$ \varphi=(h\circ r_{1})\cdot\cdot\cdot(h\circ r_{d}), $$ 

where $h$ is a non-negative $C^{\infty}$ function on the real line which is 1 on $[-1,1]$ and zero outside of $(-2,2)$. To construct such an $h$, we start with the function

 $$ f(t)=\left\{\begin{aligned}{}&{{}e^{-1/t}}&{}&{{}t>0}\\ {}&{{}0}&{}&{{}t\leq0}\\ \end{aligned}\right. $$ 

which is non-negative, $C^{\infty}$, and positive for $t>0$. Then the function

 $$ g(t)=\frac{f(t)}{f(t)+f(1-t)} $$ 

is non-negative, $C^\infty$, and takes the value 1 for $t \geq 1$ and the value zero for $t \leq 0$. We obtain the desired function $h$ by setting

 $$ h(t)=g(t+2)g(2-t). $$ 

1.11 Theorem (Existence of Partitions of Unity) Let $M$ be a differentiable manifold and $\{U_a: a \in A\}$ an open cover of $M$. Then there exists a countable partition of unity $\{\varphi_i: i = 1, 2, 3, \ldots\}$ subordinate to the cover $\{U_a\}$ with $\operatorname{supp} \varphi_i$ compact for each $i$. If one does not require compact supports, then there is a partition of unity $\{\varphi_a\}$ subordinate to the cover $\{U_a\}$ (that is, $\operatorname{supp} \varphi_a \subset U_a$) with at most countably many of the $\varphi_a$ not identically zero.

PROOF Let the sequence $\{G_i\}$ cover $M$ as in 1.9(1), and set $G_0 = \varnothing$. For $p \in M$, let $i_p$ be the largest integer such that $p \in M - \overline{G_{i_p}}$. Choose an $\alpha_p$ such that $p \in U_{\alpha_p}$, and let $(V, \tau)$ be a coordinate system centered at $p$ such that $V \subset U_{\alpha_p} \cap (G_{i_p+2} - \overline{G_{i_p}})$ and such that $\tau(V)$ contains the closed cube $\overline{C(2)}$. Define

 $$ \psi_{o}=\left\{\begin{aligned}{}&{{}\varphi^{\circ}\tau}&{\quad\mathrm{o n~}V}\\ {}&{{}0}&{\quad\mathrm{e l s e w h e r e}}\\ \end{aligned}\right. $$ 

where $\varphi$ is the function $1.10(1)$. Then $\psi_s$ is a $C^\infty$ function on $M$ which has the value 1 on some open neighborhood $W_s$ of $p$, and has compact support lying in $V \subset U_{s_p} \cap (G_{t_p+1} - \overline{G}_{t_p})$. For each $i \geq 1$, choose a finite set of points $p$ in $M$ whose corresponding $W_s$ neighborhoods cover $\overline{G}_t - G_{t-1}$. Order the corresponding $\psi_s$ functions in a sequence $\psi_j, j=1,2,3,\ldots$. The supports of the $\psi_j$ form a locally finite family of subsets of $M$. Thus the function

 $$ \psi=\sum_{j=1}^{\infty}\psi_{j} $$ 

is a well-defined $C^{\infty}$ function on $M$, and moreover $\psi(p) > 0$ for each $p \in M$. For each $i = 1, 2, 3, \ldots$ define

 $$ \varphi_{i}=\frac{\psi_{i}}{\psi_{-}}. $$ 

Then the functions $\{\varphi_i: i=1,2,3,\ldots\}$ form a partition of unity subordinate to the cover $\{U_a\}$ with $\operatorname{supp} \varphi_i$ compact for each $i$. If we let $\varphi_a$ be identically zero if no $\varphi_i$ has support in $U_a$, and otherwise let $\varphi_a$ be the sum of the $\varphi_i$ with support in $U_a$, then $\{\varphi_a\}$ is a partition of unity subordinate to the cover $\{U_a\}$ with at most countably many of the $\varphi_a$ not identically zero. To see that the support of $\varphi_a$ lies in $U_a$, observe that if $\mathcal{A}$ is a locally finite family of closed sets, then $\overline{\mathbf{U}A} = \bigcup_{A\in\mathcal{A}} A$.

Observe, however, that the support of $\varphi_{a}$ is not necessarily compact.

Corollary Let $G$ be open in $M$, and let $A$ be closed in $M$, with $A \subset G$. Then there exists a $C^{\infty}$ function $\varphi: M \to \mathbb{R}$ such that

(a)  $ 0 \leq \varphi(p) \leq 1 $ for all  $ p \in M $.

(b)  $ \varphi(p) = 1 $ if  $ p \in A $.

(c) supp  $ \varphi \subset G $.

PROOF There is a partition of unity $\{\varphi, \psi\}$ subordinate to the cover $\{G, M - A\}$ of $M$ with $\operatorname{supp} \varphi \subset G$ and $\operatorname{supp} \psi \subset M - A$. Then $\varphi$ is the desired function.

#### TANGENT VECTORS AND DIFFERENTIALS

1.12 A vector $v$ with components $v_{1}, \ldots, v_{d}$ at a point $p$ in Euclidean space $\mathbb{R}^{d}$ can be thought of as an operator on differentiable functions. Specifically, if $f$ is differentiable on a neighborhood of $p$, then $v$ assigns to $f$ the real number $v(f)$ which is the directional derivative of $f$ in the direction $v$ at $p$. That is,

 $$ v(f)=v_{1}\frac{\partial f}{\partial r_{1}}\bigg|_{p}+\cdots+v_{d}\frac{\partial f}{\partial r_{d}}\bigg|_{p}. $$ 

This operation of the vector v on differentiable functions satisfies two important properties.

 $$ \begin{aligned}{v(f+\lambda g)}&{{}=v(f)+\lambda v(g);}\\ {v(f\cdot g)}&{{}=f(p)v(g)+g(p)v(f),}\\ \end{aligned} $$ 

whenever $f$ and $g$ are differentiable near $p$, and $\lambda$ is a real number. The first property says that $v$ acts linearly on functions, and the second says that $v$ is a derivation. This motivates our definition of tangent vectors on manifolds. They will be directional derivatives, that is, linear derivations on functions. The operation of taking derivatives depends only on local properties of functions, properties in arbitrarily small neighborhoods of the point at which the derivative is being taken. In order to express most conveniently this dependence of the derivative on the local nature of functions, we introduce the notion of germs of functions.

1.13 Definitions Let $m \in M$. Functions $f$ and $g$ defined on open sets containing $m$ are said to have the same germ at $m$ if they agree on some neighborhood of $m$. This introduces an equivalence relation on the $C^\infty$ functions defined on neighborhoods of $m$, two functions being equivalent if and only if they have the same germ. The equivalence classes are called $germs$, and we denote the set of germs at $m$ by $F_m$. If $f$ is a $C^\infty$ function on a neighborhood of $m$, then $f$ will denote its germ. The operations of addition, scalar multiplication, and multiplication of functions induce on $F_m$ the structure of an algebra over $\mathbb{R}$. A germ $f$ has a well-defined value $f(m)$ at $m$, namely, the value at $m$ of any representative of the germ. Let $F_m \subset F_m$ be the set of germs which vanish at $m$. Then $F_m$ is an ideal in $F_m$, and we let $F_m^k$ denote its $k$th power. $F_m^k$ is the ideal of $F_m$ consisting of all finite linear combinations of $k$-fold products of elements of $F_m$. These form a descending sequence of ideals $F_m \supset F_m \supset F_m^k \supset F_m^k \supset \cdots$.

1.14 Definition A tangent vector  $ v $ at the point  $ m \in M $ is a linear derivation of the algebra  $ \widetilde{F}_m $. That is, for all  $ \mathbf{f} $,  $ \mathbf{g} \in \widetilde{F}_m $ and  $ \lambda \in \mathbb{R} $,

 $$ \begin{array}{r l}{\mathrm{(a)}}&{v(\mathbf{f}+\lambda\mathbf{g})=v(\mathbf{f})+\lambda v(\mathbf{g}).}\end{array} $$ 

 $$ v(\mathbf{f}\cdot\mathbf{g})=\mathbf{f}(m)v(\mathbf{g})+\mathbf{g}(m)v(\mathbf{f}). $$ 

 $ M_m $ denotes the set of tangent vectors to  $ M $ at  $ m $ and is called the tangent space to  $ M $ at  $ m $. Observe that if we define  $ (v + w)(f) $ and  $ (\lambda v)(f) $ by

 $$ \begin{aligned}(v+w)(\mathbf{f})&=v(\mathbf{f})+w(\mathbf{f})\ $ \lambda v)(\mathbf{f})&=\lambda(v(\mathbf{f}))\end{aligned} $$ 

whenever $v, w \in M_m$ and $\lambda \in \mathbb{R}$, then $v + w$ and $\lambda v$ again are tangent vectors at $m$. So in this way $M_m$ becomes a real vector space. The fundamental property of the vector space $M_m$, which we shall establish in 1.17, is that its dimension equals the dimension of $M$. This definition of tangent vector

is not suitable in the $C^{k}$ case for $1 \leq k < \infty$. (We will discuss the $C^{k}$ case further in 1.21.) We give this definition of tangent vector for several reasons. One reason is that it is intrinsic; that is, it does not depend on coordinate systems. Another reason is that it generalizes naturally to higher order tangent vectors, as we shall see in 1.26.

1.15 If $c$ is the germ of a function with the constant value $c$ on a neighborhood of $m$, and if $v$ is a tangent vector at $m$, then $v(c) = 0$, for

 $$ v(\mathbf{c})=c v(\mathbf{1}), $$ 

and

1.16 Lemma  $ M_{m} $ is naturally isomorphic with  $ (F_{m}/F_{m}^{2})^{*} $. (The symbol  $ {}^{*} $ denotes dual vector space.)

 $$ v(\mathbf{1})=v(\mathbf{1}\cdot\mathbf{1})=1v(\mathbf{1})+1v(\mathbf{1})=2v(\mathbf{1}). $$ 

PROOF If $v \in M_m$, then $v$ is a linear function on $F_m$ vanishing on $F_m^2$ because of the derivation property. Conversely, if $\ell \in (F_m/F_m^2)^*$, we define a tangent vector $v_\ell$ at $m$ by setting $v_\ell(\mathbf{f}) = \ell(\{\mathbf{f} - \mathbf{f}(\mathbf{m})\})$ for $\mathbf{f} \in \widetilde{F}_m$. (Here $\mathbf{f}(\mathbf{m})$ denotes the germ of the function with the constant value $\mathbf{f}(m)$, and-) is used to denote cosets in $F_m/F_m^2$.) Linearity of $v_\ell$ on $\widetilde{F}_m$ is clear. It is a derivation since

 $$ \begin{aligned}{v_{\ell}(\mathbf{f}\cdot\mathbf{g})}&{{}=\ell\big(\{\mathbf{f}\cdot\mathbf{g}-\mathbf{f}(\mathbf{m})\mathbf{g}(\mathbf{m})\}\big)}\\ {}&{{}=\ell\big(\{(\mathbf{f}-\mathbf{f}(\mathbf{m}))(\mathbf{g}-\mathbf{g}(\mathbf{m}))+\mathbf{f}(\mathbf{m})\big(\mathbf{g}-\mathbf{g}(\mathbf{m})\big)}\\ {}&{{}\quad+\big(\mathbf{f}-\mathbf{f}(\mathbf{m})\big)\mathbf{g}(\mathbf{m})\}\big)}\\ {}&{{}=\ell\big(\{(\mathbf{f}-\mathbf{f}(\mathbf{m}))(\mathbf{g}-\mathbf{g}(\mathbf{m}))\}\big)+\mathbf{f}(m)\ell\big(\{\mathbf{g}-\mathbf{g}(\mathbf{m})\}\big)}\\ {}&{{}\quad+\mathbf{g}(m)\ell\big(\{\mathbf{f}-\mathbf{f}(\mathbf{m})\}\big)}\\ {}&{{}=\mathbf{f}(m)v_{\ell}(\mathbf{g})+\mathbf{g}(m)v_{\ell}(\mathbf{f}).}\\ \end{aligned} $$ 

Thus we obtain mappings of $M_{m}$ into $(F_{m}/F_{m}^{2})^{*}$, and vice versa. It is easily checked that these are inverses of each other and thus are iso morphisms.

### 1.17 Theorem  $ \dim\left(F_{m}/F_{m}^{2}\right)=\dim M. $

The proof is based on the following calculus lemma [31].

Lemma If $g$ is of class $C^k$ ($k \geq 2$) on a convex open set $U$ about $p$ in $\mathbb{R}^d$, then for each $q \in U$,

 $$ \begin{aligned}{\mathbf{g}(q)}&{{}=\mathbf{g}(p)+\sum_{i=1}^{d}\frac{\partial g}{\partial r_{i}}\bigg|_{p}\big(r_{i}(q)-r_{i}(p)\big)\quad.}\\ {}&{{}\quad+\sum_{i,j}\big(r_{i}(q)-r_{i}(p)\big)\big(r_{j}(q)-r_{j}(p)\big)\int_{0}^{1}(1-t)\frac{\partial^{2}g}{\partial r_{i}\partial r_{j}}\bigg|_{(p+t(q-p))}d t.}\\ \end{aligned} $$ 

In particular, if $g \in C^{\infty}$, then the second summation in (1) determines an element of $F_{p}^{2}$ since the integral as a function of $q$ is of class $C^{\infty}$.

## 14 Manifolds

PROOF OF 1.17 Let $(U,\varphi)$ be a coordinate system about $m$ with coordinate functions $x_1,\ldots,x_d$ ($d=\dim M$). Let $f\in F_m$. Apply (1) to $f\circ\varphi^{-1}$, and compose with $\varphi$ to obtain

 $$ f=\sum_{i=1}^{d}\frac{\partial(f\circ\varphi^{-1})}{\partial r_{i}}\bigg|_{\varphi(m)}(x_{i}-x_{i}(m))+\sum_{i,j}(x_{i}-x_{i}(m))(x_{j}-x_{j}(m)) $$ 

on a neighborhood of $m$, where $h \in C^{\infty}$. Thus

 $$ \mathbf{f}=\sum_{i=1}^{d}\frac{\partial(f\circ\varphi^{-1})}{\partial r_{i}}\bigg|_{\varphi(m)}\left(\mathbf{x}_{i}-\mathbf{x}_{i}(\mathbf{m})\right)\bmod F_{m}{}^{3}. $$ 

Hence $\{\{\mathbf{x}_{i}-\mathbf{x}_{i}(\mathbf{m})\}: i=1,\ldots,d\}$ spans $F_{m}/F_{m}^{2}$. Consequently $\dim F_{m}/F_{m}^{2}\leq d$. We claim that these elements are linearly independent. For suppose that

 $$ \sum_{i=1}^{d}a_{i}(\mathbf{x}_{i}-\mathbf{x}_{i}(\mathbf{m}))\in F_{\mathrm{m}}^{\mathrm{s}}. $$ 

Now,

 $$ \sum_{i=1}^{d}a_{i}\big(x_{i}-x_{i}(m)\big)\circ\varphi^{-1}=\sum_{i=1}^{d}a_{i}\big(r_{i}-r_{i}\big(\varphi(m)\big)\big). $$ 

Thus

 $$ \sum_{i=1}^{d}a_{i}\big(\mathbf{r}_{i}-\mathbf{r}_{i}\big(\mathbf{\varphi}(\mathbf{m})\big)\big)\in F_{\varphi(\mathbf{m})}^{2}\;. $$ 

But this implies that

 $$ \frac{\partial}{\partial r_{j}}\bigg|_{\substack{\varphi(m)}}\big(\textstyle\sum a_{i}\big(r_{i}-r_{i}\big(\varphi(m)\big)\big)\big)=0 $$ 

for $j=1,\ldots,d$, which implies that the $a_{i}$ must all be zero.

Corollary dim  $ M_{m} = \dim M $.

1.18 In practice we will treat tangent vectors as operating on functions rather than on their germs. If $f$ is a differentiable function defined on a neighborhood of $m$, and $v \in M_{m}$, we define

 $$ v(f)=v(\mathbf{f}). $$ 

Thus  $ v(f) = v(g) $ whenever f and g agree on a neighborhood of m, and clearly

 $$ \begin{aligned}{v(f+\lambda g)}&{{}=v(f)+\lambda v(g)\qquad(\lambda\in\mathbb{R}),}\\ {v(f\cdot g)}&{{}=f(m)v(g)+g(m)v(f),}\\ \end{aligned} $$ 

where  $ f + \lambda g $ and  $ f \cdot g $ are defined on the intersection of the domains of definition of f and g.

1.19 Definition Let $(U,\varphi)$ be a coordinate system with coordinate functions $x_{1},\ldots,x_{d}$, and let $m\in U$. For each $i\in(1,\ldots,d)$, we define

a tangent vector  $ (\partial/\partial x_i)|_{m} \in M_m $ by setting

 $$ \left(\frac{\partial}{\partial x_{i}}\bigg\vert_{m}\right)(f)=\frac{\partial(f\circ\varphi^{-1})}{\partial r_{i}}\bigg\vert_{\varphi(m)} $$ 

for each function $f$ which is $C^{\infty}$ on a neighborhood of $m$. We interpret (1) as the directional derivative of $f$ at $m$ in the $x_{i}$ coordinate direction. We also use the notation

 $$ \left.\frac{\partial f}{\partial x_{i}}\right|_{m}=\left(\left.\frac{\partial}{\partial x_{i}}\right|_{m}\right)(f). $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//61098b9b-10c0-4344-90c8-5e3f1bbc25cf/markdown_2/imgs/img_in_image_box_142_360_796_574.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A11Z%2F-1%2F%2F9024c648ef5b6611bdef4261ff784ff6d9056566eceed51c4c756d4dbc403aaa" alt="Image" width="68%" /></div>


### 1.20 Remarks on 1.19

(a) Clearly  $  ((\partial/\partial x_i)_m)(f)  $ depends only on the germ of  $  f  $ at  $  m  $, and (a) and (b) of 1.14 are satisfied; so  $  (\partial/\partial x_i)_m  $ is a tangent vector at  $  m  $. Moreover,  $  \{(\partial/\partial x_i)_m : i = 1, \ldots, d\}  $ is a basis of  $  M_m  $. Indeed, it is the basis of  $  M_m  $ dual to the basis  $  \{(\mathbf{x}_i - \mathbf{x}_1(\mathbf{m})) : i = 1, \ldots, d\}  $ of  $  F_m/F_m^2  $ since

 $$ \frac{\partial}{\partial x_{i}}\bigg|_{m}(x_{j}-x_{j}(m))=\delta_{ij}. $$ 

(b) If  $ v \in M_{m} $, then

 $$ v=\sum_{i=1}^{d}v(x_{i})\left.\frac{\partial}{\partial x_{i}}\right|_{\infty}. $$ 

Simply check that both sides give the same results when applied to the functions $(x_{j}-x_{j}(m))$.

(c) Suppose that $(U,\varphi)$ and $(V,\psi)$ are coordinate systems about $m$, with coordinate functions $x_{1},\ldots,x_{d}$ and $y_{1},\ldots,y_{d}$ respectively. Then it follows from remark (b) that

 $$ \frac{\partial}{\partial y_{j}}\Big|_{m}=\sum_{i=1}^{d}\frac{\partial x_{i}}{\partial y_{j}}\Big|_{m}\frac{\partial}{\partial x_{i}}\Big|_{m}. $$ 

Observe that $(\partial/\partial x_{i})$ depends on $\varphi$ and not only on $x_{i}$. In particular, if $x_{1}$ were equal to $y_{1}$, it would not necessarily follow that $\partial/\partial x_{1}$ equals $\partial/\partial y_{1}$.

## 16 Manifolds

(d) If we apply Definition 1.19 to the canonical coordinate system  $ r_{1}, \ldots, r_{d} $ on  $ R^{d} $, then the tangent vectors which we obtain are none other than the ordinary partial derivative operators  $ (\partial/\partial r_{i}) $.

1.21 Our proof of the finite dimensionality of  $ F_m/F_m^3 $ certainly fails in the  $ C^k $ case for  $ k < \infty $ since the remainder term in the lemma of 1.17 will not be a sum of products of  $ C^k $ functions, and the lemma doesn't even make sense in the  $ C^1 $ case. In fact, it turns out (see [21]) that  $ F_m/F_m^3 $ is always infinite dimensional in the  $ C^k $ case for  $ 1 \leq k < \infty $. There are various ways to define tangent vectors in the  $ C^k $ case in order that  $ \dim M_m = \dim M $ (all of which work in the  $ C^\infty $ case, too). One way is to define a tangent vector v at m as a mapping which assigns to each function (defined and differentiable of class  $ C^k $ on a neighborhood of m) a real number  $ v(f) $ such that if  $ (U, \varphi) $ is a coordinate system on a neighborhood of m, then there exists a list of real numbers  $ (a_1, \ldots, a_d) $ (depending on  $ \varphi $) such that

 $$ v(f)=\sum_{i=1}^{d}a_{i}\frac{\partial(f\circ\varphi^{-1})}{\partial r_{i}}\bigg|_{\varphi(m)}. $$ 

Then the space  $ M_m $ of tangent vectors again turns out to be finite dimensional, with a basis  $ \{(\partial/\partial x_i)\big|_{m}\} $.

1.22 The Differential Let  $ \psi: M \to N $ be  $ C^\infty $, and let  $ m \in M $. The differential of  $ \psi $ at  $ m $ is the linear map

 $$ d\psi\colon M_{m}\to N_{\psi(m)} $$ 

defined as follows. If $v\in M_{m}$, then $d\psi(v)$ is to be a tangent vector at $\psi(m)$, so we describe how it operates on functions. Let $g$ be a $C^{\infty}$ function on a neighborhood of $\psi(m)$. Define $d\psi(v)(g)$ by setting

 $$ d\psi(v)(g)=v(g\circ\psi). $$ 

It is easily checked that $d\psi$ is a linear map of $M_{m}$ into $N_{\psi(m)}$. Strictly speaking, this map should be denoted $d\psi\mid M_{m}$, or simply $d\psi_{m}$. However, we omit the subscript $m$ when there is no possibility of confusion. The map $\psi$ is called non-singular at $m$ if $d\psi_{m}$ is non-singular, that is, if the kernel of (1) consists of 0 alone. The dual map

 $$ (i.e.,(i n j.) $$ 

 $$ \delta\psi\colon N_{\psi(m)}^{*}\to M_{m}^{*} $$ 

is defined as usual by requiring that

 $$ \delta\psi(\omega)(v)=\omega\bigl(d\psi(v)\bigr) $$ 

whenever $\omega \in N_{v(m)}^{*}$ and $v \in M_{m}$. In the special case of a $C^{\infty}$ function $f: M \to \mathbb{R}$, if $v \in M_{m}$ and $f(m) = r_{0}$, then

 $$ d f(v)=v(f)\frac{d}{d r}\bigg|_{r_{0}}. $$ 

In this case, we usually take $df$ to mean the element of $M_{m}^{*}$ defined by

 $$ d f(v)=v(f). $$ 

That is, we identify $df$ with $\delta f(\omega)$, where $\omega$ is the basis of the 1-dimensional space $\mathbb{R}_{r_{0}}^{*}$ dual to $(d/dr)|_{r_{0}}$. Particular usage will be clear from the context.

### 1.23 Remarks on 1.22

(a) Let $(U, x_{1}, \ldots, x_{d})$ and $(V, y_{1}, \ldots, y_{t})$ be coordinate systems about $m$ and $\psi(m)$ respectively. Then it follows from 1.22(2) and 1.20(b) that

 $$ d\psi\left(\frac{\partial}{\partial x_{j}}\bigg|_{m}\right)=\sum_{i=1}^{\ell}\frac{\partial(y_{i}\circ\psi)}{\partial x_{j}}\bigg|_{m}\frac{\partial}{\partial y_{i}}\bigg|_{w(m)}. $$ 

The matrix $\{\partial(y_{i}\circ\psi)/\partial x_{i}\}$ is called the Jacobian of the map $\psi$ (with respect to the given coordinate system). For maps between Euclidean spaces, the Jacobian will always be taken with respect to the canonical coordinate systems.

(b) If $(U, x_1, \ldots, x_d)$ is a coordinate system on $M$, and $m \in U$, then $\{dx_i\}_{m}$ is the basis of $M_m^*$ dual to $\{\partial/\partial x_i\}_{m}\}$. If $f: M \to \mathbb{R}$ is a $C^\infty$ function, then

 $$ \begin{array}{r}{d f_{m}=\left.\sum_{i=1}^{d}\frac{\partial f}{\partial x_{i}}\right|_{m}d x_{i}|_{m}.}\end{array} $$ 

(c) Chain Rule. Let  $ \psi $:  $ M \to N $ and  $ \varphi $:  $ N \to X $ be  $ C^\infty $ maps. Then

 $$ d(\varphi\circ\psi)_{m}=d\varphi_{\psi(m)}\circ d\psi_{m}, $$ 

or simply $d(\varphi\circ\psi)=d\varphi\circ d\psi$. It is a useful exercise to check the form that this equation takes when the maps are expressed in terms of the matrices obtained by choosing coordinate systems.

(d) If $\psi: M \to N$ and $f: N \to \mathbb{R}$ are $C^\infty$, then $\delta\psi(df_{\psi(m)}) = d(f \circ \psi)_m$, for $\delta\psi(df_{\psi(m)})(v) = df(d\psi(v)) = d(f \circ \psi)_m(v)$ whenever $v \in M_m$.

(e) A $C^{\infty}$ mapping $\sigma: (a,b)\to M$ is called a smooth curve in $M$. Let $t\in(a,b)$. Then the tangent vector to the curve $\sigma$ at $t$ is the vector

 $$ d\sigma\left(\frac{d}{d r}\bigg|_{t}\right)\in M_{\sigma(t)}. $$ 

We shall denote the tangent vector to  $ \sigma $ at t by  $ \dot{\sigma}(t) $.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//775e6ebd-0f3f-4c72-ab2c-f2200f28e540/markdown_0/imgs/img_in_image_box_193_1012_798_1161.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A11Z%2F-1%2F%2Fcacfbdfb3f45300d8f1ba8658cf9d428a052ed89e64a9742b590ac1fd09df306" alt="Image" width="63%" /></div>


Now, if $v$ is any element of $M_{m}$, then $v$ is the tangent vector to a smooth curve in $M$. For one can simply choose a coordinate system $(U,\varphi)$, centered at $m$, for which

 $$ v=d\varphi\left(\frac{\partial}{\partial r_{1}}\bigg|_{0}\right). $$ 

Then $v$ is the tangent vector at 0 to the curve $t \mapsto \varphi^{-1}(t, 0, \ldots, 0)$. One should observe that many curves can have the same tangent vector, and that two smooth curves $\sigma$ and $\tau$ in $M$ for which $\sigma(t_{0}) = \tau(t_{0}) = m$ have the same tangent vector at $t_{0}$ if and only if

 $$ \frac{d(f\circ\sigma)}{d r}\Big|_{t_{0}}=\frac{d(f\circ\tau)}{d r}\Big|_{t_{0}} $$ 

for all functions $f$ which are $C^{\infty}$ on a neighborhood of $m$.

If $\sigma$ happens to be a curve in the Euclidean space $\mathbb{R}^{*}$, then

 $$ \dot{\sigma}(t)=\frac{d\sigma_{1}}{d r}\bigg|_{t}\frac{\partial}{\partial r_{1}}\bigg|_{\sigma(t)}+\cdots+\frac{d\sigma_{n}}{d r}\bigg|_{t}\frac{\partial}{\partial r_{n}}\bigg|_{\sigma(t)}. $$ 

If we identify this tangent vector with the element

 $$ \left(\frac{d\sigma_{1}}{d r}\bigg|_{t},\ldots,\frac{d\sigma_{n}}{d r}\bigg|_{t}\right) $$ 

of  $ R^{*} $, then we have

 $$ \dot{\sigma}(t)=\lim_{h\to0}\frac{\sigma(t+h)-\sigma(t)}{h}. $$ 

Thus with this identification our notion of tangent vector coincides, in this special case, with the geometric notion of a tangent to a curve in Euclidean space.

1.24 Theorem Let $\psi$ be a $C^\infty$ mapping of the connected manifold $M$ into the manifold $N$. Suppose that for each $m \in M$, $d\psi_m \equiv 0$. Then $\psi$ is a constant map.

PROOF Let $n\in\psi(M)$. $\psi^{-1}(n)$ is closed. We need only show that it is open. For this, let $m\in\psi^{-1}(n)$. Choose coordinate systems $(U,x_{1},\ldots,x_{d})$ and $(V,y_{1},\ldots,y_{c})$ about $m$ and $n$ respectively, so that $\psi(U)\subset V$. Then on $U$,

 $$ 0=d\psi\left(\frac{\partial}{\partial x_{j}}\right)=\sum_{i=1}^{c}\frac{\partial(y_{i}\circ\psi)}{\partial x_{j}}\frac{\partial}{\partial y_{i}}\qquad(j=1,\ldots,d), $$ 

which implies that

 $$ \frac{\partial(y_{i}\circ\psi)}{\partial x_{j}}\equiv0\qquad(i=1,\ldots,c;j=1,\ldots,d). $$ 

Thus the functions $y_{t}\circ\psi$ are constant on $U$. This implies that $\psi(U)=n$; hence $\psi^{-1}(n)$ is open and consequently $\psi^{-1}(n)=M$.

We shall now see that in a natural way the collection of all tangent vectors to a differentiable manifold itself forms a differentiable manifold called the tangent bundle. We have a similar dual object called the cotangent bundle formed from the linear functionals on the tangent spaces.

1.25 Tangent and Cotangent Bundles Let M be a $C^{\infty}$ manifold with differentiable structure $\mathcal{F}$. Let

 $$ \begin{aligned}{T(M)=\bigcup_{m\in\mathcal{M}}M_{m},}\\ {T^{*}(M)=\bigcup_{m\in\mathcal{M}}M_{m}^{*}.}\\ \end{aligned} $$ 

There are natural projections:

 $$ \begin{aligned}{\pi\colon T(M)\to M,\qquad}&{{}\pi(v)=m\quad\mathrm{i f}\quad v\in M_{m},}\\ {\pi^{*}\colon T^{*}(M)\to M,\qquad}&{{}\pi^{*}(\tau)=m\quad\mathrm{i f}\quad\tau\in M_{m}^{*}.}\\ \end{aligned} $$ 

Let $(U,\varphi)\in\mathcal{F}$ with coordinate functions $x_1,\ldots,x_d$. Define $\tilde{\varphi}\colon\pi^{-1}(U)\to\mathbb{R}^{2d}$ and $\tilde{\varphi}^*colon(U)\to\mathbb{R}^{2d}$ by

 $$ \tilde{\varphi}(v)=\big(x_{1}\big(\pi(v)\big),\ldots,x_{d}\big(\pi(v)\big),d x_{1}(v),\ldots,d x_{d}(v)\big) $$ 

 $$ \tilde{\varphi}^{*}(\tau)=\Bigl(x_{1}\bigl(\pi^{*}(\tau)\bigr),\ldots,x_{d}\bigl(\pi^{*}(\tau)\bigr),\tau\Bigl(\frac{\partial}{\partial x_{1}}\Bigr),\ldots,\tau\Bigl(\frac{\partial}{\partial x_{d}}\Bigr)\Bigr) $$ 

for all $v\in\pi^{-1}(U)$ and $\tau\in(\pi^{*})^{-1}(U)$. Note that $\widetilde{\varphi}$ and $\widetilde{\varphi}^*$ are both one-to-one maps onto open subsets of $\mathbb{R}^{2d}$. The following steps outline the construction of a topology and a differentiable structure on $T(M)$. The construction for $T^*(M)$ goes similarly. The proofs are left as exercises.

(a) If  $ (U,\varphi) $ and  $ (V,\varphi)\in\mathcal{F} $, then  $ \tilde{\psi}\circ\tilde{\varphi}^{-1} $ is  $ C^{\infty} $.

(b) The collection $\{\tilde{\varphi}^{-1}(W)\colon W \text{ open in } \mathbb{R}^{2d}, (U,\varphi) \in \mathcal{F}\}$ forms a basis for a topology on $T(M)$ which makes $T(M)$ into a $2d$-dimensional, second countable, locally Euclidean space.

(c) Let $\mathcal{F}$ be the maximal collection, with respect to 1.4(b), containing

 $$ \{(\pi^{-1}(U),\widetilde{\varphi})\colon(U,\varphi)\in\mathcal{F}\}. $$ 

Then $\mathcal{F}$ is a differentiable structure on $T(M)$.

$T(M)$ and $T^{*}(M)$ with these differentiable structures are called respectively the tangent bundle and the cotangent bundle. It will sometimes be convenient to write the points of $T(M)$ as pairs $(m,v)$ where $m\in M$ and $v\in M_{m}$ (and similarly for $T^{*}(M)$).

## 20 Mantfolds

If $\psi: M \to N$ is a $C^{\infty}$ map, then the differential of $\psi$ defines a mapping of the tangent bundles

 $$ d\psi\colon T(M)\to T(N), $$ 

where  $ d\psi(m,v) = d\psi_{m}(v) $ whenever  $ v \in M_{m} $. It is easily checked that (4) is a  $ C^{\infty} $ map.

1.26† Higher Order Tangent Vectors and Differentials It is useful to look at $M_{m}$ as $(F_{m}/F_{m}^{2})^{*}$, for this point of view allows an immediate generalization to higher order tangent vectors. We digress for a moment to give these definitions.

Recall that  $ \tilde{F}_{m} $ is the algebra of germs of functions at m.  $ \tilde{F}_{m} \subset \tilde{F}_{m} $ is the ideal of germs vanishing at m, and  $ \tilde{F}_{m}^{k} $ (k an integer  $ \geq 1 $) is the ideal of  $ \tilde{F}_{m} $ consisting of all finite linear combinations of k-fold products of elements of  $ \tilde{F}_{m} $.

The vector space $F_m/F_m^{\kappa+1}$ is called the space of $k$th order differentials at $m$, and we denote it by $^k M_m$. As before, $f$ denotes the germ of $f$ at $m$, and {} will denote cosets in $F_m/F_m^{\kappa+1}$. Let $f$ be a differentiable function on a neighborhood of $m$. We define the $k$th order differential $d^k f$ of $f$ at $m$ by

 $$ d^{k}f=\{\mathbf{f}-\mathbf{f}(\mathbf{m})\}. $$ 

A kth order tangent vector at m is a real linear function on  $ F_{m} $ vanishing on  $ F_{m}^{k+1} $ and vanishing also on the set of germs of functions constant on a neighborhood of m. The real linear space of kth order tangent vectors at m will be denoted by  $ M_{m}^{k} $. We have a natural identification of  $ M_{m}^{k} $ with  $ (kM_{m})^{*} $ since any kth order tangent vector restricted to  $ F_{m} $ yields a linear function on  $ F_{m} $ vanishing on  $ F_{m}^{k+1} $, and hence yields an element of  $ (kM_{m})^{*} $; and conversely an element of  $ (kM_{m})^{*} $ uniquely determines a linear function on  $ F_{m} $ vanishing on  $ F_{m}^{k+1} $, and this extends uniquely to a kth order tangent vector by requiring it to annihilate germs of constant functions.

We can tie up this notion of higher order tangent vector with the usual notion of higher order derivative in Euclidean space by looking at the forms that these tangent vectors and differentials take in a coordinate system. Let  $ (U,\varphi) $ be a coordinate system about  $ m $ with coordinate functions  $ x_1, \ldots, x_d $ such that  $ \varphi(U) $ is a convex open set in Euclidean space  $ \mathbb{R}^d $. Let  $ \alpha = (\alpha_1, \ldots, \alpha_d) $ be a list of non-negative integers. In addition to our conventions of 1.1, we let

 $$ (x-x(m))^{\alpha}=(x_{1}-x_{1}(m))^{\alpha_{1}}\cdots(x_{d}-x_{d}(m))^{\alpha_{d}}. $$ 

Let f be a  $ C^{\infty} $ function on U. Then it follows from the lemma of 1.17, that

 $$ f=f(m)+\sum_{\{\alpha\}=1}^{k}a_{\alpha}(x-x(m))^{\alpha}+\sum_{\{\alpha\}=k+1}h_{\alpha}(x-x(m))^{\alpha}, $$ 

The material of this section will not be used elsewhere in the book, and so it may be skipped without loss of continuity.

where the $h_{\alpha}$ are $C^{\infty}$ functions on $U$ and where

 $$ a_{\alpha}=\frac{1}{\alpha!}\frac{\partial^{\alpha}(f\circ\varphi^{-1})}{\partial r^{\alpha}}\bigg|_{\varphi(m)}. $$ 

Hence

 $$ d^{k}f=\sum_{1\leq[\alpha]\leq k}a_{\alpha}\{\left(\mathbf{x}-\mathbf{x}(\mathbf{m})\right)^{\alpha}\}. $$ 

Thus the collection

 $$ [\{(x-\mathbf{x}(\mathbf{m}))^{a}\}\colon1\leq[\alpha]\leq k] $$ 

spans  $ ^{k}M_{m} $. The proof that these elements are linearly independent in  $ ^{k}M_{m} $ is the obvious generalization of the proof for the case k = 2 which was treated in 1.17. Thus the collection (5) forms a basis of  $ ^{k}M_{m} $. Consequently  $ ^{k}M_{m} $ is finite dimensional with dimension equal to the binomial coefficient  $ \sum_{j=1}^{k}\binom{d+j-1}{j} $. As the dual space of  $ ^{k}M_{m} $,  $ M_{m}^{k} $ is also finite dimensional with the same dimension. Since  $ M_{m}^{k} $ is identified with  $ (^{k}M_{m})^{*} $, and these spaces are finite dimensional, we have a canonical isomorphism of  $ ^{k}M_{m} $ with  $ (M_{m}^{k})^{*} $, under which the element of  $ d^{k}f \in ^{k}M_{m} $, considered as an element of  $ (M_{m}^{k})^{*} $, satisfies

 $$ d^{k}f(v)=v(\mathbf{f}). $$ 

Let

 $$ \frac{\partial^{\alpha}f}{\partial x^{\alpha}}\bigg|_{m}=\frac{\partial^{\alpha}(f\circ\varphi^{-1})}{\partial r^{\alpha}}\bigg|_{\varphi(m)}. $$ 

Since the derivative is linear, and since the value of $\partial^a f/\partial x^a$ at $m$ depends only on the germ of $f$ at $m$ and vanishes if $f$ is constant on a neighborhood of $m$ or if $f$ is an $[\alpha]+1$-fold product of functions which vanish at $m$, then $(\partial^a/\partial x^a)\big|_m$ is an $[\alpha]$th order tangent vector at $m$. It follows that

 $$ \left\{\left(\frac{1}{\alpha!}\right)\frac{\partial^{\alpha}}{\partial x^{\alpha}}\bigg|_{m}:1\leq[\alpha]\leq k\right\} $$ 

is the basis of $M_{m}^{k}$ dual to the basis (5) of $^{k}M_{m}$. If $v$ is a $k$th order tangent vector at $m$, then

 $$ v=\sum_{[a]=1}^{k}b_{a}\frac{\partial^{a}}{\partial x^{a}}\bigg|_{m}, $$ 

where

 $$ b_{\alpha}=\left(\frac{1}{\alpha!}\right)v(({\bf x}-{\bf x}({\bf m}))^{\alpha}). $$ 

In terms of the basis (8), equation (3) becomes

 $$ a_{a}=\frac{1}{\alpha!}\frac{\partial^{a}f}{\partial x^{\alpha}}\bigg|_{m}. $$ 

## 22 Manifolds

As in the case of first order tangent vectors, we customarily think of tangent vectors as operating on the functions themselves rather than their germs; indeed, we define

 $$ v(f)=v(\mathbf{f}) $$ 

whenever $f$ is $C^{\infty}$ on a neighborhood of $m$ and $v$ is a tangent vector of any order at $m$.

Finally, just as there are natural mappings of tangent vectors and differentials associated with a differentiable map $\varphi\colon M\to N$, so are there linear mappings

 $$ \begin{aligned}{}&{{}d^{k}\varphi\colon M_{m}{}^{k}\to N_{\varphi(m)}^{k},}\\ {}&{{}\delta^{k}\varphi\colon{}^{k}N_{\varphi(m)}\to{}^{k}M_{m}}\\ \end{aligned} $$ 

defined by

 $$ \begin{array}{c}{d^{k}\varphi(v)(g)=v(g\circ\varphi),}\\ {\partial^{k}\varphi(d^{k}g)=d^{k}(g\circ\varphi)}\\ \end{array} $$ 

whenever $v\in M_{m}^{k}$ and $g$ is a $C^{\infty}$ function on a neighborhood of $\varphi(m)$. It is easily checked that (14) does indeed define the mappings (13) and that the mappings $d^{k}\varphi$ and $\delta^{k}\varphi$ are dual.

Our definition of a first order tangent vector in this section agrees with Definition 1.14 in view of Lemma 1.16. Moreover, we have seen three interpretations of the first order differential $df$ of a function $f$; the interpretation (13) agrees with our original definition 1.22(1), the interpretation (6) agrees with 1.22(6), and we have the additional interpretation (1).

## SUBMANIFOLDS, DIFFEOMORPHISMS, AND THE INVERSE FUNCTION THEOREM

1.27 Definitions Let  $ \psi\colon M \to N $ be  $ C^\infty $.

(a)  $ \psi $ is an immersion if  $ d\psi_{m} $ is non-singular for each  $ m \in M $.

(b) The pair $(M,\psi)$ is a submanifold of $N$ if $\psi$ is a one-to-one immersion.

(c)  $ \psi $ is an imbedding if  $ \psi $ is a one-to-one immersion which is also a homeomorphism into; that is,  $ \psi $ is open as a map into  $ \psi(M) $ with the relative topology.

(d)  $ \psi $ is a diffeomorphism if  $ \psi $ maps  $ M $ one-to-one onto  $ N $ and  $ \psi^{-1} $ is  $ C^\infty $.

1.28 Remarks on 1.27 One can, for example, immerse the real line R into the plane, as illustrated in the following figure, so that the first case is an immersion which is not a submanifold, the second is a submanifold which is not an imbedding, and the third is an imbedding.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//84cfd649-485a-47cc-b27b-fb4ff71ab8f1/markdown_2/imgs/img_in_image_box_128_118_775_372.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A22Z%2F-1%2F%2Fd69daef1650dd84204875a5e6ccbf781c6ab8b6297f97a5056bb487365fade55" alt="Image" width="68%" /></div>


Immersion, but not a Submanifold

Submanifold, but not an Imbedding

Imbedding

Observe that if $(U,\varphi)$ is a coordinate system, then $\varphi\colon U\to\varphi(U)$ is a diffeomorphism.

The composition of diffeomorphisms is again a diffeomorphism. Thus the relation of being diffeomorphic is an equivalence relation on the collection of differentiable manifolds. It is quite possible for a locally Euclidean space to possess distinct differentiable structures which are diffeomorphic. (See Exercise 2.) In a remarkable paper, Milnor showed the existence of locally Euclidean spaces ($S^{7}$ is an example) which possess non-diffeomorphic differentiable structures [19]. There are also locally Euclidean spaces which possess no differentiable structures at all [14].

If $\psi$ is a diffeomorphism, then $d\psi_m$ is an isomorphism since both $(d\psi \circ d\psi^{-1})|_{\psi(m)}$ and $(d\psi^{-1} \circ d\psi)|_m$ are the identity transformations. The inverse function theorem gives us a local converse of this—whenever $d\psi_m$ is an isomorphism, $\psi$ is a diffeomorphism on a neighborhood of $m$. Before we recall the precise statement of the inverse function theorem, we give a definition which will be needed in the corollaries.

1.29 Definition A set $y_{1}, \ldots, y_{i}$ of $C^{\infty}$ functions defined on some neighborhood of $m$ in $M$ is called an independent set at $m$ if the differentials $dy_{1}, \ldots, dy_{i}$ form an independent set in $M_{m}^{*}$.

1.30 Inverse Function Theorem Let  $ U \subset \mathbb{R}^d $ be open, and let  $ f: U \to \mathbb{R}^d $ be  $ C^\infty $. If the Jacobian matrix

 $$ \left\{\frac{\partial r_{i}\circ f}{\partial r_{j}}\right\}_{i,j=1,\ldots,d} $$ 

is non-singular at  $ r_0 \in U $, then there exists an open set  $ V $ with  $ r_0 \in V \subset U $ such that  $ f \mid V $ maps  $ V $ one-to-one onto the open set  $ f(V) $, and  $ (f \mid V)^{-1} $ is  $ C^\infty $.

This is one of the results we shall assume from advanced calculus. For a proof, we refer the reader, for example, to [31] or [6].

##### Manifolds

Corollary (a) Assume that $\psi: M \to N$ is $C^{\infty}$, that $m \in M$, and that $d\psi: M_{m} \to N_{\psi(m)}$ is an Isomorphism. Then there is a neighborhood $U$ of $m$ such that $\psi: U \to \psi(U)$ is a diffeomorphism onto the open set $\psi(U)$ in $N$.

PROOF Observe that $\dim M = \dim N$, say $d$. Choose coordinate systems $(V, \varphi)$ about $m$ and $(W, \tau)$ about $\varphi(m)$ with $\varphi(V) \subset W$. Let $\varphi(m) = p$ and $\tau(\varphi(m)) = q$. The differential of the map $\tau \circ \varphi \circ \varphi^{-1} \mid \varphi(V)$ is non-singular at $p$. Thus the inverse function theorem yields a diffeomorphism $\alpha: \tilde{U} \to \alpha(\tilde{U})$ on a neighborhood $\tilde{U}$ of $p$ with $\tilde{U} \subset \varphi(V)$. Then $\tau^{-1} \circ \alpha \circ \varphi$ is the required diffeomorphism on the neighborhood $U = \varphi^{-1}(\tilde{U})$ of $m$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//84cfd649-485a-47cc-b27b-fb4ff71ab8f1/markdown_3/imgs/img_in_image_box_173_372_781_655.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A23Z%2F-1%2F%2F6ff03c55b62496e4752ebad6c45af85138b30c6126dbfd5aa4a758f8cec58703" alt="Image" width="61%" /></div>


Corollary (b) Suppose that $\dim M = d$ and that $y_1, \ldots, y_d$ is an independent set of functions at $m_0 \in M$. Then the functions $y_1, \ldots, y_d$ form a coordinate system on a neighborhood of $m_0$.

PROOF Suppose that the $y_i$ are defined on the open set $U$ containing $m_0$. Define $\psi: U \to \mathbb{R}^d$ by

 $$ \psi(m)=\left(y_{1}(m),\ldots,y_{d}(m)\right)\qquad(m\in U). $$ 

Then  $ \psi $ is  $ C^{\infty} $. Now  $ \delta\psi $ is an isomorphism on  $ (\mathbb{R}_{\psi(m_{a})}^{d})^{*} $ since

 $$ \delta\varphi(d r_{i})=d(r_{i}\circ\varphi)=d y_{i} $$ 

which implies that  $ \delta\psi\big|_{\psi(m_0)} $ takes a basis to a basis. Consequently, the differential  $ d\psi_{m_0} $ (which is the dual of  $ \delta\psi\big|_{\psi(m_0)} $) is an isomorphism. So the inverse function theorem implies that  $ \psi $ is a diffeomorphism on a neighborhood  $ V \subset U $ of  $ m_0 $, and consequently the functions  $ y_1, \ldots, y_d $ yield a coordinate system when restricted to V.

Corollary (c) Suppose that $\dim M = d$ and that $y_{1}, \ldots, y_{1}$, with $l < d$, is an independent set of functions at $m$. Then they form part of a coordinate system on a neighborhood of $m$.

PROOF Let $(U, x_1, \ldots, x_d)$ be a coordinate system about $m$. Then $\{dy_1, \ldots, dy_i, dx_1, \ldots, dx_d\}$ spans $M_m^*$. Choose $d-l$ of the $x_i$ so that $\{dy_1, \ldots, dy_i, dx_{i_1}, \ldots, dx_{i_{d-1}}\}$ is a basis of $M_m^*$. Then apply Corollary (b).

Corollary (d) Let $\psi: M \to N$ be $C^{\infty}$, and assume that $d\psi: M_{m} \to N_{\psi(m)}$ is surjective. Let $x_{1}, \ldots, x_{1}$ form a coordinate system on some neighborhood of $\psi(m)$. Then $x_{1} \circ \psi, \ldots, x_{1} \circ \psi$ form part of a coordinate system on some neighborhood of $m$.

PROOF The fact that $d\psi_{m}$ is surjective implies that the dual map $\delta\psi|_{v(m)}$ is injective. Thus the functions $\{x_{i}\circ\psi:i=1,\ldots,l\}$ are independent at $m$ since $\delta\psi(dx_{i})=d(x_{i}\circ\psi)$. The claim now follows from Corollary (c).

Corollary (e) Suppose that $y_{1},\ldots,y_{k}$ is a set of $C^{\infty}$ functions on a neighborhood of $m$ such that their differentials span $M_{m}^{*}$. Then a subset of the $y_{i}$ forms a coordinate system on a neighborhood of $m$.

PROOF Simply choose a subset whose differentials form a basis of  $ M_{m}^{*} $, and apply Corollary (b).

Corollary (f) Let $\psi: M \to N$ be $C^{\infty}$, and assume that $d\psi: M_{m} \to N_{\psi(m)}$ is injective. Let $x_{1}, \ldots, x_{k}$ form a coordinate system on a neighborhood of $\psi(m)$. Then a subset of the functions $\{x_{i} \circ \psi\}$ forms a coordinate system on a neighborhood of $m$. In particular, $\psi$ is one-to-one on a neighborhood of $m$.

PROOF The fact that $d\psi_m$ is injective implies that $\delta\psi|_{\psi(m)}$ is surjective. This implies that $\{d(x_i \circ \psi) = \delta\psi(dx_i): i = 1, \ldots, k\}$ spans $M_m^*$. This corollary then follows from Corollary (e).

1.31 The situation often arises that one has a $C^{\infty}$ mapping, say $\psi$, of a manifold $N$ into a manifold $M$ factoring through a submanifold $(P,\varphi)$ of $M$. That is, $\psi(N) \subset \varphi(P)$, whence there is a uniquely defined mapping $\psi_0$ of $N$ into $P$ such that $\varphi \circ \psi_0 = \psi$. The problem is: When is $\psi_0$ of class $C^{\infty}$? This is certainly not always the case. As an example, let $N$ and $P$ both be the real line, and let $M$ be the plane. Let $(\mathbb{R},\psi)$ and $(\mathbb{R},\varphi)$ both be figure-8 submanifolds with precisely the same image sets, but with the difference that as $t \to \pm \infty$, $\psi(t)$ approaches the intersection along the horizontal direction, but $\varphi(t)$ approaches along the vertical. Suppose also that $\psi(0) = \varphi(0) = 0$. Then $\psi_0$ is not even continuous since $\psi_0^{-1}(-1,1)$ consists of the origin plus two open sets of the form $(\alpha,+\infty)$, $(-\infty,-\alpha)$ for some $\alpha > 0$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c39f73a5-46d9-4f67-96a1-7149c914d027/markdown_0/imgs/img_in_image_box_153_1038_578_1216.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A26Z%2F-1%2F%2F62a19391c8cb30e9da0ec000f85b3aa8252dcd22eadef9d695181b7bc332824a" alt="Image" width="44%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c39f73a5-46d9-4f67-96a1-7149c914d027/markdown_0/imgs/img_in_image_box_615_1044_813_1171.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A26Z%2F-1%2F%2Fa7927a52a7137dfd1c82687293f1e0d99dad474edf535e42a4883c96c248d106" alt="Image" width="20%" /></div>


1.32 Theorem Suppose that $\psi: N \to M$ is $C^\infty$, that $(P, \varphi)$ is a submanifold of $M$, and that $\varphi$ factors through $(P, \varphi)$, that is, $\psi(N) \subset \varphi(P)$. Since $\varphi$ is injective, there is a unique mapping $\psi_0$ of $N$ into $P$ such that $\varphi \circ \varphi_0 = \varphi$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c39f73a5-46d9-4f67-96a1-7149c914d027/markdown_1/imgs/img_in_image_box_346_196_547_325.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A28Z%2F-1%2F%2F6b01c3effd7538a62fbc1e33270dc28406135b8b1d3a5f3d83061f515c9ac295" alt="Image" width="20%" /></div>


(a)  $ \psi_{0} $ is  $ C^{\infty} $ if it is continuous.

(b)  $ \psi_{0} $ is continuous if  $ \varphi $ is an imbedding.

Another important case in which  $ \varphi_{0} $ is continuous occurs when  $ (P,\varphi) $ is an integral manifold of an involutive distribution on M, as we shall see in 1.62.

PROOF Result (b) is obvious. So assume that $\psi_0$ is continuous. We prove that it is $C^\infty$. It suffices to show that $P$ can be covered by coordinate systems $(U,\tau)$ such that the map $\tau\circ\psi_0$ restricted to the open set $\psi_0^{-1}(U)$ is $C^\infty$. Let $p\in P$, and let $(V,\gamma)$ be a coordinate system on a neighborhood of $\varphi(p)$ in $M^d$. Then by Corollary (f) of 1.30 there exists a projection $\pi$ of $\mathbb{R}^d$ onto a suitable subspace (obtained by setting certain of the coordinate functions equal to $0$) such that the map $\tau=\pi\circ\gamma\circ\varphi$ yields a coordinate system on a neighborhood $U$ of $p$. Then

 $$ \begin{aligned}{\tau\circ\psi_{\emptyset}\mid\psi_{\emptyset}^{-1}(U)}&{{}=\pi\circ\gamma\circ\varphi\circ\psi_{\emptyset}\mid\psi_{\emptyset}^{-1}(U)}\\ {}&{{}=\pi\circ\gamma\circ\psi\mid\psi_{\emptyset}^{-1}(U),}\\ \end{aligned} $$ 

which is  $ C^{\infty} $

1.33 Further Remarks on Submanifolds Submanifolds  $ (N_{1},\varphi_{1}) $ and  $ (N_{2},\varphi_{2}) $ of M will be called equivalent if there exists a diffeomorphism  $ \alpha\colon N_{1}\to N_{2} $ such that  $ \varphi_{1}=\varphi_{2}\circ\alpha $.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c39f73a5-46d9-4f67-96a1-7149c914d027/markdown_1/imgs/img_in_image_box_345_900_553_1026.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A29Z%2F-1%2F%2F4e85340033c1ee7082cc74b459bb075ea5d3295abc64bf5c2a690785967ebf4c" alt="Image" width="21%" /></div>


This is an equivalence relation on the collection of all submanifolds of $M$. Each equivalence class $\xi$ has a unique representative of the form $(A,i)$ where $A$ is a subset of $M$ with a manifold structure such that the inclusion map $i: A \to M$ is a $C^\infty$ immersion. Namely, if $(N,\varphi)$ is any representative

of $\xi$, then the subset $A$ of $M$ must be $\varphi(N)$. We induce a manifold structure on $A$ by requiring $\varphi: N \to A$ to be a diffeomorphism. With this manifold structure, $(A,i)$ is a submanifold of $M$ equivalent to $(N,\varphi)$. This is the only manifold structure on $A$ with the property that $(A,i)$ is equivalent to $(N,\varphi)$; thus this is the unique such representative of $\xi$.

The conclusion of some theorems in the following sections states that there exist unique submanifolds satisfying certain conditions. Uniqueness means up to equivalence as defined above. In particular, if the submanifolds of $M$ are viewed as subsets $A \subset M$ with manifold structures for which the inclusion maps are $C^{\infty}$ immersions, then uniqueness means unique subset with unique second countable locally Euclidean topology and unique differentiable structure.

In the case of a submanifold $(A,i)$ of $M$ where $i$ is the inclusion map, we shall often drop the $i$ and simply speak of the submanifold $A \subset M$.

Let $A$ be a subset of $M$. Then generally there is not a unique manifold structure on $A$ such that $(A,l)$ is a submanifold of $M$, if there is one at all. For example, the diagrams in 1.31 illustrate two distinct manifold structures on the figure-8 in the plane, each of which makes the figure-8 together with the inclusion map a submanifold of $\mathbb{R}^{2}$. However, we have the following two uniqueness theorems which involve conditions on the topology on $A$.

(a) Let $M$ be a differentiable manifold and $A$ a subset of $M$. Fix a topology on $A$. Then there is at most one differentiable structure on $A$ such that $(A, i)$ is a submanifold of $M$, where $i$ is the inclusion map.

(b) Again let $A$ be a subset of $M$. If in the relative topology, $A$ has a differentiable structure such that $(A,i)$ is a submanifold of $M$, then $A$ has a unique manifold structure (that is, unique second countable locally Euclidean topology together with a unique differentiable structure) such that $(A,i)$ is a submanifold of $M$.

We leave these to the reader as exercises. Result (a) follows from an application of Theorem 1.32. Result (b) depends strongly on our assumption that manifolds are second countable, and for its proof you will need to use the proposition in Exercise 6 in addition to Theorem 1.32.

1.34 Slices Suppose that $(U,\varphi)$ is a coordinate system on $M$ with coordinate functions $x_1,\ldots,x_d$, and that $c$ is an integer, $0\leq c\leq d$. Let $a\in\varphi(U)$, and let

 $$ S=\{q\in U\colon x_{i}(q)=\mathbb{X}_{i}(a),i=c+1,\ldots,d\}. $$ 

The subspace S of M together with the coordinate system

 $$ \{x_{i}\mid S\colon j=1,\ldots,c\} $$ 

forms a manifold which is a submanifold of $M$ called a slice of the coordinate system $(U, \varphi)$.

## 28 Manifolds

1.35 Proposition Let $\psi: M^{c} \to N^{d}$ be an immersion, and let $m \in M$. Then there exists a cubic-centered coordinate system $(V, \varphi)$ about $\psi(m)$ and a neighborhood $U$ of $m$ such that $\psi \mid U$ is 1:1 and $\psi(U)$ is a slice of $(V, \varphi)$.

PROOF Let $(W,\tau)$ be a centered coordinate system about $\psi(m)$ with coordinate functions $y_{1},\ldots,y_{d}$. By Corollary (f) of 1.30 we can renumber the coordinate functions so that

 $$ \tilde{\tau}=\pi_{a}\circ\tau\circ\psi $$ 

is a coordinate map on a neighborhood $V'$ of $m$ where $\pi_e\colon\mathbb{R}^d\to\mathbb{R}^e$ is projection on the first $c$ coordinates. Define functions $\{x_t\}$ on $(\pi_e\circ\tau)^{-1}(\tilde{\tau}(V'))$ by setting

 $$ x_{i}=\left\{\begin{aligned}{}&{{}y_{i}}&{}&{{}(i=1,\ldots,c)}\\ {}&{{}y_{i}-y_{i}\circ\psi\circ\tilde{\tau}^{-1}\circ\pi_{c}\circ\tau}&{}&{{}(i=c+1,\ldots,d).}\\ \end{aligned}\right. $$ 

The functions $\{x_{t}\}$ are independent at $\psi(m)$, since at $\psi(m)$,

 $$ d x_{i}=\left\{\begin{aligned}{}&{{}d y_{i}}&{}&{{}(i=1,\ldots,c)}\\ {}&{{}d y_{i}+\sum_{s=1}^{c}a_{i j}d y_{j}}&{}&{{}(i=c+1,\ldots,d)}\\ \end{aligned}\right. $$ 

for some constants $a_{ij}$. By Corollary (b) of 1.30 the $\{x_i\}$ form a coordinate system on a neighborhood of $\psi(m)$. Let $V$ be a neighborhood of $\psi(m)$ on which the $x_1, \ldots, x_d$ form a cubic coordinate system. Denote the corresponding coordinate map by $\varphi$. Let $U = \psi^{-1}(V) \cap V$. Then $U$ and $(V, \varphi)$ are the required neighborhood and coordinate system.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c39f73a5-46d9-4f67-96a1-7149c914d027/markdown_3/imgs/img_in_image_box_122_729_777_1178.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A31Z%2F-1%2F%2Fcb834f6e4bfd97b811d4e74586a7268e15601db460b613d89f3581b62c017674" alt="Image" width="66%" /></div>


We emphasize that this proposition only says that there is a neighborhood $U$ of $m$ such that $\psi(U)$ is a slice of the coordinate system $(V,\varphi)$. Even if $(M,\psi)$ is a submanifold of $N$, it may well be that $\psi(M)\cap V$ is far from being a slice or even a union of slices. For an example, consider again the figure-8 submanifold of the plane:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//cfd2d4f8-2f72-4986-81e3-8d0f6ee731af/markdown_0/imgs/img_in_image_box_131_248_790_491.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A11Z%2F-1%2F%2Fe8f638f81df0e233e4d2bdcd55c43566bfd3a922ac5fa9695996d31b3b08c423" alt="Image" width="69%" /></div>


However, in the case that $(M,\psi)$ is an imbedded submanifold, the coordinate system $(V,\varphi)$ can be chosen so that all of $\psi(M)\cap V$ is a single slice of $V$.

Let us now consider the question of the extent to which the set of $C^{\infty}$ functions on a manifold determines the set of $C^{\infty}$ functions on a submanifold. Let $(M,\psi)$ be a submanifold of $N$. Then, of course, if $f\in C^{\infty}(N)$, then $f|M$ is a $C^{\infty}$ function on $M$. (More precisely, $f\circ\psi$ is a $C^{\infty}$ function on $M$) In general, however, the converse does not hold; that is, not all $C^{\infty}$ functions on $M$ arise as the restrictions to $M$ of $C^{\infty}$ functions on $N$. For the converse to hold, it is necessary and sufficient to assume that $\psi$ is an imbedding and that $\psi(M)$ is closed. We prove the sufficiency in the following proposition, and leave the necessity as Exercise 11 below.

1.36 Proposition Let $\psi: M \to N$ be an imbedding such that $\psi(M)$ is closed in $N$. If $g \in C^{\infty}(M)$, then there exists $f \in C^{\infty}(N)$ such that $f \circ \psi = g$.

To simplify notation, we shall suppress the map $\psi$ and consider $M \subset N$.

PROOF For each point $p \in M$ there exists an open set $O_p$ in $N$ containing $p$ and an extension of $g$ from $O_p \cap M$ to a $C^\infty$ function $\tilde{g}_p$ on $O_p$. One simply has to take $O_p$ to be a cubic-centered coordinate neighborhood of $p$ for which $M \cap O_p$ is a single slice, and then define $\tilde{g}_p$ to be the composition of the natural projection of $O_p$ onto the slice followed by $g$. The collection $\{O_p : p \in M\}$ together with $N - M$ forms an open cover of $N$. By Theorem 1.11, there exists a partition of unity $\{\varphi_i\}$, with $j = 1, 2, \ldots$, subordinate to this cover. Take the subsequence (which we shall continue to denote by $\{\varphi_i\}$) such that supp $\varphi_i \cap M \neq \emptyset$. For each such $j$, we can choose a point $p_i$ such that supp $\varphi_i \subset O_{p_i}$. Then $f = \sum_{j} \varphi_i \tilde{g}_{p_i}$ is a $C^\infty$ function on $N$, and $f \mid M = g$.

##### IMPLICIT FUNCTION THEOREMS

From the inverse function theorem we shall obtain two theorems which will provide us with an extremely useful way of proving that certain subsets of manifolds are submanifolds. Under suitable conditions on a differentiable map, the inverse image of a submanifold of its range will be a submanifold of its domain. We first recall the statement of the classical implicit function theorem. This is simply a local (but somewhat more explicit) version of the first "implicit function" theorem (1.38) that we shall prove for manifolds. We suggest that the reader supply a proof of 1.37 after reading 1.38.

1.37 Implicit Function Theorem Let  $ U \subset \mathbb{R}^{e-d} \times \mathbb{R}^{d} $ be open, and let  $ f: U \to \mathbb{R}^{d} $ be  $ C^{\infty} $. We denote the canonical coordinate system on  $ \mathbb{R}^{e-d} \times \mathbb{R}^{d} $ by  $ (r_{1}, \ldots, r_{e-d}, s_{1}, \ldots, s_{d}) $. Suppose that at the point  $ (r_{0}, s_{0}) \in U $

 $$ f(r_{0},s_{0})=0, $$ 

and that the matrix

 $$ \left\{\frac{\partial f_{i}}{\partial s_{j}}\bigg|_{(r_{0},s_{0})}\right\}_{i,j=1,\ldots,d} $$ 

is non-singular. Then there exists an open neighborhood $V$ of $r_0$ in $\mathbb{R}^{s-d}$ and an open neighborhood $W$ of $s_0$ in $\mathbb{R}^d$ such that $V \times W \subset U$, and there exists a $C^\infty$ map $g: V \to W$ such that for each $(p,q) \in V \times W$

 $$ f(p,q)=0\;\:\leftrightarrow\;q=g(p). $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//cfd2d4f8-2f72-4986-81e3-8d0f6ee731af/markdown_1/imgs/img_in_image_box_158_769_735_1115.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A12Z%2F-1%2F%2F12413bed76d0a04870a665bf0aca6b65b9d4d4872e0ede15892bc2422834ff98" alt="Image" width="58%" /></div>


1.38 Theorem Assume that $\Psi: M^{c} \to N^{d}$ is $C^{\infty}$, that $n$ is a point of $N$, that $P = \psi^{-1}(n)$ is non-empty, and that $d\psi: M_{m} \to N_{\psi(m)}$ is surjective for all $m \in P$. Then $P$ has a unique manifold structure such that $(P, i)$ is a submanifold of $M$, where $i$ is the inclusion map. Moreover, $i: P \to M$ is actually an imbedding, and the dimension of $P$ is $c - d$.

PROOF According to result (b) of 1.33, it is sufficient to prove that in the relative topology, $P$ has a differentiable structure such that $(P,i)$ is a submanifold of $M$ of dimension $c-d$. For this it is sufficient to prove that if $m\in P$, then there exists a coordinate system on a neighborhood $U$ of $m$ in $M$ for which $P\cap U$ is a single slice of the correct dimension. Let $x_{1},\ldots,x_{d}$ be a coordinate system centered at $n$ in $N$. Then since $d\psi:M_{m}\to N_{n}$ is surjective, it follows from Corollary (d) of 1.30 that the collection of functions

 $$ \{y_{i}=x_{i}\circ\psi\colon i=1,\ldots,d\}, $$ 

forms part of a coordinate system about $m\in M$. Complete to a coordinate system $y_1,\ldots,y_d,y_{d+1},\ldots,y_c$ on a neighborhood $U$ of $m$. Then $P\cap U$ is precisely the slice of this coordinate system given by

 $$ y_{1}=y_{2}=\cdots=y_{d}=0. $$ 

In this theorem the inverse image of a point is shown to be a submanifold as long as the differential is surjective at each point of the inverse image. A point can be thought of as a 0-dimensional submanifold. We now generalize this theorem by proving that under suitable conditions the inverse images of higher dimensional submanifolds are themselves submanifolds.

1.39 Theorem Assume that $\psi: M \to N^d$ is $C^\infty$ and that $(O^c, \varphi)$ is a submanifold of $N$. Suppose that whenever $m \in \psi^{-1}\left(\varphi(O)\right)$, then

 $$ N_{\psi(m)}=d\psi(M_{m})+d\varphi(O_{\psi^{-1}(\psi(m))}) $$ 

(not necessarily a direct sum). Then if $P=\psi^{-1}\big(\varphi(O)\big)$ and is non-empty, $P$ can be given a manifold structure so that $(P,i)$ is a submanifold of $M$, where $i$ is the inclusion map, with

 $$ \dim M-\dim P=\dim N-\dim O. $$ 

Moreover, if $(O,\varphi)$ is an imbedded submanifold, then so is $(P,i)$, and in this case there is a unique manifold structure on $P$ such that $(P,i)$ is a submanifold of $M$.

In general, if $(O,\varphi)$ is not an imbedding, $P$ need not have the relative topology, and there is no unique manifold structure on $P$ such that $(P,i)$ is a submanifold. We leave it to the reader to supply examples.

PROOF The proof will consist of locally reducing this case to the case of Theorem 1.38. Let $p \in O$. By Proposition 1.35, we can pick a neighborhood $W$ of $p$ and a centered coordinate system $(V, \tau)$ with coordinate functions $x_{1}, \ldots, x_{d}$ about $\varphi(p)$ such that $\varphi(W)$ is the slice

(3)

 $$ x_{e+i}=0\qquad(j=1,\ldots,d-c). $$ 

Let

 $$ \pi\colon\mathbb{R}^{d}\to\mathbb{R}^{d-c}, $$ 

 $$ \pi(a)=(a_{e+1},\ldots,a_{d}). $$ 

So

(5)

 $$ \pi\circ\tau\bigl(\varphi(W)\bigr)=\{0\}. $$ 

Let

(6)

 $$ U=\psi^{-1}(V), $$ 

and let

(7)

 $$ \psi_{1}=\pi\circ\tau\circ\psi\mid U\colon U\to\mathbb{R}^{d-c}. $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//cfd2d4f8-2f72-4986-81e3-8d0f6ee731af/markdown_3/imgs/img_in_image_box_104_579_763_916.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A12Z%2F-1%2F%2F25d7888242b98ce45ec090bf36ac141e2d8b93edc291e380f453508340c4a286" alt="Image" width="67%" /></div>


Now, (3) through (7) imply that

 $$ \psi_{1}^{-1}(0)=\psi^{-1}\big(\varphi(W)\big). $$ 

For each point  $ m \in \psi_{1}^{-1}(0) $,  $ d\psi_{1} \mid M_{m} $ is surjective since  $ d(\pi \circ \tau) \mid N_{\psi(m)} $ is surjective and since by (1), (5), and (7)

 $$ d(\pi\circ\tau)(N_{\varphi(m)})=d\psi_{1}(M_{m})+\{0\}. $$ 

Thus by 1.38,  $ \psi^{-1}(\varphi(W)) $ has a unique manifold structure such that  $ (\psi^{-1}(\varphi(W)), i) $ is a submanifold of  $ M $; and in this manifold structure,

 $ \psi^{-1}\left(\varphi(W)\right) $ has the relative topology and has dimension equal to  $ \dim M - \dim N + \dim O $. Cover O by a countable collection  $ \{W_i: i = 1, 2, 3, \ldots\} $ of such sets. Then

 $$ P=\bigcup_{i=1}^{\infty}\psi^{-1}\bigl(\varphi(W_{i})\bigr). $$ 

If $i \neq j$, the submanifolds $\psi^{-1}(\varphi(W_i))$ and $\psi^{-1}(\varphi(W_i))$ intersect in open subsets of each other. It follows that the union of the topologies on the various $\psi^{-1}(\varphi(W_i))$ forms a basis for a topology on $P$. With this topology, $P$ is a locally Euclidean space with dimension equal to $\dim M - \dim N + \dim O$; and, moreover, $P$ is second countable since (9) expresses $P$ as a countable union of second countable open subsets. The manifold structures on the various $\psi^{-1}(\varphi(W_i))$ are compatible on overlaps because of the uniqueness of the manifold structure on $\psi^{-1}(\varphi(W_i))$ (or any open subset of $\psi^{-1}(\varphi(W_i))$) such that $(\psi^{-1}(\varphi(W_i)))$ is a submanifold of $M$ (by result (b) of 1.33). Thus the collection of coordinate systems on $P$ containing the coordinate systems on the various $\psi^{-1}(\varphi(W_i))$ and maximal with respect to 1.4(b) forms a differentiable structure on $P$. That $(P,i)$ is a submanifold of $M$ now follows immediately from the fact that the $(\psi^{-1}(\varphi(W_i)))$ are submanifolds. If $(O, \varphi)$ is an imbedding, the coordinate neighborhood $V$ can be chosen small enough so that $\varphi(O) \cap V$ consists only of the single slice $\varphi(W)$, and thus $U \cap P = \psi^{-1}(\varphi(W))$. It follows in this case that $P$ has the relative topology; hence $(P,i)$ is an imbedding. The uniqueness of the manifold structure in this case is guaranteed by result (b) of 1.33.

### 1.40 Examples

(a) The differential of the function $f(p) = \sum_{i=1}^{a} r_i(p)^2$ on $\mathbb{R}^d$ is surjective except at the origin. Thus it follows from 1.38 that the sphere $f^{-1}(r^2)$, for a constant $r > 0$, has a unique manifold structure for which it is a submanifold of $\mathbb{R}^d$ under the inclusion map. In particular, this is the same manifold structure as the one defined in Example 1.5(d).

(b) We define a map $\psi$ from the general linear group $Gl(d, \mathbb{R})$ (Example 1.5(f)) to the vector space of all real symmetric $d \times d$ matrices by

 $$ \psi(A)=A A^{t}, $$ 

where  $ A^{t} $ is the transpose of the matrix A. Let

 $$ O(d)=\psi^{-1}(I) $$ 

where $I$ is the $d \times d$ identity matrix. $O(d)$ is a subgroup of $Gl(d,\mathbb{R})$ under matrix multiplication called the orthogonal group. To apply 1.38 to conclude that $O(d)$ has a unique manifold structure such that $(O(d),i)$ is a submanifold of $Gl(d,\mathbb{R})$, and that in this manifold structure $i$ is an imbedding and $O(d)$ has dimension $\frac{1}{2}(d(d-1))$, one

## 34 Manifolds

need only check that  $ d\psi_\sigma $ is surjective at each  $ \sigma \in O(d) $. For this, it suffices to check that  $ d\psi_I $ is surjective, since whenever  $ \sigma \in O(d) $,

 $$ \varphi=\varphi\circ r_{o} $$ 

where  $ r_{\sigma} $ (right translation by  $ \sigma $) is the diffeomorphism of  $ Gl(d, \mathbb{R}) $ defined by  $ r_{\sigma}(\tau) = \tau\sigma $. We leave the details to the reader as an exercise.

##### VECTOR FIELDS

1.41 Definitions Smooth curves $\sigma: (a,b) \to M$ and their tangent vectors $\dot{\sigma}(t)$ were defined in 1.23(e). We say that a mapping $\sigma: [a,b] \to M$ is a smooth curve in $M$ if $\sigma$ extends to be a $C^\infty$ mapping of $(a-e, b+\varepsilon)$ into $M$ for some $\varepsilon > 0$. The curve $\sigma: [a,b] \to M$ is said to be piecewise smooth if there exists a partition $a = \alpha_0 < \alpha_1 < \cdots < \alpha_n = b$ such that $\sigma \mid [\alpha_t, \alpha_{t+1}]$ is smooth for each $t = 0, \ldots, n-1$. Observe that piecewise smooth curves are necessarily continuous. If $\sigma: [a,b] \to M$ is a smooth curve in $M$, then its tangent vector

 $$ \delta(t)=d\sigma\biggl(\frac{d}{d r}\biggl|_{t}\biggr)\in M_{\sigma(t)} $$ 

is well-defined for each  $ t \in [a, b] $.

1.42 Definitions A vector field X along a curve  $ \sigma $:  $ [a,b] \to M $ is a mapping  $ X\colon [a,b] \to T(M) $ which lifts  $ \sigma $; that is,  $ \pi \circ X = \sigma $. A vector field

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//39657b02-4b6c-4478-8c26-3631161b8894/markdown_1/imgs/img_in_image_box_133_752_767_1159.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A12Z%2F-1%2F%2Fc5b8ddebffbb41f1921c94691820368e7e191637890ed1428f39832a85e73a56" alt="Image" width="64%" /></div>


X is called a smooth $(C^{\infty})$ vector field along $\sigma$ if the mapping $X\colon[a,b]\to T(M)$ is $C^{\infty}$. A vector field $X$ on an open set $U$ in $M$ is a lifting of $U$ into $T(M)$, that is, a map $X\colon U\to T(M)$ such that

 $$ \pi\circ X=\mathrm{i d e n t i t y~m a p~o n~}U. $$ 

Again, for the vector field $X$ to be smooth ($C^\infty$) means that $X \in C^\infty(U, T(M))$. The set of smooth vector fields over $U$ forms in the obvious way a vector space over $\mathbb{R}$ and a module over the ring $C^\infty(U)$ of $C^\infty$ functions on $U$. If $X$ is a vector field on $U$ and $m \in U$, then $X(m)$ (often denoted $X_m$) is an element of $M_m$. If $f$ is a $C^\infty$ function on $U$, then $X(f)$ is the function on $U$ whose value at $m$ is $X_m(f)$.

1.43 Proposition Let X be a vector field on M. Then the following are equivalent:

(a) X is  $ C^{\infty} $.

(b) If $(U, x_{1}, \ldots, x_{d})$ is a coordinate system on $M$, and if $\{a_{i}\}$ is the collection of functions on $U$ defined by

 $$ X\mid U=\sum_{i=1}^{d}a_{i}\frac{\partial}{\partial x_{i}}, $$ 

then  $ a_{i} \in C^{\infty}(U) $.

(c) Whenever $V$ is open in $M$ and $f\in C^{\infty}(V)$, then $X(f)\in C^{\infty}(V)$.

PROOF (a) $\Rightarrow$ (b) The fact that $X$ is smooth implies that $X \mid U$ is smooth; and since the composition of differentiable maps is again differentiable, it follows that $dx_i \circ X \mid U$ is smooth. (Recall that the $dx_i$ are coordinate functions on $\pi^{-1}(U) \subset T(M)$, 1.25(3).) But

 $$ d x_{i}\circ X\mid U=a_{i}. $$ 

Hence the  $ a_{i} $ are  $ C^{\infty} $ functions on U.

(b) $\Rightarrow$ (c) It suffices to prove that $X(f) \mid U \in C^{\infty}(U)$ where $(U, x_{1}, \ldots, x_{d})$ is an arbitrary coordinate system on $M$ for which $U \subset V$. But, by (b),

 $$ X(f)\left|~U=\sum_{i=1}^{d}a_{i}\frac{\partial f}{\partial x_{i}},~\right. $$ 

and the right-hand side is a  $ C^{\infty} $ function on U.

(c) $\Rightarrow$ (a) To prove that $X$ is $C^{\infty}$, it suffices to prove that $X\mid U$ is $C^{\infty}$ where $(U, x_1, \ldots, x_d)$ is an arbitrary coordinate system on $M$. To prove that $X\mid U$ is $C^{\infty}$, we need only check that $X\mid U$ composed with the canonical coordinate functions $1.25(3)$ on $\pi^{-1}(U)$ are $C^{\infty}$ functions. Now, $x_i \circ \pi \circ X\mid U = x_i$ and $dx_i \circ X\mid U = X(x_i)$, all of which are $C^{\infty}$ functions on $U$.

## 36 Manifolds

1.44 Lie Bracket If X and Y are smooth vector fields on M, we define a vector field  $ [X,Y] $ called the Lie bracket of X and Y by setting

 $$ [X,Y]_{m}(f)=X_{m}(Y f)-Y_{m}(X f). $$ 

### 1.45 Proposition

(a) [X,Y] is indeed a smooth vector field on M.

(b) If $f, g \in C^{\infty}(M)$, then $[fX, gY] = fg[X, Y] + f(Xg)Y - g(Yf)X$.

(c)  $ [X,Y] = -[Y,X] $.

(d)  $ [[X,Y],Z] + [[Y,Z],X] + [[Z,X],Y] = 0 $ for all smooth vector fields X, Y, and Z on M.

We leave the proof as an exercise. Part (d) is known as the Jacobi identity. A vector space with a bilinear operation satisfying (c) and (d) is called a Lie algebra.

1.46 Definition Let $X$ be a smooth vector field on $M$. A smooth curve $\sigma$ in $M$ is an integral curve of $X$ if

 $$ \dot{\sigma}(t)=X(\sigma(t)) $$ 

for each t in the domain of  $ \sigma $.

1.47 Let $X$ be a $C^\infty$ vector field on $M$, and let $m \in M$. Let us now consider the question: Does there exist an integral curve of $X$ through $m$, and if so, is there a unique one?

A curve  $ \gamma $:  $ (a,b) \to M $ is an integral curve of X if and only if

 $$ d\gamma\left(\frac{d}{d r}\bigg|_{t}\right)=X\big(\gamma(t)\big)\qquad\big(t\in(a,b)\big). $$ 

Let us interpret this in coordinates. Suppose that  $ 0 \in (a,b) $ and  $ \gamma(0) = m $. Choose a coordinate system  $ (U,\varphi) $ with coordinate functions  $ x_1, \ldots, x_d $ about m. By 1.43(b),

 $$ X\mid U=\sum_{i=1}^{d}f_{i}\frac{\partial}{\partial x_{i}} $$ 

where the $f_{i}$ are $C^{\infty}$ functions on $U$. Moreover, for each $t$ such that $\gamma(t) \in U$,

 $$ d\gamma\left(\frac{d}{d r}\bigg\vert_{t}\right)=\sum_{i=1}^{d}\frac{d(x_{i}\circ\gamma)}{d r}\bigg\vert_{t}\frac{\partial}{\partial x_{i}}\bigg\vert_{r(t)}. $$ 

Thus, in view of (2) and (3), equation (1) becomes

 $$ \sum_{i=1}^{d}\frac{d(x_{i}\circ\gamma)}{d r}\bigg|_{t}\frac{\partial}{\partial x_{i}}\bigg|_{\gamma(t)}=\sum_{i=1}^{d}f_{i}(\gamma(t))\frac{\partial}{\partial x_{i}}\bigg|_{\gamma(t)}. $$ 

Thus $\gamma$ is an integral curve of $X$ on $\gamma^{-1}(U)$ if and only if

 $$ \left.\frac{d\gamma_{i}}{d r}\right|_{t}=f_{i}\circ\varphi^{-1}\big(\gamma_{1}(t),\ldots,\gamma_{d}(t)\big)\qquad\big(i=1,\ldots,d\quad\mathrm{a n d}\quad t\in\gamma^{-1}(U)\big), $$ 

where $\gamma_{t}=x_{t}\circ\gamma$. Equation (5) is a system of first order ordinary differential equations for which there exist fundamental existence and uniqueness theorems [11]. These theorems, when translated into manifold terminology, give the following.

1.48 Theorem Let $X$ be a $C^\infty$ vector field on a differentiable manifold $M$. For each $m\in M$ there exists $a(m)$ and $b(m)$ in $\mathbb{R}\cup\{\pm\infty\}$, and a smooth curve

(1)

 $$ \gamma_{m}\colon\big(a(m),b(m)\big)\to M $$ 

such that

(a)  $ 0 \in (a(m), b(m)) $ and  $ \gamma_m(0) = m $.

(b)  $ \gamma_{m} $ is an integral curve of X.

(c) If $\mu\colon(c,d)\to M$ is a smooth curve satisfying conditions (a) and (b), then $(c,d)\subset(a(m),b(m))$ and $\mu=\gamma_{m}\mid(c,d)$.

We continue with the statement of the theorem after the following.

Definition For each $t\in\mathbb{R}$, we define a transformation $X_{t}$ with domain

 $$ \mathcal{D}_{t}=\left\{m\in M\colon t\in\left(a(m),b(m)\right)\right\} $$ 

by setting

(3)

 $$ X_{t}(m)=\gamma_{m}(t). $$ 

(d) For each $m \in M$, there exists an open neighborhood $V$ of $m$ and $an \varepsilon > 0$ such that the map

(4)

 $$ (t,p)\mapsto X_{t}(p) $$ 

is defined and is  $ C^{\infty} $ from  $ (-\varepsilon,\varepsilon) \times V $ into M.

(e)  $ D_{t} $ is open for each t.

(f)  $ \bigcup \mathcal{D}_t = M $.

(g)  $ X_{t}\colon \mathcal{D}_{t} \to \mathcal{D}_{-t} $ is a diffeomorphism with inverse  $ X_{-t} $.

(h) Let $s$ and $t$ be real numbers. Then the domain of $X_{s} \circ X_{t}$ is contained in but generally not equal to $\mathcal{D}_{s+t}$. However, the domain of $X_{s} \circ X_{t}$ is $\mathcal{D}_{s+t}$ in the case in which $s$ and $t$ both have the same sign. Moreover, on the domain of $X_{s} \circ X_{t}$ we have

(5)

 $$ X_{s}\circ X_{t}=X_{s+t}. $$ 

PROOF We let $(a(m),b(m))$ be the union of all the open intervals which contain the origin and which are domains of integral curves of $X$ satisfying the initial condition that the origin maps to $m$. That $(a(m),b(m)) \neq \varnothing$ (and hence part (f) holds) follows from an application of the fundamental existence theorem [11, THEOREM 4, p. 28] to the system 1.47(5). Now if $\alpha$ and $\beta$ are integral curves of $X$ with domains the open intervals $A$ and $B$ (with $A \cap B \neq \varnothing$), and if $\alpha$ and $\beta$ have the same initial conditions $\alpha(t_0) = \beta(t_0)$ at some point $t_0 \in A \cap B$, then the subset of $A \cap B$ on which $\alpha$ and $\beta$ agree is nonempty, open by the basic uniqueness theorem [11, THEOREM 3, p. 28], and closed by continuity; and hence this subset is equal to $A \cap B$ by the connectedness of $A \cap B$. It follows that there exists a curve $\gamma_m$ defined on $(a(m), b(m))$ and satisfying parts (a), (b), and (c).

The existence of an $\varepsilon>0$ and a neighborhood $V$ of $m$ such that the map (4) is defined on $(-\varepsilon,\varepsilon)\times V$ is the content of THEOREM 7 on p. 29 of [11]. That the map (4) is smooth (and hence part (d) holds) follows from THEOREM 9 on p. 29 of [11] on the differentiability of the solutions of 1.47(5) with respect to their initial values.

Next we prove part (h). Let  $ t \in (a(m), b(m)) $. Then  $ s \mapsto \gamma_m(t + s) $ is an integral curve of X with the initial condition  $ 0 \mapsto \gamma_m(t) $ and with maximal domain  $ (a(m) - t, b(m) - t) $. It follows from part (c) that

 $$ (a(m)-t,b(m)-t)=\bigl(a\bigl(\gamma_{m}(t)\bigr),b\bigl(\gamma_{m}(t)\bigr)\bigr), $$ 

and for s in the interval (6),

 $$ \gamma_{\gamma_{m}(t)}(s)=\gamma_{m}(t+s). $$ 

Now let $m$ belong to the domain of $X_s \circ X_t$. Then $t \in (a(m), b(m))$ and $s \in (a(\gamma_m(t)), b(\gamma_m(t)))$, so by (6), $s + t \in (a(m), b(m))$. Thus $m \in \mathcal{D}_{s+t}$, and (5) follows from (7). It is easy to construct examples to show that the domain of $X_s \circ X_t$ is generally not equal to $\mathcal{D}_{s+t}$. (Consider, for example, the vector field $\partial/\partial r_1$ on $\mathbb{R}^3 - \{0\}$ with $s = -1$ and $t = 1$. If, however, $s$ and $t$ both have the same sign, and if $m \in \mathcal{D}_{s+t}$, that is, if $s + t \in (a(m), b(m))$, then it follows that $t \in (a(m), b(m))$ and, by (6), $s \in (a(\gamma_m(t)), b(\gamma_m(t)))$; hence $m$ is in the domain of $X_s \circ X_t$.

Parts (e) and (g) are trivial if $t=0$, so assume that $t>0$ and that $m\in\mathcal{D}_t$. (A similar argument will prove (e) and (g)) if $t<0$. It follows from part (d) and the compactness of $[0,t]$ that there exists a neighborhood $W$ of $\gamma_m([0,t]]$ and an $\varepsilon>0$ such that the map (4) is defined and $C^\infty$ on $(-\varepsilon,\varepsilon)\times W$. Choose a positive integer $n$ large enough so that $t/n\in(-\varepsilon,\varepsilon)$. Let $\alpha_1=X_{t/n}\mid W$, and let $W_1=\alpha_1^{-1}(W)$. Then for $i=2,\ldots,n$ we inductively define

 $$ \alpha_{i}=X_{t/n}\mid W_{t-1} $$ 

and

 $$ W_{t}=\alpha_{t}^{-1}(W_{t-1}). $$ 

$\alpha_{i}$ is a $C^{\infty}$ map on the open set $W_{t-1} \subset W$. It follows that $W_{n}$ is an open subset of $W$, that $W_{n}$ contains $m$ (since if $X_{t/n}$ composed with itself $n$ times is applied to $m$, we obtain $\gamma_{m}(t)$, which lies in $W$), and that by part (h),

 $$ \alpha_{1}\circ\alpha_{2}\circ\cdots\circ\alpha_{n}\mid W_{n}=X_{t}\mid W_{n}. $$ 

Consequently, $W_{n} \subset \mathcal{D}_{t}$; hence $\mathcal{D}_{t}$ is open, which proves part (e).

Finally, $X_{t}$ is a 1:1 map of $\mathcal{D}_{t}$ onto $\mathcal{D}_{-t}$ with inverse $X_{-t}$. That $X_{t}$ is $C^{\infty}$ (similarly for $X_{-t}$) follows from (8), which locally expresses $X_{t}$ as a composition of $C^{\infty}$ maps. Hence $X_{t}$ is a diffeomorphism from $\mathcal{D}_{t}$ to $\mathcal{D}_{-t}$, which proves part (g) and finishes Theorem 1.48.

1.49 Definitions A smooth vector field $X$ on $M$ is complete if $\mathcal{D}_t = M$ for all $t$ (that is, the domain of $\gamma_m$ is $(-\infty, \infty)$ for each $m \in M$). In this case, the transformations $X_t$ form a group of transformations of $M$ parametrized by the real numbers called the 1-parameter group of $X$. If $X$ is not complete, the transformations $X_t$ do not form a group since their domains depend on $t$. In this case, we shall refer to the collection of transformations $X_t$ as the local 1-parameter group of $X$.

1.50 Remarks A simple example of a non-complete vector field is obtained by considering the vector field $\partial/\partial r_{1}$ on the plane with the origin removed. If $a>0$, the domain of the maximal integral curve through $(a,0)$ is $(-a,+\infty)$. In the case in which the manifold $M$ is compact, any $C^{\infty}$ vector field on $M$ is complete. We leave the proof as an exercise.

1.51 Definition Let $\psi: M \to N$ be $C^\infty$. A smooth vector field $X$ along $\psi$ (that is, $X \in C^\infty(M, T(N))$ and $\pi \circ X = \psi$) has local $C^\infty$ extensions in $N$ if given $m \in M$ there exist a neighborhood $U$ of $m$ and a neighborhood $V$ of $\psi(m)$ such that $\psi(U) \subset V$, and there also exists a $C^\infty$ vector field $\tilde{X}$ on $V$ such that

 $$ \tilde{X}\circ\psi\mid U=X\mid U. $$ 

1.52 Remark It is easy to prove that a $C^{\infty}$ vector field $X$ along an immersion $\psi: M \to N$ always has local $C^{\infty}$ extensions in $N$. However, if $\psi$ is not an immersion, such extensions generally do not exist. Consider the following example. We shall first define a smooth vector field $X$ along a smooth curve $\alpha: \mathbb{R} \to \mathbb{R}$ in the real line. Let

 $$ \alpha(t)=t^{3}, $$ 

(that is,  $ \alpha = r^{3} $ where r is the canonical coordinate function on  $ \mathbb{R} $), and let

 $$ X(t)=\dot{\alpha}(t)=d\alpha\left(\frac{d}{d r}\bigg|_{t}\right). $$ 

## 40 Manifolds

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//209fd49e-d8af-44d0-93d5-311b55b43ae4/markdown_3/imgs/img_in_image_box_318_101_583_300.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2Ff489560058f2522ce56c7c0c9575b35b26713e7f94d3474be1a3368e9142be90" alt="Image" width="27%" /></div>


Since $\alpha$ is a homeomorphism, there is induced a vector field $\tilde{X}$ on $\mathbb{R}^{1}$ so that the above diagram commutes. Now, $X$ is a smooth vector field along $\alpha$, but $\tilde{X}$ is not a smooth vector field on $\mathbb{R}^{1}$. To show this, let $u = t^{3}$. Then

 $$ \begin{aligned}{\tilde{X}_{u}}&{{}=\tilde{X}_{\alpha(t)}=X(t)=d\alpha\bigg(\frac{d}{d r}\bigg|_{t}\bigg)}\\ {}&{{}=\frac{d\alpha}{d r}\bigg|_{t}\frac{d}{d r}\bigg|_{\alpha(t)}=3t^{2}\frac{d}{d r}\bigg|_{\alpha(t)}=3u^{2/3}\frac{d}{d r}\bigg|_{u}.}\\ \end{aligned} $$ 

Thus

 $$ \tilde{X}=3r^{2/3}\frac{d}{d r}, $$ 

and the function  $ r^{2/3} $ is not differentiable at the origin. If we extend  $ \alpha $ to be a mapping into the plane by setting

 $$ \alpha(t)=(t^{3},0), $$ 

and again we let $X(t)=\dot{\alpha}(t)$, then $X$ is a smooth vector field along the one-to-one $C^{\infty}$ curve $\alpha$ in the plane, which admits no local $C^{\infty}$ extension to a neighborhood of $(0,0)$.

1.53 Proposition Let $m \in M^{d}$, and let $X$ be a smooth vector field on $M$ such that $X(m) \neq 0$. Then there exists a coordinate system $(U, \varphi)$ with coordinate functions $x_{1}, \ldots, x_{d}$ on a neighborhood of $m$ such that

 $$ x\mid U=\frac{\partial}{\partial x_{1}}\mid U. $$ 

PROOF Choose a coordinate system $(V,\tau)$ centered at $m$ with coordinate functions $y_{1},\ldots,y_{d}$, such that

 $$ X_{m}=\frac{\partial}{\partial y_{1}}\Big|_{m}. $$ 

It follows from 1.48(d) that there exists an $\varepsilon>0$ and a neighborhood $W$ of the origin in $\mathbb{R}^{d-1}$ such that the map

 $$ \sigma(t,a_{2},\ldots,a_{d})=X_{t}\big(\tau^{-1}(0,a_{2},\ldots,a_{d})\big) $$ 

is well-defined and smooth for $(t, a_{2}, \ldots, a_{d}) \in (-\varepsilon, \varepsilon) \times W \subset \mathbb{R}^{d}$.

Now,  $ \sigma $ is non-singular at the origin since

 $$ d\sigma\bigg(\frac{\partial}{\partial r_{1}}\bigg|_{0}\bigg)=X_{m}=\frac{\partial}{\partial y_{1}}\bigg|_{m}\quad\mathrm{a n d}\quad d\sigma\bigg(\frac{\partial}{\partial r_{i}}\bigg|_{0}\bigg)=\frac{\partial}{\partial y_{i}}\bigg|_{m}\qquad(i\geq2). $$ 

Thus by Corollary (a) of 1.30,  $ \varphi = \sigma^{-1} $ is a coordinate map on some neighborhood U of m. Let  $ x_1, \ldots, x_d $ denote the coordinate functions of the coordinate system  $ (U, \varphi) $. Then since

 $$ d\sigma\bigg(\frac{\partial}{\partial r_{1}}\bigg|_{(t,a_{2},\ldots,a_{n})}\bigg)=X_{\sigma(t,a_{2},\ldots,a_{n})}\;, $$ 

we have

 $$ X\mid U=\frac{\partial}{\partial x_{1}}\mid U. $$ 

1.54 Definition Let  $ \varphi: M \to N $ be  $ C^\infty $. Smooth vector fields X on M and Y on N are called  $ \varphi $-related if  $ d\varphi \circ X = Y \circ \varphi $.

1.55 Proposition Let $\varphi: M \to N$ be $C^\infty$. Let $X$ and $X_1$ be smooth vector fields on $M$, and let $Y$ and $Y_1$ be smooth vector fields on $N$. If $X$ is $\varphi$-related to $Y$, and if $X_1$ is $\varphi$-related to $Y_1$, then $[X, X_1]$ is $\varphi$-related to $[Y, Y_1]$.

PROOF We must show that  $ d_{\phi} \circ [X, X_1] = [Y, Y_1] \circ \phi $. For this, let  $ m \in M $ and  $ f \in \dot{C}^{\infty}(N) $. Then we must show that

 $$ d_{\Phi}([X,X_{1}]_{m})(f)=[Y,Y_{1}]_{\varphi(m)}(f). $$ 

We simply unwind the definitions:

 $$ \begin{aligned}{d\varphi([X,X_{1}]_{m})(f)}&{{}=[X,X_{1}]_{m}(f\circ\varphi)}\\ {}&{{}=X_{m}\big(X_{1}(f\circ\varphi)\big)-X_{1}\big|_{m}\left(X(f\circ\varphi)\right)}\\ {}&{{}=X_{m}\big((d\varphi\circ X_{1})(f)\big)-X_{1}\big|_{m}\left((d\varphi\circ X)(f)\right)}\\ {}&{{}=X_{m}\big(Y_{1}(f)\circ\varphi\big)-X_{1}\big|_{m}\big(Y(f)\circ\varphi\big)}\\ {}&{{}=d\varphi(X_{m})\big(Y_{1}(f)\big)-d\varphi(X_{1}|_{m})\big(Y(f)\big)}\\ {}&{{}=Y_{\varphi(m)}\big(Y_{1}(f)\big)-Y_{1}\big|_{\varphi(m)}\left(Y(f)\right)}\\ {}&{{}=[Y,Y_{1}]_{\varphi(m)}(f).}\\ \end{aligned} $$ 

##### DISTRIBUTIONS AND THE FROBENIUS THEOREM

1.56 Definitions Let $c$ be an integer, $1 \leq c \leq d$. A $c$-dimensional distribution $\mathcal{D}$ on a $d$-dimensional manifold $M$ is a choice of a $c$-dimensional subspace $\mathcal{D}(m)$ of $M_m$ for each $m$ in $M$. $\mathcal{D}$ is smooth if for each $m$ in $M$ there is a neighborhood $U$ of $m$ and there are $c$ vector fields $X_1, \ldots, X_c$ of class $C^\infty$ on $U$ which span $\mathcal{D}$ at each point of $U$. A vector field $X$ on $M$ is said to belong to (or lie in) the distribution $\mathcal{D}(X \in \mathcal{D})$ if $X_m \in \mathcal{D}(m)$ for each

## 42 Manifolds

 $ m \in M $. A smooth distribution  $ \mathcal{D} $ is called involutive (or completely integrable) if  $ [X, Y] \in \mathcal{D} $ whenever  $ X $ and  $ Y $ are smooth vector fields lying in  $ \mathcal{D} $.

1.57 Definition A submanifold $(N,\psi)$ of $M$ is an integral manifold of a distribution $\mathcal{D}$ on $M$ if

 $$ d\varphi(N_{n})=\mathcal{D}\big(\psi(n)\big)\quad\mathrm{f o r~e a c h}n\in N. $$ 

1.58 Remarks Our object in this section is to prove that a necessary and sufficient condition for there to exist integral manifolds of $\mathcal{D}$ through each point of $M$ is that $\mathcal{D}$ be involutive. Perhaps a word of explanation is in order about the expression “completely integrable” sometimes used in place of “involutive.” We have required integral manifolds to be submanifolds whose tangent spaces coincide with the subspaces determined by the distribution. One could define a weaker notion of integral manifold by requiring only that the tangent spaces of the submanifold be contained in but not necessarily equal to the distribution at each point. It is possible for a distribution $\mathcal{D}$ to be “integrable” in the sense that it has low-dimensional “integral manifolds,” but not completely integrable in the sense that $\mathcal{D}$ does not have integral manifolds of the maximal dimension. For us, unless specified otherwise, integral manifolds of distributions will always be taken to mean integral manifolds of maximal dimension, that is, as defined in 1.57.

1.59 Proposition Let $\mathcal{D}$ be a smooth distribution on $M$ such that through each point of $M$ there passes an integral manifold of $\mathcal{D}$. Then $\mathcal{D}$ is involutive.

PROOF Let $X$ and $Y$ be smooth vector fields lying in $\mathcal{D}$, and let $m \in M$. We must prove that $[X, Y]_{m} \in \mathcal{D}(m)$. Let $(N, \psi)$ be an integral manifold of $\mathcal{D}$ through $m$, and suppose that $\psi(n_0) = m$. Since $d\psi: N_n \to \mathcal{D}(\psi(n))$ is an isomorphism at each $n$ in $N$, there exist vector fields $\widetilde{X}$, $\widetilde{Y}$ on $N$ such that

 $$ d\psi\circ\tilde{X}=X\circ\psi, $$ 

 $$ d\psi\circ\tilde{Y}=Y\circ\psi. $$ 

It is easily checked that $\tilde{X}$ and $\tilde{Y}$ are smooth. By 1.55, $[\tilde{X},\tilde{Y}]$ and $[X,Y]$ are $\psi$-related. Hence $[X,Y]_{m}=d\psi([\tilde{X},\tilde{Y}]_{n_{0}})\in\mathcal{D}(m)$.

1.60 Theorem (Frobenius) Let $\mathcal{D}$ be a $c$-dimensional, involutive, $C^{\infty}$ distribution on $M^{d}$. Let $m\in M$. Then there exists an integral manifold of $\mathcal{D}$ passing through $m$. Indeed, there exists a cubic coordinate system $(U,\varphi)$ which is centered at $m$, with coordinate functions $x_{1},\ldots,x_{d}$ such that the slices

 $$ x_{i}=\mathrm{c o n s t a n t}\qquad\mathrm{f o r~a l l~}i\in\{c+1,\ldots,d\} $$ 

are integral manifolds of $\mathcal{D}$; and if $(N,\psi)$ is a connected integral manifold of $\mathcal{D}$ such that $\psi(N)\subset U$, then $\psi(N)$ lies in one of these slices.

PROOF We shall prove the existence part of the theorem by induction on $c$. For the case $c=1$, choose a vector field $X$ lying in $\mathcal{D}$, defined on an open neighborhood of $m$, such that $X(m)\neq0$. Then Proposition 1.53 yields a coordinate system $(U,\varphi)$ about $m$, which can be taken to be cubic centered, for which $X\mid U=\partial/\partial x_1$. Hence the theorem holds for $c=1$.

Now assume that the theorem holds for $c-1$; we prove it for a distribution $\mathcal{D}$ of dimension $c$. Since $\mathcal{D}$ is smooth, there exist smooth vector fields $X_1,\ldots,X_c$ spanning $\mathcal{D}$ on a neighborhood $\tilde{V}$ of $m$. By 1.53, there exists a coordinate system $(V,y_1,\ldots,y_d)$ centered at $m$, with $V\subset\tilde{V}$, such that

 $$ X_{1}\mid V=\frac{\partial}{\partial y_{1}}. $$ 

On V, let

 $$ Y_{1}=X_{1}, $$ 

 $$ Y_{i}=X_{i}-X_{i}(y_{1})X_{1}\qquad(i=2,\ldots,c). $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//8a6047d9-2c8e-4af7-852e-1f5a884593c9/markdown_2/imgs/img_in_image_box_294_558_684_923.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A12Z%2F-1%2F%2F9351e3c936f95b36afc3bdd59dc8879cb30b8e2ae244c82a1b32ac9dec81f28c" alt="Image" width="41%" /></div>


Then the vector fields $Y_{1}, \ldots, Y_{e}$ are independent $C^{\infty}$ vector fields spanning $\mathcal{D}$ in $V$. Let $S$ be the slice $y_{1}=0$, and let

 $$ Z_{i}=Y_{i}\left|S\right.\quad(i=2,\ldots,c). $$ 

Then since (2) and (3) imply that

 $$ Y_{i}(y_{1})=0\qquad(i=2,\ldots,c), $$ 

the $Z_i$ are actually vector fields on $S$; that is, $Z_i(q) \in S_q$ whenever $q \in S$. The $Z_i$ span a smooth $c - 1$ dimensional distribution on $S$.

## 44 Manifolds

We claim this is involutive. Indeed, the $Z_{t}$ are $t$-related (inclusion map of $S$ in $M$) to the $Y_{t}$, and therefore, by 1.55, their Lie brackets are also $t$-related to the corresponding brackets of the $Y_{t}$. But $[Y_{t}, Y_{t}]$, $(i, j \geq 2)$, has no component in the $Y_{t}$ direction (apply to $y_{1}$ and get 0). Therefore, there exist $C^{\infty}$ functions $c_{ijk}$ such that

 $$ [Y_{i},Y_{j}]=\sum_{k=2}^{o}c_{i j k}Y_{k} $$ 

on V, and thus

 $$ [Z_{i},Z_{j}]=\sum_{k=2}^{e}c_{i j k}\bigg|_{S}Z_{k}. $$ 

This proves that the distribution on $S$ is involutive. By the induction hypothesis, there exists a centered coordinate system $w_{s}, \ldots, w_{d}$ on some neighborhood of $m$ in $S$ such that the slices defined by $w_{t} = \text{constant}$ for all $i \in \{c+1, \ldots, d\}$ are precisely the integral manifolds of the distribution spanned by $Z_{s}, \ldots, Z_{t}$ on this neighborhood.

The functions

 $$ \begin{aligned}{}&{{}x_{1}=y_{1},}\\ {}&{{}x_{j}=w_{j}\circ\pi\qquad(j=2,\ldots,d),}\\ \end{aligned} $$ 

where $\pi: V \to S$ is the natural projection in the $y$ coordinate system, are defined on some neighborhood of $m$ in $M$, are independent at $m$, and they all vanish at $m$. Thus there is a cubic-centered coordinate system $(U,\varphi)$ with the coordinate functions $x_{1},\ldots,x_{d}$ on a suitable neighborhood $U$ of $m$. We now prove that

 $$ Y_{t}(x_{o+r})\equiv0\quad\mathrm{o n}~U\qquad(i=1,\ldots,c;~r=1,\ldots,d-c). $$ 

From this it follows that the vector fields $\partial/\partial x_{1},\ldots,\partial/\partial x_{c}$ form a basis for $\mathcal{D}$ at each point of $U$, and thus the slices (1) are integral manifolds of $\mathcal{D}$.

To prove (9), first observe that (8) implies that

 $$ \frac{\partial x_{j}}{\partial y_{1}}=\left\{\begin{aligned}{}&{{}1\quad}&{(j=1)}\\ {}&{{}0\quad}&{(j=2,\ldots,d)}\\ \end{aligned}\right. $$ 

on $U$; and thus (2), (3), and (10) imply that

 $$ Y_{1}=\frac{\partial}{\partial x_{1}}\mathrm{\quad on~}U, $$ 

so certainly (9) holds for $i = 1$. Now let $i \in \{2, \ldots, c\}$ and $r \in \{1, \ldots, d - c\}$. By (11),

 $$ \frac{\partial}{\partial x_{1}}\left(Y_{i}(x_{c+r})\right)=Y_{1}\big(Y_{i}(x_{c+r})\big)=[Y_{1},Y_{i}](x_{c+r}). $$ 

The involutivity of $\mathcal{D}$ implies that there are $C^{\infty}$ functions $c_{ik}$ such that

 $$ [Y_{1},Y_{i}]=\sum_{k=1}^{e}c_{i k}Y_{k}. $$ 

Using (13), (12) becomes

 $$ \frac{\partial}{\partial x_{1}}\left(Y_{i}(x_{e+r})\right)=\sum_{k=2}^{e}c_{i k}Y_{k}(x_{e+r})\quad(i=2,\ldots,c;r=1,\ldots,d-c). $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c4b76db3-fcb4-479b-8e7a-02a05f323e35/markdown_0/imgs/img_in_image_box_173_247_798_592.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A11Z%2F-1%2F%2F7fa55d5e100a1bdc333866b58c24afff47937358d18fb3c17fb7700abb9001ef" alt="Image" width="65%" /></div>


Fix a slice of $U$ of the form $x_{2}=$ constant, ..., $x_{d}=$ constant. On such a slice, $Y_{t}(x_{e+r})$ is a function of $x_{1}$ alone, and (14) becomes a system of $c-1$ homogeneous linear differential equations with respect to $x_{1}$. Such a system has a unique solution with given initial values [11]. Since the system is homogeneous, the 0 functions give a solution. But each such slice has a unique point in $S\cap U$, and on $S\cap U$,

 $$ Y_{i}(x_{c+r})=Z_{i}(w_{c+r})=0\qquad(i=2,\ldots,c). $$ 

The first equality follows from (4) and (8), and the second from the fact that the integral manifolds of the distribution on $S$ determined by the $Z_{t}$ are given by suitable slices in the $w$ coordinate system. It follows from (14) and (15) that the functions $Y_{t}(x_{e+r})$ must be identically zero on $U$. Thus (9) holds, and the induction step is completed.

Finally, suppose that $(N,\psi)$ is a connected integral manifold of $\mathcal{D}$ such that $\psi(N)\subset U$. Let $\pi$ be the projection of $\mathbb{R}^d$ onto the last $d-c$ coordinates. Then vectors in $\mathcal{D}$ are annihilated by $d(\pi\circ\varphi)$. Thus

 $$ d(\pi\circ\varphi\circ\psi)|_{n}\equiv0 $$ 

for each $n \in N$. By $1.24$, $\pi \circ \varphi \circ \psi$ is a constant map since $N$ is connected. Thus $\psi(N)$ is contained in one of the slices (1).

1.61 Remarks The classical version of the Frobenius theorem appears quite different from our version in 1.60. The classical Frobenius theorem can be formulated as follows.

## 46 Manifolds

Let $U$ and $V$ be open sets in $\mathbb{R}^m$ and $\mathbb{R}^n$ respectively. We use coordinates $r_1, \ldots, r_m$ on $\mathbb{R}^m$ and $s_1, \ldots, s_n$ on $\mathbb{R}^n$. Let

 $$ b\colon U\times V\to M(n,m) $$ 

be a $C^{\infty}$ map of $U\times V$ into the set of all $n\times m$ real matrices, and let $(r_{0},s_{0})\in U\times V$. If

 $$ \begin{array}{r l r}&{}&{\frac{\partial b_{i\beta}}{\partial r_{\gamma}}-\frac{\partial b_{i\gamma}}{\partial r_{\beta}}+\displaystyle\sum_{s=1}^{n}\left(\frac{\partial b_{i\beta}}{\partial s_{s}}\;b_{i\gamma}-\frac{\partial b_{i\gamma}}{\partial s_{j}}\;b_{j\beta}\right)=0}\\ &{}&{(i=1,\ldots,n;\gamma,\beta=1,\ldots,m)}\end{array} $$ 

on $U\times V$, then there exist neighborhoods $U_{\theta}$ of $r_{\theta}$ in $U$ and $V_{\theta}$ of $s_{\theta}$ in $V$ and a unique $C^{\infty}$ map

 $$ \alpha\colon U_{\mathfrak{g}}\times V_{\mathfrak{g}}\to V $$ 

such that if

 $$ \alpha_{s}(r)=\alpha(r,s)\qquad(s\in V_{0},\quad r\in U_{0}), $$ 

then

 $$ \alpha_{s}(r_{0})=s, $$ 

 $$ d\alpha_{s}|_{r}=b(r,\alpha(r,s)) $$ 

for all  $ (r,s)\in U_{0}\times V_{0} $

Equation (4) is a so-called total differential equation. We specify in (1) what the differential of a map should be as a function of the graph, and in (2) we have a necessary and sufficient condition for the existence of such a map with the specified initial conditions. It can be shown that this version is equivalent to 1.60. For example, if we start with a c-dimensional, involutive,  $ C^\infty $ distribution  $ \mathcal{D} $ on  $ M^d $ and a point  $ m \in M $, then we can obtain 1.60 from the classical version as follows. We can first choose a coordinate system  $ (W, \tau) $ about  $ m $ with coordinate functions  $ y_1, \ldots, y_d $ and with  $ \tau(W) = U \times V \subset \mathbb{R}^e \times \mathbb{R}^{d-e} $, for which there exist  $ C^\infty $ functions  $ f_{ji} $ on  $ U \times V $ ( $ i = 1, \ldots, c $;  $ j = 1, \ldots, d-c $) such that the vector fields

 $$ Y_{i}=\frac{\partial}{\partial y_{i}}+\sum_{i=1}^{d-c}f_{ji}\circ\tau\frac{\partial}{\partial y_{e+j}}\qquad(i=1,\ldots,c) $$ 

span D on W. Then we define a map b as in (1) by setting

 $$ b(r,s)=\{f_{j i}(r,s)\}. $$ 

It turns out that the involutivity of $\mathcal{D}$ implies that (2) is satisfied, and from the map $\alpha$ one can obtain the desired coordinate system 1.60(1). Conversely, one can obtain the classical version from 1.60 in a similar way.

We shall give in Chapter 2 yet another version of the Frobenius theorem in terms of differential forms and differential ideals.

In 1.32 we considered the situation in which a $C^{\infty}$ map $\psi: N \to M$ factors through a submanifold $(P,\varphi)$ of $M$ so that $\psi = \varphi \circ \psi_{\oplus}$ where $\psi_{\oplus}: N \to P$, and we sought sufficient conditions for $\psi_{\oplus}$ to be $C^{\infty}$. An important case occurs when $(P,\varphi)$ is an integral manifold of an involutive distribution on $M$.

1.62 Theorem Suppose that $\psi: N \to M^d$ is $C^\infty$, that $(P^c, \varphi)$ is an integral manifold of an involutive distribution $\mathcal{D}$ on $M$, and that $\psi$ factors through $(P, \varphi)$, that is, $\psi(N) \subset \varphi(P)$. Let $\psi_0: N \to P$ be the (unique) mapping such that $\varphi \circ \psi_0 = \psi$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c4b76db3-fcb4-479b-8e7a-02a05f323e35/markdown_2/imgs/img_in_image_box_351_351_552_477.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A12Z%2F-1%2F%2F65bce4e560e27b07ba07deebe0a3a442f5f309f4f25091b1d0abc750928ea533" alt="Image" width="21%" /></div>


Then  $ \psi_{0} $ is continuous (and hence  $ C^{\infty} $ by 1.32(a)).

PROOF Let $p$ belong to an open set $U$ in $P$, and let $n\in\psi_0^{-1}(p)$. Using 1.60, we can obtain an open set $\tilde{U}$ with $p\in\tilde{U}\subset U$ and a cubic coordinate system $(V,\tau)$ centered at $\varphi(p)$ with coordinate functions $x_1,\ldots,x_d$ such that the slices

 $$ x_{i}=\mathrm{c o n s t a n t}\qquad\mathrm{f o r~a l l~}i\in\{c+1,\ldots,d\} $$ 

are the integral manifolds of $\mathscr{D}$ in $V$, and such that $\varphi(U)$ is the slice

 $$ x_{c+1}=\cdots=x_{d}=0. $$ 

$\psi^{-1}(V)$ is open in $N$. Let $W$ be the component of $\psi^{-1}(V)$ containing $n$. $W$ is open. To prove that $\psi_0$ is continuous, we need only prove that $\psi_0(W) \subset \tilde{U} \subset U$. By the commutativity of (1) and the injectivity of $\psi$, it suffices to prove that $\psi(W)$ lies in the slice (3) of $V$. Now, $\psi$ is continuous and $W$ connected; hence $\psi(W)$ is connected. Moreover, $\psi(W)$ has at least the point $\psi(n)$ in common with the slice (3). So since $\psi(W)$ lies in a component of $\varphi(P) \cap V$, it is sufficient to prove that components of $\varphi(P) \cap V$ are contained in slices of the form (2).

Let $C$ be a component of $\varphi(P) \cap V$, and let $\pi: V \to \mathbb{R}^{d-c}$ be defined by

 $$ \pi(m)=\left(x_{c+1}(m),\ldots,x_{d}(m)\right). $$ 

Then since $P$ is second countable, and since $\varphi(P) \cap V$ is a union of the slices (2) due to the fact that $(P,\varphi)$ is an integral manifold of $\mathcal{D}$, it follows that $\pi(\varphi(P) \cap V)$ consists of a countable number of points in $\mathbb{R}^{d-c}$. Thus $\pi(C)$ is a connected countable subset of $\mathbb{R}^{d-c}$; hence $\pi(C)$ is a single point, and $C$ lies in a single slice.

1.63 Definition A maximal integral manifold $(N,\psi)$ of a distribution $\mathcal{D}$ on a manifold $M$ is a connected integral manifold of $\mathcal{D}$ whose image in $M$ is not a proper subset of any other connected integral manifold of $\mathcal{D}$. That is, there does not exist a connected integral manifold $(N_1,\psi_1)$ of $\mathcal{D}$ such that $\psi(N)$ is a proper subset of $\psi_1(N_1)$.

1.64 Theorem Let $\mathcal{D}$ be a $c$-dimensional, involutive, $C^{\infty}$ distribution on $M^{d}$. Let $m \in M$. Then through $m$ there passes a unique maximal connected integral manifold of $\mathcal{D}$, and every connected integral manifold of $\mathcal{D}$ through $m$ is contained in the maximal one.

PROOF Existence Let K be the set of all those points p in M for which there is a piecewise smooth curve joining m to p whose smooth portions

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c4b76db3-fcb4-479b-8e7a-02a05f323e35/markdown_3/imgs/img_in_image_box_316_422_604_490.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2Ff390b5a99b89a892ecc325ff1c0b1eb007a94e54e216ea7357f5937ecc6cadea" alt="Image" width="29%" /></div>


<div style="text-align: center;"><div style="text-align: center;">Integral curve of 2</div> </div>


are 1-dimensional integral curves of $\mathcal{D}$, that is, their tangent vectors belong to $\mathcal{D}$. By 1.60 and the second countability of $M$, there is a countable covering of $M$ by cubic coordinate systems $\{(U_{t}, x_{1}^{t}, \ldots, x_{d}^{t}) : i = 0, 1, 2, \ldots\}$ such that the integral manifolds of $\mathcal{D}$ in $U_{t}$ are the slices

 $$ x_{c+s}^{i}=\mathrm{c o n s t a n t}\qquad\mathrm{f o r~a l l~}j\in\{1,\ldots,d-c\}. $$ 

We shall assume that  $ m \in U_{0} $

Now let $p \in K$. Then there exists an index $i$, such that $p \in U_{i_p}$, and there is a slice $S_{i_p}$ of $U_{i_p}$ of the form (1) containing $p$. Observe that $S_{i_p} \subset K$. It follows from 1.60 that the collection of all open subsets of all such $S_{i_p}$ as $p$ runs over $K$ forms a basis for a locally Euclidean topology on $K$, and that we obtain a differentiable structure on $K$ if we take the maximal family of coordinate systems (with respect to 1.4(b)) containing the collection

 $$ \{(S_{i_{p}},\;x_{1}^{i_{p}}\;\big|\;S_{i_{p}},\;\ldots,\;x_{c}^{i_{p}}\;\big|\;S_{i_{p}}):p\in K\}. $$ 

We claim that $K$ with this topology and differentiable structure is a connected differentiable manifold of dimension $c$. $K$ is clearly connected since it is pathwise connected by construction. We have only to prove that the topology on $K$ is second countable. For this, fix an $i\in(0,1,2,\ldots)$. We need only show that there are at most countably many slices of $U_{i}$ in $K$. Each point of $U_{i}$ which lies in $K$ is joinable to $m$ by a piecewise smooth curve whose range also lies in $K$. To each such curve from $m$ to points in $U_{i}$ there corresponds (although not uniquely) a finite sequence

 $$ U_{0},~U_{i_{1}},~\ldots,~U_{i_{n}},~U_{i} $$ 

of the coordinate neighborhoods through which the curve passes in order. The curve thus begins in the slice of U_{t_{0}} containing m, passes through some slice of U_{t_{1}}, then through some slice of U_{t_{2}}, and so on, until in a finite number of steps it reaches a slice in U_{t}. Since there are at most countably many such sequences (3) from U_{t} to U_{t_{1}}, we need only show that for each such sequence there are at most countably many slices of U_{t} reachable in the above manner.  $ \underline{\text{For this,}} $ we need only observe that for any j, k \in (0, 1, \ldots) a single slice of U_{t} can intersect at most countably many slices of U_{k}; for if S is a slice of U_{t_{1}}, then S \cap U_{k} is an open submanifold of S and therefore consists of at most countably many components, each such component being a connected integral manifold of \mathcal{D} in U_{k}, and hence lying in a slice of U_{k}. This proves the second countability of K.

 $ (K,i) $, where  $ i: K \to M $ is the inclusion map, is now a submanifold of  $ M $ and is a connected integral manifold of  $ \mathcal{D} $ passing through  $ m $. Moreover,  $ (K,i) $ is a maximal connected integral manifold of  $ \mathcal{D} $. For let  $ (N,\psi) $ be any connected integral manifold of  $ \mathcal{D} $ passing through  $ m $, and let  $ p \in \psi(N) $. There is a piecewise smooth curve  $ c: [0,1] \to N $ joining  $ \psi^{-1}(m) $ to  $ \psi^{-1}(p) $. (Connected manifolds are pathwise connected.) Then  $ \psi \circ c $ is a piecewise smooth 1-dimensional integral curve of  $ \mathcal{D} $ connecting  $ m $ to  $ p $. Thus  $ p \in K $, and so  $ \psi(N) \subset K $, which proves that  $ K $ is maximal. Thus we have proved the existence of a maximal connected integral manifold  $ (K,i) $ of  $ \mathcal{D} $ passing through  $ m $, and have proved that every connected integral manifold of  $ \mathcal{D} $ through  $ m $ has its image in  $ K $.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//3d509304-d411-4786-813d-cdca1c258207/markdown_0/imgs/img_in_image_box_503_282_816_506.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A12Z%2F-1%2F%2F39c7dd790effcbe5e0ec067865cf2356e1b0b1c32811c437f9a91c4b44525f38" alt="Image" width="32%" /></div>


Uniqueness (cf. 1.33) Let $(N,\psi)$ be any other maximal connected integral manifold of $\mathcal{D}$ passing through $m$. As we have observed above, $\psi(N) \subset K$; thus $\psi$ factors as follows:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//3d509304-d411-4786-813d-cdca1c258207/markdown_0/imgs/img_in_image_box_336_889_529_1014.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A12Z%2F-1%2F%2Fdd7273880c8ad5e48826cb17e4963bbfe9213877438dae6c14876bf890b2c49d" alt="Image" width="20%" /></div>


$\psi_{0}$ is $C^{\infty}$ by 1.62, and is 1:1 and non-singular since $\psi$ is 1:1 and non-singular. $\psi_{0}$ is onto since the fact that $(N,\psi)$ is a maximal integral manifold of $\mathcal{D}$ through $m$ implies that $\psi(N)$ cannot be a proper subset of $K$. It follows from Corollary (a) of 1.30 that $\psi_{0}$ is a diffeomorphism. Thus $(N,\psi)$ and $(K,i)$ are equivalent, and the maximal connected integral manifold of $\mathcal{D}$ through $m$ is unique.

##### EXERCISES

1 Prove that in Example 1.5(d) one does indeed obtain a differentiable structure on  $ S^{d} $.

2 The usual differentiable structure on the real line $\mathbb{R}$ was obtained by taking $\mathcal{F}$ to be the maximal collection containing the identity map. Let $\mathcal{F}_1$ be the maximal collection (with respect to $1.4(b)$ containing the map $t \mapsto t^2$. Prove that $\mathcal{F} \neq \mathcal{F}_1$, but that $(\mathbb{R},\mathcal{F})$ and $(\mathbb{R},\mathcal{F}_1)$ are diffeomorphic.

3 Let $\{U_{\alpha}\}$ be an open cover of a manifold $M$. Prove that there exists a refinement $\{V_{\alpha}\}$ such that $\overline{V}_{\alpha} \subset U_{\alpha}$ for each $\alpha$.

4 Use the fact that manifolds are regular and paracompact to prove that manifolds are normal topological spaces.

5 Prove 1.25(a), (b), and (c).

6 Prove that if $\psi: M \to N$ is $C^{\infty}$, one-to-one, onto, and everywhere non-singular, then $\psi$ is a diffeomorphism. (This proposition depends strongly on the second countability of $M$. Here is an outline for a proof. This map $\psi$ is a diffeomorphism if and only if $d\psi$ is surjective everywhere. If $d\psi$ is not surjective at some point, then the dimension of $M$ is less than the dimension of $N$. Let $\dim M = p$ and $\dim N = d$. Assuming that $p < d$, one arrives at a contradiction as follows. Let $(U,\varphi)$ be a coordinate system on $N$ such that $\varphi(U) = \mathbb{R}^d$. Since $\psi$ maps $M$ onto $N$, the range of $\varphi \circ \psi$ is all of $\mathbb{R}^d$. Now we show that this yields a contradiction. One way is to use 1.35 to observe that the range of $\varphi \circ \psi$ is a countable union of nowhere dense sets in $\mathbb{R}^d$, and therefore, by the Baire category theorem, could not possibly be all of $\mathbb{R}^d$. Another way is to use the fact that $p < d$ to prove that the range of $\varphi \circ \psi$ has measure 0 in $\mathbb{R}^d$, which also is a contradiction (where a set in $\mathbb{R}^d$ has measure 0 if it can be covered by a sequence of balls, the union of whose volumes is arbitrarily small). That the range of $\varphi \circ \psi$ has measure 0 in $\mathbb{R}^d$ follows from the second countability of $M$ and the fact that a $C^1$ map $\mathbb{R}^d \to \mathbb{R}^d$ has image of measure 0, and this, in turn, follows from the fact that a $C^1$ map $\mathbb{R}^d \to \mathbb{R}^d$ takes sets of measure 0 to sets of measure 0. To prove the latter, observe that if $f: \mathbb{R}^d \to \mathbb{R}^d$ is $C^1$, and if $A$ is a compact set in $\mathbb{R}^d$, then $f$ has a Lipschitz constant $K$ on $A$,

 $$ \|f(x)-f(y)\|\leq K\|x-y\|\quad(x,y\in A), $$ 

so that $f$ magnifies the volume of balls in $A$ by at most $K^{d}$, and hence takes sets of measure 0 in $A$ into sets of measure 0.)

7 Prove 1.33(a) and (b).

8 Obtain the classical implicit function theorem 1.37 from 1.38.

9 Let  $ f\colon \mathbb{R}^2 \to \mathbb{R} $ be defined by.

 $$ f(x,y)=x^{3}+x y+y^{3}+1. $$ 

For which points $p = (0,0)$, $p = (\tfrac{1}{3},\tfrac{1}{3})$, $p = (-\tfrac{1}{3},-\tfrac{1}{3})$ is $f^{-1}(f(p))$ an imbedded submanifold in $\mathbb{R}^2$?

10 Let $M$ be a compact manifold of dimension $n$, and let $f: M \to \mathbb{R}^n$ be $C^\infty$. Prove that $f$ cannot everywhere be non-singular.

11 Find counterexamples to show that Proposition 1.36 would fail if either of the hypotheses closed or imbedded were deleted. In fact, one can prove more; namely, if $(M,\psi)$ is a submanifold of $N$ such that whenever $g\in C^\infty(M)$ there is a $C^\infty$ function $f$ on $N$ such that $f\circ\psi=g$, then $\psi$ is an imbedding and $\psi(M)$ is closed in $N$.

12 Supply the details for 1.40(a) and (b).

13 Prove Proposition 1.45.

14 Is every vector field on the real line complete?

15 Prove that if $(U, x_1, \ldots, x_d)$ is a coordinate system on $M$, then $[\partial/\partial x_i, \partial/\partial x_j] = 0$ on $U$.

16 Let $N \subset M$ be a submanifold. Let $\gamma: (a,b) \to M$ be a $C^\infty$ curve such that $\gamma(a,b) \subset N$. Show that it is not necessarily true that $\dot{\gamma}(t) \in N_{\gamma(t)}$ for each $t \in (a,b)$.

17 Prove that any $C^{\infty}$ vector field on a compact manifold is complete.

18 Prove that a $C^{\infty}$ map $f\colon \mathbb{R}^{8} \to \mathbb{R}^{1}$ cannot be one-to-one.

19 Supply the details of the equivalence of the two versions 1.60 and 1.61 of the Frobenius theorem.

20 Let $\varphi: N \to M$ be $C^\infty$, and let $X$ be a $C^\infty$ vector field on $N$. Suppose that $d\varphi(X(p)) = d\varphi(X(q))$ whenever $\varphi(p) = \varphi(q)$. Is there a smooth vector field $Y$ on $M$ which is $\varphi$-related to $X?$

21 The torus is the manifold $S^{1} \times S^{1}$. Consider $S^{1}$ as the unit circle in the complex plane. We define a mapping $\varphi: \mathbb{R} \to S^{1} \times S^{1}$ by setting $\varphi(t) = (e^{\mathfrak{z}_{\pi i t}}, e^{\mathfrak{z}_{\pi i a t}})$ where $\alpha$ is an irrational number. Prove that $(\mathbb{R}, \varphi)$ is a dense submanifold of $S^{1} \times S^{1}$. This submanifold is known as the skew line on the torus.

22 Let $\gamma(t)$ be an integral curve of a vector field $X$ on $M$. Suppose that $\dot{\gamma}(t)=0$ for some $t$. Prove that $\gamma$ is a constant map, that is, its range consists of one point.

23 A Riemannian structure on a differentiable manifold M is a smooth choice of a positive definite inner product  $ \langle\cdot,\rangle_{m} $ on each tangent space  $ M_{m} $, smooth in the sense that whenever X and Y are  $ C^{\infty} $ vector fields on M, then  $ \langle X,Y\rangle $ is a  $ C^{\infty} $ function on M. Prove that there exists a Riemannian structure on every differentiable manifold. You will need to use a partition of unity argument. A Riemannian manifold is a differentiable manifold together with a Riemannian structure.

24 Consider the product manifold  $ M \times N $ with the canonical projections  $ \pi_1: M \times N \to M $ and  $ \pi_8: M \times N \to N $.

(a) Prove that  $ \alpha\colon \tilde{M} \to M \times N $ is  $ C^\infty $ if and only if  $ \pi_1 \circ \alpha $ and  $ \pi_2 \circ \alpha $ are  $ C^\infty $.

(b) Prove that the map $v \mapsto (d\pi_{1}(v), d\pi_{2}(v))$ is an isomorphism of $(M \times N)_{(m,n)}$ with $M_{m} \oplus N_{n}$.

(c) Let $X$ and $Y$ be $C^{\infty}$ vector fields on $M$ and $N$ respectively. Then, by (b), $X$ and $Y$ canonically determine vector fields $\tilde{X} = (X,0)$ and $\tilde{Y} = (0,Y)$ on $M \times N$. Prove that $[X, \tilde{Y}] = 0$.

(d) Let  $ (m_{0}, n_{0}) \in M \times N $, and define injections  $ i_{n_{0}}: M \to M \times N $ and  $ i_{m_{0}}: N \to M \times N $ by setting

 $$ \begin{aligned}{}&{{}i_{n_{0}}(m)=(m,n_{0}),}\\ {}&{{}i_{m_{0}}(n)=(m_{0},n).}\\ \end{aligned} $$ 

Let  $ v \in (M \times N)_{(m_0, n_0)} $, and let  $ v_1 = d\pi_1(v) \in M_{m_0} $ and  $ v_2 = d\pi_2(v) \in N_{m_0} $. Let  $ f \in C^\infty(M \times N) $. Prove that

 $$ v(f)=v_{1}(f\circ i_{n_{0}})+v_{1}(f\circ i_{m_{0}}). $$ 

TENSORS

and DIFFERENTIAL

FORMS

There are a number of vector spaces and algebras naturally associated with the tangent space  $ M_{m} $. Suitably smooth assignments of elements of these spaces to the points in M yield tensor fields and differential forms of various types. We shall first develop some of the pertinent facts from multilinear algebra, and then beginning with 2.14 we shall apply these concepts to manifolds.

##### TENSOR AND EXTERIOR ALGEBRAS

Throughout 2.1–2.13, $V$, $W$, and $U$ will denote finite dimensional real vector spaces. As usual, $V^{*}$ will denote the dual space of $V$ consisting of all real-valued linear functions on $V$.

2.1 Definitions Let $F(V,W)$ be the free vector space over $\mathbb{R}$ whose generators are the points of $V \times W$. Thus $F(V,W)$ consists of all finite linear combinations of pairs $(v,w)$ with $v \in V$ and $w \in W$. Let $R(V,W)$ be the subspace of $F(V,W)$ generated by the set of all elements of $F(V,W)$ of the following forms:

 $$ \begin{array}{l}{(v_{1}+v_{2},w)-(v_{1},w)-(v_{2},w)}\\ {(v,w_{1}+w_{2})-(v,w_{1})-(v,w_{2})}\\ {(a v,w)-a(v,w)}\\ {(v,a w)-a(v,w)}\\ \end{array}\left(\begin{array}{c}{a\in\mathbb{R}}\\ {v,v_{1},v_{2}\in V}\\ {w,w_{1},w_{2}\in W}\\ \end{array}\right). $$ 

The quotient space $F(V,W)/R(V,W)$ is called the tensor product of $V$ and $W$ and is denoted by $V\otimes W$. The coset of $V\otimes W$ containing the element $(v,w)$ of $F(V,W)$ is denoted by $v\otimes w$. It follows from (1) that we have the following identities in $V\otimes W$:

 $$ \begin{aligned}{(v_{1}+v_{\mathbf{z}})\otimes w}&{{}=v_{1}\otimes w+v_{\mathbf{z}}\otimes w}\\ {v\otimes(w_{1}+w_{\mathbf{z}})}&{{}=v\otimes w_{1}+v\otimes w_{\mathbf{z}}}\\ {a(v\otimes w)}&{{}=a v\otimes w=v\otimes a w.}\\ \end{aligned} $$ 

2.2 The following properties of the tensor product are easily established, and are left to the reader as exercises.

(a) Universal Mapping Property. Let $\varphi$ denote the bilinear map $(v,w)\mapsto$ $v\otimes w$ of $V\times W$ into $V\otimes W$. Then whenever $U$ is a vector space and $l:V\times W\to U$ is a bilinear map, there exists a unique linear map $\tilde{l}\colon V\otimes W\to U$ such that the following diagram commutes:

(1)

The pair consisting of $V\otimes W$ and $\varphi$ is said to solve the universal mapping problem for bilinear maps with domain $V\times W$. Moreover, $V\otimes W$ and $\varphi$ are unique with this property in the sense that if $X$ is a vector space and $\tilde{\varphi}:V\times W\to X$ a bilinear map with the above universal mapping property, then there exists an isomorphism $\alpha:V\otimes W\to X$ such that $\alpha\circ\varphi=\tilde{\varphi}$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//30cc24cd-0f69-41af-9c7f-2bd7289ef894/markdown_2/imgs/img_in_image_box_398_276_648_398.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A22Z%2F-1%2F%2F01e0f40d87795dd38791e6a376af86c651cf1f71808cd3fda8b31b3e2b79f2fc" alt="Image" width="26%" /></div>


(b)  $ V \otimes W $ is canonically isomorphic with  $ W \otimes V $.

(c)  $ V \otimes (W \otimes U) $ is canonically isomorphic with  $ (V \otimes W) \otimes U $.

(d) By property (a), the bilinear map of $V^{*}\times W$ into the vector space $\mathrm{Hom}(V,W)$ of linear transformations from $V$ to $W$ defined by $(f,w)(v)=f(v)\cdot w$ for $f\in V^{*}$, $v\in V$, and $w\in W$ determines uniquely a linear map $\alpha\colon V^{*}\otimes W\to\mathrm{Hom}(V,W)$. $\alpha$ is an isomorphism. As a consequence,

(2)

 $$ \dim V\otimes W=(\dim V)(\dim W). $$ 

(e) Let $\{e_i: i = 1, \ldots, c\}$ and $\{f_i: j = 1, \ldots, d\}$ be bases for $V$ and $W$ respectively. Then $\{e_i \otimes f_i: i = 1, \ldots, c$ and $j = 1, \ldots, d\}$ is a basis of $V \otimes W$.

2.3 Definitions The tensor space $V_{r,s}$ of type $(r,s)$ associated with $V$ is the vector space

(1)

 $$ \underbrace{V\otimes\cdots\otimes V}_{{~\mathfrak{r}~c o p l e s}}\otimes\underbrace{V^{*}\otimes\cdots\otimes V^{*}}_{{~s~c o p l e s}}. $$ 

The direct sum

(2)

 $$ T(V)=\sum V_{r,s}\qquad(r,s\geq0), $$ 

where  $ V_{0,0} = \mathbb{R} $, is called the tensor algebra of  $ V $. Elements of  $ T(V) $ are finite linear combinations over  $ \mathbb{R} $ of elements of the various  $ V_{r,s} $ and are called tensors.  $ T(V) $ is a non-commutative, associative, graded algebra under  $ \otimes $ multiplication, where if  $ u = u_1 \otimes \cdots \otimes u_{r_1} \otimes u_1^* \otimes \cdots \otimes u_{s_1^*} $ belongs to  $ V_{r_1,s_1} $ and  $ v = v_1 \otimes \cdots \otimes v_{r_2} \otimes v_1^* \otimes \cdots \otimes v_{s_2^*} $ belongs to  $ V_{r_2,s_2} $.

##### Tensors and Differential Forms

then their product  $ u \otimes v $ is defined by

 $$ u\otimes v=u_{1}\otimes\cdots\otimes u_{r_{1}}\otimes v_{1}\otimes\cdots\otimes v_{r_{8}}\otimes u_{1}^{*}\otimes\cdots\otimes u_{s_{1}}^{*}\otimes v_{1}^{*}\otimes\cdots\otimes v_{s_{8}}^{*} $$ 

and belongs to $V_{r_{1}+r_{2},s_{1}+s_{2}}$. Tensors in a particular tensor space $V_{r,s}$ are called homogeneous of degree $(r,s)$. A homogeneous tensor (of degree $(r,s)$, say) is called decomposable if it can be written in the form

 $$ v_{1}\otimes\cdots\otimes v_{r}\otimes v_{1}^{*}\otimes\cdots\otimes v_{s}^{*} $$ 

where  $ v_i \in V $  $ (i = 1, \ldots, r) $ and  $ v_j^* \in V^* $  $ (j = 1, \ldots, s) $.

2.4 Definitions We let $C(V)$ denote the subalgebra $\sum_{k=0}^{\infty} V_{k,0}$ of $T(V)$. Let $I(V)$ be the two-sided ideal in $C(V)$ generated by the set of elements of the form $v\otimes v$ for $v\in V$, and set

 $$ I_{k}(V)=I(V)\cap V_{k,0}. $$ 

It follows that

 $$ \begin{array}{r}{I(V)=\displaystyle\sum_{k=0}^{\infty}I_{k}(V),}\end{array} $$ 

and is a graded ideal in $C(V)$. The exterior algebra $\Lambda(V)$ of $V$ is the graded algebra $C(V)/I(V)$. If we set

 $$ \Lambda_{k}(V)=V_{k,0}/I_{k}(V)\qquad(k\geq2),\qquad\Lambda_{0}(V)=\mathbb{R},\qquad\Lambda_{1}(V)=V, $$ 

then

 $$ \Lambda(V)=\sum_{k=0}^{\infty}\Lambda_{k}(V). $$ 

We shall denote multiplication in the algebra $\Lambda(V)$ by $\wedge$. This is called the wedge or exterior product. In particular, the residue class containing $v_1\otimes\cdots\otimes v_k$ is $v_1\wedge\cdots\wedge v_k$.

### 2.5 Definition A multilinear map

 $$ h\colon\underbrace{V\times\cdots\times}_{r\mathrm{~c o p l e s}}\underset{}{V}{\to}W $$ 

is called alternating if

 $$ (2)\quad h(v_{\pi(1)},\ldots,v_{\pi(r)})=(\operatorname{s g n}\pi)h(v_{1},\ldots,v_{r})\qquad(v_{1},\ldots,v_{r}\in V), $$ 

for all permutations $\pi$ in the permutation group $S_{r}$ on $r$ letters. Sgn $\pi$ is the sign of the permutation $\pi$ (+1 if $\pi$ is even, -1 if $\pi$ is odd). The vector space of all alternating multilinear functions

 $$ \underbrace{V\times\cdots\times}_{r{~c o p l e s}}V\to\mathbb{R} $$ 

will be denoted by  $ A_r(V) $, and for convenience we set  $ A_0(V) = \mathbb{R} $.

2.6 The following properties of the exterior algebra are left to the reader as exercises:

(a)  $ \operatorname*{If} u \in \Lambda_k(V) $ and  $ v \in \Lambda_l(V) $, then  $ u \land v \in \Lambda_{k+l}(V) $ and  $ u \land v = (-1)^{kl} v \land u $.

(b) If  $ e_{1}, \ldots, e_{d} $ is a basis of V, then

(1)

 $$ \{e_{\bullet}\} $$ 

is a basis of $\Lambda(V)$, where $\Phi$ runs over all subsets of $\{1, \ldots, d\}$, including the empty set; where $e_{\Phi} = e_{i_1} \wedge \cdots \wedge e_{i_r}$ with $i_1 < \cdots < i_r$ when $\Phi$ is the subset $\{i_1, \ldots, i_r\}$ of $\{1, \ldots, d\}$; and where $e_{\Phi} = 1$ when $\Phi = \varnothing$. In particular,

 $$ \Lambda_{d}(V)\cong\mathbb{R}, $$ 

 $$ \Lambda_{d+j}(V)=\{0\}\qquad(j>0). $$ 

Moreover, it follows that

 $$ \dim\Lambda(V)=2^{d}, $$ 

 $$ \operatorname{d i m}\Lambda_{k}(V)=\binom{d}{k}=\frac{d!}{k!(d-k)!}\qquad(0\leq k\leq d). $$ 

(Hint: Observe that the elements $\{e_\oplus\}$ span $\Lambda(V)$. To prove that they also are linearly independent, first prove that $e_1 \wedge \cdots \wedge e_d$ is not zero in $\Lambda_d(V)$. For this, one must show that $e_1 \otimes \cdots \otimes e_d$ does not belong to $I(V)$. Express an arbitrary element of $I(V)$ in terms of the basis vectors $e_1, \ldots, e_d$, and show that it could not equal $e_1 \otimes \cdots \otimes e_d$. Then for linear independence of the entire set $\{e_\oplus\}$, multiply the equation $\sum a_e e_\oplus = 0$ by suitable products of the $e_i$ to land in $\Lambda_d(V)$, and conclude that the various $a_\oplus$ are all zero.)

(c) Universal Mapping Property. Let $\varphi$ denote the mapping $(v_1, \ldots, v_k) \mapsto v_1 \wedge \cdots \wedge v_k$ of $V \times \cdots \times V$ ($k$ copies) into $\Lambda_k(V)$. Then $\varphi$ is an alternating multilinear map. Now to each alternating multilinear map $h$ of $V \times \cdots \times V$ ($k$ copies) into a vector space $W$, there corresponds uniquely a linear map $\tilde{h}$: $\Lambda_k(V) \to W$ such that $\tilde{h} \circ \varphi = h$.

<div style="text-align: center;"><div style="text-align: center;">(4)</div> </div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//764f1c39-5dae-4487-9d53-1dbc2ff8fe13/markdown_0/imgs/img_in_image_box_308_891_612_1039.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A26Z%2F-1%2F%2Fa0d917652e553ebd69f628d6f0ec3815e29721e1f2b6194f78a1d2c210657e34" alt="Image" width="31%" /></div>


The pair consisting of $\Lambda_{k}(V)$ and $\varphi$ is said to solve the universal mapping problem for alternating multilinear maps with domain $V\times\cdots\times V$; and this is the unique solution in the sense that if $X$ is a vector space and $\tilde{\varphi}\colon V\times\cdots\times V\to X$ an alternating multilinear map also possessing the universal mapping property for alternating multilinear maps

with domain  $ V \times \cdots \times V $, then there is an isomorphism  $ \alpha\colon \Lambda_k(V) \to X $ such that  $ \alpha \circ \varphi = \widetilde{\varphi} $.

In the special case in which  $ W = \mathbb{R} $, the diagram (4) establishes a natural isomorphism

 $$ \Lambda_{k}(V)^{*}\cong A_{k}(V) $$ 

of $\Lambda(V_k)$* with the vector space $A_k(V)$ of all alternating multilinear functions on $V\times\cdots\times V$ (k copies). It follows from property (b) that $A_k(V)=\{0\}$ for $k>\dim V$.

We shall now consider various dualities between the spaces $V_{r,s}$, $\Lambda_{k}(V)$, $\Lambda(V)$ and the corresponding spaces $(V^{*})_{r,s}$, $\Lambda_{k}(V^{*})$, $\Lambda(V^{*})$ built on the dual space $V^{*}$ of $V$.

2.7 Definition Let $V$ and $W$ be real finite dimensional vector spaces. A pairing of $V$ and $W$ is a bilinear map ($, $): $V $\times$ $W \to \mathbb{R}$. A pairing is called non-singular if whenever $w \neq 0$ in $W$, there exists an element $v \in V$ such that $(v, w) \neq 0$, and whenever $v \neq 0$ in $V$, there exists an element $w \in W$ such that $(v, w) \neq 0$.

Let V and W be non-singularly paired by (, ), and define

 $$ \varphi\colon V\to W^{*}\quad\mathtt{b y}\quad\varphi(v)(w)=(v,w)\qquad(v\in V;~w\in W). $$ 

It follows that $\varphi$ is $1:1$. Similarly, there is a $1:1$ map $W \to V^{*}$. Therefore $V$ and $W$ have the same dimension, and hence $\varphi$ is an isomorphism of $V$ with $W^{*}$. Thus a non-singular pairing of $V$ and $W$ in a canonical way yields an isomorphism $\varphi: V \to W^{*}$ and similarly an isomorphism $W \to V^{*}$.

2.8 Definition A non-singular pairing of $(V^{*})_{r,s}$ with $V_{r,s}$. This pairing is to be the bilinear map $(V^{*})_{r,s} \times V_{r,s} \to \mathbb{R}$ which on decomposable elements

 $$ v^{*}=v_{1}^{*}\otimes\cdots\otimes v_{r}^{*}\otimes u_{r+1}\otimes\cdots\otimes u_{r+s}\in(V^{*})_{r,s} $$ 

and

 $$ u=u_{1}\otimes\cdots\otimes u_{r}\otimes v_{r+1}^{*}\otimes\cdots\otimes v_{r+s}^{*}\in V_{r,s} $$ 

yields the following:

 $$ (v^{*},u)=v_{1}^{*}(u_{1})\cdot\cdot\cdot v_{r+s}^{*}(u_{r+s}). $$ 

It is easily checked that there is a unique such bilinear map and that it is a non-singular pairing. This pairing establishes an isomorphism

 $$ (V^{*})_{r,s}\cong(V_{r,s})^{*}. $$ 

On the other hand, the obvious extension of the universal mapping property 2.2(a) shows that there is a natural isomorphism

 $$ (V_{\tau,8})^{*}\cong M_{\tau,8}(V) $$ 

where $M_{r,s}(V)$ is the vector space of all multilinear functions

 $$ \underbrace{V\times\cdots\times}_{{~r~o o p i e s}}V\times\underbrace{V^{*}\times\cdots\times}_{{~s~c o p i e s}}V^{*}\to\mathbb{R}. $$ 

Under the isomorphism (3), if $\tilde{h} \in (V_{\varphi,s})^{*}$, then the corresponding multi-linear function $h$ in $M_{\varphi,s}(V)$ satisfies

 $$ h(v_{1},\ldots,v_{r},v_{1}^{*},\ldots,v_{s}^{*})=\tilde{h}(v_{1}\otimes\cdots\otimes v_{r}\otimes v_{1}^{*}\otimes\cdots\otimes v_{s}^{*}). $$ 

Finally, from (2) and (3) we obtain an isomorphism

 $$ (V^{*})_{r,s}\cong M_{r,s}(V). $$ 

2.9 Definition A non-singular pairing of $\Lambda_k(V^*)$ with $\Lambda_k(V)$. This pairing is to be the bilinear map of $\Lambda_k(V^*) \times \Lambda_k(V) \to \mathbb{R}$ which on decomposable elements $v^* = v_1^* \wedge \cdots \wedge v_k^*$ in $\Lambda_k(V^*)$ and $u = u_1 \wedge \cdots \wedge u_k$ in $\Lambda_k(V)$ yields

Again it is easily checked that there is a unique such bilinear map and that it is a non-singular pairing. For $k=0$, the pairing is simply multiplication of real numbers. This pairing establishes an isomorphism

 $$ (v^{*},u)=\det\big(v_{i}^{*}(u_{j})\big). $$ 

 $$ \Lambda_{k}(V^{*})\cong\Lambda_{k}(V)^{*}. $$ 

Composing (2) with the natural isomorphism

 $$ \Lambda_{k}(V)^{*}\cong A_{k}(V) $$ 

of 2.6(5) yields an isomorphism

 $$ \Lambda_{k}(V^{*})\cong A_{k}(V). $$ 

Using the isomorphism (2), and observing that the dual space of a finite direct sum is canonically isomorphic to the direct sum of the dual spaces, we obtain isomorphism

 $$ \hat{\Lambda}(V^{*})=\sum_{k=0}^{\infty}\Lambda_{k}(V^{*})\cong\sum_{k=0}^{\infty}\Lambda_{k}(V)^{*}\cong\Lambda(V)^{*}, $$ 

and from (3) we obtain an isomorphism

 $$ \Lambda(V)^{*}\cong A(V)=\sum_{k=0}^{\infty}A_{k}(V). $$ 

Henceforth we shall make use of the identification (5) of $\Lambda(V^{*})$ with $\Lambda(V)^{*}$ via the pairing (1) without further comment.

### 2.10 Remarks on 2.9

(a) If $\{e_1, \ldots, e_d\}$ is a basis of $V$ with dual basis $\{\gamma_1, \ldots, \gamma_d\}$ in $V^*$, then the bases $\{e_\oplus\}$ and $\{\gamma_\oplus\}$ defined in 2.6(b) are dual bases of $\Lambda(V)$ and $\Lambda(V^*)$ under the isomorphism 2.9(5).

(b) In 2.9(5) and (6), the following isomorphismswere established:

 $$ \Lambda(V^{*})\cong\Lambda(V)^{*}\cong A(V). $$ 

The second of these is the natural isomorphism arising from the universal mapping property 2.6(c). The first, call it $\alpha$ for the moment, arose from our choice of the pairing 2.9(1). There is another pairing in common use, this one obtained by replacing 2.9(1) by

 $$ (v^{*},u)=\frac{1}{k!}\operatorname*{d e t}\bigl(v_{i}^{*}(u_{j})\bigr). $$ 

This pairing gives a different isomorphism of $\Lambda(V^*)$ with $\Lambda(V)^*,$ call it $\beta$. Now $\Lambda(V^*)$ is an algebra under wedge multiplication. Via the above isomorphism we obtain two algebra structures $\wedge_a$ and $\wedge_\beta$ on $A(V)$. It is not difficult to see that if $f\in A_p(V)$ and $g\in A_q(V)$, then these induced algebra structures on $A(V)$ take the form

 $$ \begin{aligned}{f}&{{}\wedge_{a}g(v_{1},\ldots,v_{p+q})}\\ {}&{{}=\sum_{p,q{s h u f f i e s}}(\operatorname{s g n}\pi)f(v_{s(1)},\ldots,v_{s(p)})g(v_{s(p+1)},\ldots,v_{s(\frac{p+q}{\cdot})})}\\ \end{aligned} $$ 

and

(3)

 $$ \begin{aligned}{f}&{{}\wedge_{\beta}g(v_{1},\ldots,v_{p+q})}\\ {}&{{}=\frac{1}{(p+q)!}\sum_{\pi\pi S_{p+q}}(\operatorname{s g n}\pi)f(v_{\pi(1)},\ldots,v_{\pi(p)})g(v_{\pi(p+1)},\ldots,v_{\pi(p+q)}).}\\ \end{aligned} $$ 

Here a permutation  $ \pi \in S_{p+q} $ is called a "p, q shuffle" if  $ \pi(1) < \pi(2) < \cdots < \pi(p) $ and  $ \pi(p+1) < \cdots < \pi(p+q) $. It follows from (2) and (3) that

 $$ f\wedge_{\alpha}g=\frac{(p+q)!}{p!q!}f\wedge_{\beta}g. $$ 

For example, consider the case in which $p = q = 1$. Let $\gamma$ and $\delta$ belong to $V^* = A_1(V)$, and let $v, w \in V$. Then $\gamma \wedge_\alpha \delta$ and $\gamma \wedge_\beta \delta \in A_2(V)$ and

 $$ \gamma\wedge_{\alpha}\delta(v,w)=\gamma(v)\delta(w)-\gamma(w)\delta(v), $$ 

whereas

 $$ \gamma\wedge_{\beta}\delta\left(v,w\right)=\tfrac{1}{2}\big(\gamma(v)\,\delta(w)-\gamma(w)\,\delta(v)\big). $$ 

We shall use only the pairing 2.9(1). It has the advantage of avoiding factors such as the $\frac{1}{2}$ in (6).

2.11 Linear Transformations of $\Lambda(V)$ End$(\Lambda(V))$ will denote the vector space of all endomorphisms of $\Lambda(V)$ (i.e. linear transformations from $\Lambda(V)$ into $\Lambda(V)$). Let $u \in \Lambda(V)$. Left multiplication by $u$ is the endomorphism $e(u)$ of $\Lambda(V)$ defined by

 $$ e(u)v=u\land v\qquad(v\in\Lambda(V)). $$ 

The transpose $i(u)$ of $\varepsilon(u)$ is an endomorphism of $\Lambda(V)^{*}$. Under our identification of $\Lambda(V)^{*}$ with $\Lambda(V^{*})$, the transpose $i(u)$ can be considered as an endomorphism of $\Lambda(V^{*})$, and this endomorphism is called interior multiplication by $u$. In terms of our pairing of $\Lambda(V)$ with $\Lambda(V^{*})$, $i(u)$ is defined by

 $$ (2)\quad\big(i(u)v^{*},w\big)=\big(v^{*},\varepsilon(u)w\big)=(v^{*},u\land w)\qquad\big(v^{*}\in\Lambda(V^{*});w\in\Lambda(V)\big). $$ 

If $u \in V$, then $i(u)$ maps $\Lambda_k(V^*)$ into $\Lambda_{k-1}(V^*)$ for each $k$. In particular, if $v^* \in V^*$, then $i(u)v^* \in \mathbb{R}$ and

 $$ i(u)v^{*}=\left(i(u)v^{*},1\right)=\left(v^{*},\varepsilon(u)\cdot1\right)=(v^{*},u)=v^{*}(u). $$ 

An endomorphism $l$ of $\Lambda(V)$ (or in general of any graded algebra) is

(a) a derivation if $l(u \land v) = l(u) \land v + u \land l(v)$ $\quad (u, v \in \Lambda(V))$,

(b) an anti-derivation if $l(u \land v) = l(u) \land v + (-1)^u u \land l(v)$

$(u \in \Lambda_p(V); v \in \Lambda(V))$,

(c) of degree k if  $ l\colon \Lambda_{j}(V) \to \Lambda_{j+k}(V) $ for all j.

(We assume that  $ \Lambda_{i}(V) = \{0\} $ if  $ i < 0 $.)

It is easy to see that  $ l \in \text{End} \Lambda(V) $ is an anti-derivation if and only if on decomposable elements we have

 $$ l(v_{1}\wedge\cdots\wedge v_{j})=\sum_{i=1}^{s}(-1)^{i+1}v_{1}\wedge\cdots\wedge l(v_{i})\wedge\cdots\wedge v_{j}. $$ 

2.12 Proposition If $u \in V$, then $i(u)$ is an anti-derivation of degree -1.

PROOF That the degree of $i(u)$ is $-1$ if $u \in V$ is clear from the definition 2.11(2). To prove that $i(u)$ is an anti-derivation, we check that 2.11(3) holds. For this, it is sufficient to see that both sides of 2.11(3) give the same result when paired with an element of $\Lambda(V)$ of the form $w_{2} \wedge \cdots \wedge w_{j}$. That is, we must show that

 $$ \begin{aligned}{}&{{}\left(i(u)(v_{1}^{*}\wedge\cdots\wedge v_{j}^{*}),w_{2}\wedge\cdots\wedge w_{j}\right)}\\ {}&{{}\qquad=\left(\sum_{i=1}^{j}(-1)^{i+1}v_{1}^{*}\wedge\cdots\wedge i(u)v_{i}^{*}\wedge\cdots\wedge v_{j}^{*},w_{2}\wedge\cdots\wedge w_{j}\right).}\\ \end{aligned} $$ 

## 62. Tensors and Differential Forms

Now, the left-hand side of (1) equals

 $$ (v_{1}^{*}\wedge\cdots\wedge v_{j}^{*},u\wedge w_{2}\wedge\cdots\wedge w_{j})=\operatorname*{d e t}(v_{i}^{*}(w_{l})), $$ 

where we have put  $ w_{1}=u $. The right-hand side of (1) is

 $$ \begin{align*}\sum_{i=1}^{j}(-1)^{i+1}v_{i}^{*}(u)&(v_{1}^{*}\wedge\cdots\wedge\widehat{v_{i}^{*}}\wedge\cdots v_{j}^{*},w_{2}\wedge\cdots\wedge w_{j})\\&=\sum_{i=1}^{j}(-1)^{i+1}v_{i}^{*}(u)\det\big(v_{k}^{*}(w_{i})\big)\quad\begin{pmatrix}k=1,\ldots,\widehat{i},\ldots,j\\ l=2,\ldots,j\end{pmatrix}\\&=\det\big(v_{i}^{*}(w_{i})\big)\quad\begin{pmatrix}i=1,\ldots,j\\ l=1,\ldots,j\end{pmatrix}.\end{align*} $$ 

2.13 Effect of Linear Transformations Let $l: V \to W$ be a linear transformation. Then $l$ extends to an algebra homomorphism

(Here the circumflex over a term means that it is to be omitted.)

 $$ l\colon\Lambda(V)\to\Lambda(W), $$ 

where

 $$ l(v_{1}\wedge\cdot\cdot\cdot\wedge v_{k})=l(v_{1})\wedge\cdot\cdot\cdot\wedge l(v_{k})\quad\mathrm{a n d}\quad l(1)=1. $$ 

The transpose  $ \delta l $:  $ W^{*}\rightarrow V^{*} $ also extends to an algebra homomorphism

 $$ \delta l\colon\Lambda(W^{*})\to\Lambda(V^{*}). $$ 

Our isomorphisms 2.9(5) of  $ \Lambda(V^{*}) $ with  $ \Lambda(V)^{*} $ and of  $ \Lambda(W^{*}) $ with  $ \Lambda(W)^{*} $ are natural in the sense that (2) is the transpose of (1); that is,

 $$ \big(\delta l(w^{*}),v\big)=\big(w^{*},l(v)\big)\qquad\big(w^{*}\in\Lambda(W^{*});v\in\Lambda(v)\big). $$ 

##### TENSOR FIELDS AND DIFFERENTIAL FORMS

2.14 Definitions Let M be a differentiable manifold. We define

 $$ T_{r,s}(M)=\bigcup_{m\in\mathcal{M}}(M_{m})_{r,s} $$ 

tensor bundle of type (r,s) over M

 $$ \Lambda_{k}^{*}(M)=\bigcup_{m\in\mathcal{M}}\Lambda_{k}(M_{m}^{*}) $$ 

exterior k bundle over M

(3)

 $$ \Lambda^{*}(M)=\bigcup_{m\in\mathcal{M}}\Lambda(M_{m}^{*}) $$ 

exterior algebra bundle over M.

In the cases in which $k = 0$ and $(r,s) = (0,0)$, the unions in (1) and (2) are disjoint unions of copies of the real line—one copy for each point in $M$. $T_{r,s}(M)$, $\Lambda_{k}^{*}(M)$, and $\Lambda^{*}(M)$ have natural manifold structures such that the canonical projection maps to $M$ are $C^{\infty}$. If $(U,\varphi)$ is a coordinate system on $M$ with coordinate functions $y_{1}, \ldots, y_{d}$, then the bases $\{\partial/\partial y_{i}\}$ of $M_{m}$ and $\{dy_{i}\}$ of $M_{m}^{*}$, for $m \in U$, yield bases of $(M_{m})_{r,s}$, $\Lambda_{k}(M_{m}^{*})$, and $\Lambda(M_{m}^{*})$. For example, the basis of $\Lambda_{k}(M_{m}^{*})$ is $\{dy_{i_{1}} \wedge \cdots \wedge dy_{i_{k}}: i_{1} < \cdots < i_{k}\}$.

Using these bases, one can define maps of the inverse images of $U$ in $T_{r,s}(M)$, $\Lambda_{k}^{*}(M)$, and $\Lambda^{*}(M)$ under the respective projection maps to $\varphi(U) \times$ Euclidean spaces of the proper dimensions. By requiring these maps to be coordinate systems, one obtains the natural manifold structures on $T_{r,s}(M)$, $\Lambda_{k}^{*}(M)$, and $\Lambda^{*}(M)$ just as we did previously in 1.25 for $T(M)$ and $T^{*}(M)$ (which incidentally is simply $\Lambda_{1}^{*}(M)$).

2.15 Definition A $C^{\infty}$ mapping of $M$ into $T_{r,s}(M)$, $\Lambda_{k}^{*}(M)$, or $\Lambda^{*}(M)$ whose composition with the canonical projection is the identity map is called a (smooth) tensor field of type $(r,s)$ on $M$, a (differential) $k$-form on $M$, or a (differential) form on $M$ respectively. Since our tensor fields and differential forms will always be smooth in this sense, we shall drop the adjectives “smooth” and “differential” unless needed for emphasis.

2.16 Remarks A lifting  $ \alpha\colon M \to T_{r,s}(M) $ is a smooth tensor field of type  $ (r,s) $ if and only if for each coordinate system  $ (U, y_1, \ldots, y_d) $ on  $ M $,

 $$ \alpha\mid U=\sum a_{\mathfrak{s}_{1},\ldots,\mathfrak{s}_{r};\mathfrak{s}_{1},\ldots,\mathfrak{s}_{s}}\frac{\partial}{\partial y_{\mathfrak{s}_{1}}}\otimes\cdots\otimes\frac{\partial}{\partial y_{\mathfrak{s}_{r}}}\otimes d y_{\mathfrak{s}_{1}}\otimes\cdots\otimes d y_{\mathfrak{s}_{s}}, $$ 

where the  $ a_{t_1,\ldots,t_r;t_1,\ldots,t_s} \in C^\infty(U) $. (In the classical tensor notation one uses lower indices on tangent vectors, upper indices on functions and differentials, and the reverse on coefficients; thus the individual terms of (1) would appear as

 $$ a_{j_{1},\ldots,j_{s}}^{i_{1},\ldots,i_{r}}\frac{\partial}{\partial y^{i_{1}}}\otimes\cdots\otimes\frac{\partial}{\partial y^{i_{r}}}\otimes d y^{j_{1}}\otimes\cdots\otimes d y^{j_{s}}.)\nonumber $$ 

A lifting $\beta\colon M\to\Lambda_{k}^{*}(M)$ is a differential $k$-form if and only if for each coordinate system $(U,y_{1},\ldots,y_{d})$ on $M$,

 $$ \beta\mid U=\sum_{i_{1}<\dots<i_{k}}b_{i_{1},\dots,i_{k}}d y_{i_{1}}\wedge\dots\wedge d y_{i_{k}}, $$ 

where the  $ b_{i_{1},...,i_{k}} $ are  $ C^{\infty} $ functions on U.

2.17 Definitions  $ E^*(M) $ shall denote the set of all smooth k-forms on M, and  $ E^*(M) $ the set of all differential forms.  $ E^*(M) $ can be identified with  $ C^\infty(M) $; indeed, the differentiable manifold  $ \Lambda_0^*(M) $ is simply  $ M \times \mathbb{R} $, and smooth liftings of M into  $ M \times \mathbb{R} $ are simply graphs of  $ C^\infty $ functions on M. Forms can be added, multiplied by scalars, and given a product  $ (\wedge) $. If  $ \omega, \varphi \in E^*(M) $ and  $ c \in \mathbb{R} $, then  $ \omega + \varphi $,  $ c\omega $, and  $ \omega \wedge \varphi $ are the forms which at m have the values  $ \omega_m + \varphi_m $,  $ c\omega_m $, and  $ \omega_m \wedge \varphi_m $ respectively. In the case in which f is a 0-form and  $ \omega \in E^*(M) $, we write  $ f \wedge \omega $ simply as  $ f\omega $.  $ E^*(M) $ thus has the structure both of a module over the ring  $ C^\infty(M) $ and of a graded algebra over  $ \mathbb{R} $ with wedge multiplication.

2.18 Let  $ \omega \in E^b(M) $. Then  $ \omega_m \in \Lambda_k(M_m^*) $, and can be considered (via the duality 2.9(4)) as an alternating multilinear function on  $ M_m $. So if  $ X_1, \ldots, X_k $ are vector fields on  $ M $,  $ \omega(X_1, \ldots, X_k) $ makes sense—it is the function whose value at  $ m $ is

 $$ \omega(X_{1},\ldots,X_{k})(m)=\omega_{m}\bigl(X_{1}(m),\ldots,X_{k}(m)\bigr). $$ 

Thus, if we let  $ \mathfrak{X}(M) $ denote the  $ C^\infty(M) $ module of smooth vector fields on M, then

 $$ \omega\colon\underbrace{\mathfrak{Z}(M)\times\cdots\times\mathfrak{Z}(M)}_{k{~c o p i e s}}\to C^{\infty}(M) $$ 

and is an alternating multilinear map of the module  $ \mathfrak{X}(M) $ into  $ C^\infty(M) $. We stress that  $ \omega $ is multilinear over the  $ C^\infty(M) $ module  $ \mathfrak{X}(M) $; that is

 $$ \begin{aligned}{\omega(X_{1},\ldots,X_{i-1},}&{{}f X+g Y,X_{i+1},\ldots,X_{k})}\\ {\quad=}&{{}f\omega(X_{1},\ldots,X_{i-1},X,X_{i+1},\ldots,X_{k})}\\ {}&{{}+g\omega(X_{1},\ldots,X_{i-1},Y,X_{i+1},\ldots,X_{k})}\\ \end{aligned} $$ 

whenever $f, g \in C^\infty(M)$ and $X_1, \ldots, X_{i-1}, X, Y, X_{i+1}, \ldots, X_k \in \mathfrak{X}(M)$.

Conversely, it is useful to observe that any alternating $C^\infty(M)$ multilinear map (2) of the module $\mathfrak{X}(M)$ into $C^\infty(M)$ defines a form; for we claim that if $\omega$ is such a map, then $\omega(X_1, \ldots, X_k)(m)$ depends only on the values of the vector fields $X_i$ at $m$. Assuming this for the moment, it follows that $\omega$ defines an alternating multilinear function $\omega_m$ on $M_m$, and hence defines an element of $\Lambda_k(M_m^*)$; namely, given $(v_1, \ldots, v_k) \in M_m \times \cdots \times M_m$, choose $V_1, \ldots, V_k \in \mathfrak{X}(M)$ such that $V_i(m) = v_i$ ($i = 1, \ldots, k$), and define

 $$ \omega_{m}(v_{1},\ldots,v_{k})=\omega(V_{1},\ldots,V_{k})(m). $$ 

By our claim,  $ \omega_m(v_1, \ldots, v_k) $ is well-defined, independent of the choice of the extensions  $ V_i $. Thus  $ \omega $ gives a lifting  $ m \mapsto \omega_m $ of  $ M $ into  $ \Lambda^*(M) $, and this is easily seen to be smooth; hence  $ \omega $ is a form.

For simplicity of notation, we illustrate the claim with the case in which $\omega$ is a linear map of the module $\mathfrak{X}(M)$ into $C^\infty(M)$. Let $X\in\mathfrak{X}(M)$. We wish to show that $\omega(X)(m)$ depends only on $X(m)$. It suffices to show that $\omega(X)(m)=0$ if $X(m)=0$. Let $(U,x_1,\ldots,x_a)$ be a coordinate system about $m$. Then on $U$, we have $X=\sum a_i(\partial/\partial x_i)$ where $a_i(m)=0$. Now, let $\varphi$ be a $C^\infty$ function which takes the value 1 on a neighborhood $V\subset U$ of $m$ and is zero on a neighborhood of $M-U$ (see 1.10). Then the vector field $X_t$ which is $\varphi(\partial/\partial x_t)$ on $U$ and $0$ elsewhere is a $C^\infty$ vector field on $M$; the function $\bar{a}_t$ which is $\varphi a_t$ on $U$ and $0$ elsewhere belongs to $C^\infty(M)$; and

 $$ X=\sum\tilde{a}_{i}X_{i}+(1-\varphi^{a})X. $$ 

Thus

 $$ \begin{array}{r}{\omega(X)(m)=\sum\tilde{a}_{i}(m)\omega(X_{i})(m)+\big((1-\varphi^{2})(m)\big)\big(\omega(X)(\dot{m})\big)=0.}\end{array} $$ 

So  $ \omega(X)(m)=0 $ if  $ X(m)=0 $, as was to be shown.

Finally, we remark that via the duality 2.8(5), tensor fields can be given a similar interpretation. If $T$ is a tensor field of type $(r,s)$, then we can consider $T$ as a map

 $$ T\colon\underbrace{E^{1}(M)\times\cdots\times E^{1}(M)}_{{~r~c o p i e s}}\times\underbrace{\mathfrak{X}(M)\times\cdots\times\mathfrak{X}(M)}_{{~s~c o p l e s}}\to C^{\infty}(M), $$ 

which is $C^{\infty}(M)$ multilinear with respect to the $C^{\infty}(M)$ modules $E^{1}(M)$ and $\mathfrak{X}(M)$.

Observe the simple form which formula (2) of 2.10(b) takes when $\omega, \varphi \in E^1(M)$ and $X, Y \in \mathfrak{X}(M)$. In this case, we have

 $$ \omega\wedge\varphi(X,Y)=\omega(X)\varphi(Y)-\omega(Y)\varphi(X). $$ 

2.19 Definition If $f \in C^\infty(M)$, the differential $df$ is a smooth mapping of $T(M)$ into $\mathbb{R}$ which is linear on each tangent space. Thus $df$ can be considered as a 1-form, $df: M \to \Lambda_1^*(M)$. The 1-form $df$ is called the exterior derivative of the 0-form $f$, and this exterior differentiation operator $d$ has an important extension to $E^*(M)$ given by the following.

2.20 Theorem (Exterior Differentiation) There exists a unique anti-derivation $d\colon E^{*}(M)\to E^{*}(M)$ of degree +1 such that

(1)  $ d^{2}=0 $

(2) Whenever  $ f \in C^\infty(M) = E^0(M) $, df is the differential of f.

PROOF Existence. Let $p \in M$. Let $E^*(p)$ be the set of all smooth forms defined on open subsets of $M$ containing $p$, with $E^k(p)$ the corresponding set of $k$-forms. We fix a coordinate system $(U, x_1, \ldots, x_d)$ about $p$. If $\omega \in E^*(p)$, then

(3)

 $$ \omega\big|_{{\mathrm{(d o m a i n~}\omega)\cap\mathcal{V}}}=\sum a_{\Phi}d x_{\Phi} $$ 

where the $a_\Phi \in C^\infty\big((\text{domain} \omega) \cap U\big)$, where $\Phi$ runs over all subsets of $\{1, \ldots, d\}$, and where the $dx_\Phi$ are either $dx_{\epsilon_1} \wedge \cdots \wedge dx_{\epsilon_r}$ when $\Phi = \{i_1 < \cdots < i_r\}$ or the constant function $1$ when $\Phi = \varnothing$. We define $d\omega$ at $p$ by setting

 $$ \begin{array}{r}{d\omega_{p}=\sum d a_{\Phi}|_{p}\wedge d x_{\Phi}|_{p}\in\Lambda(M_{p}^{*}).}\end{array} $$ 

(4)

## 66 Tensors and Differential Forms

We will have to show that the definition of  $ d\omega $, is independent of the choice of coordinates. But first, we give the following properties:

(a)  $ \omega \in E^{\tau}(p) \Rightarrow d\omega_g \in \Lambda_{r+1}(M_g^*) $.

(b)  $ d\omega_{p} $ depends only on the germ of  $ \omega $ at p.

(c)  $ d(a_1\omega_1 + a_2\omega_2)|_g = a_1(d\omega_1)|_g + a_2(d\omega_2)|_g $,  $ (a_i \in \mathbb{R}; \omega_i \in E^*(p)) $, where the domain of  $ a_1\omega_1 + a_2\omega_2 $ is (domain  $ \omega_1 \cap \text{domain}\omega_2 $).

 $$ \begin{array}{r}{d(\omega_{1}\wedge\omega_{2})\big|_{p}=d\omega_{1}\big|_{p}\wedge\omega_{2}\big|_{p}+(-1)^{r}\omega_{1}\big|_{p}\wedge d\omega_{2}\big|_{p}}\\ {\big(\omega_{1}\in E^{r}(p);\omega_{2}\in E^{*}(p)\big).}\end{array} $$ 

In view of properties (b) and (c), it suffices to check (d) for $\omega_1 = f dx_{i_1} \wedge \cdots \wedge dx_{i_r}$ and $\omega_8 = g dx_{i_1} \wedge \cdots \wedge dx_{i_s}$ on some neighborhood of $p$. For the case $r = s = 0$, property (d) is simply $d(f \cdot g)|_{p} = df_p \cdot g(p) + f(p) \cdot dg_p$; and the case in which only one of $r$ or $s$ is $0$ is similar. Now suppose that $r > 0$ and $s > 0$. If $\{i_1, \ldots, i_r\} \cap \{j_1, \ldots, j_s\} \neq \varnothing$, both sides are 0. So assume that this intersection is empty. Then

 $$ \begin{array}{r}{(f d x_{i_{1}}\wedge\cdot\cdot\cdot\wedge d x_{i_{r}})\wedge(g d x_{i_{1}}\wedge\cdot\cdot\cdot\wedge d x_{i_{r}})}\\ {=\varepsilon f\cdot g\;d x_{i_{1}}\wedge\cdot\cdot\cdot\wedge d x_{i_{r+s}}}\end{array} $$ 

where  $ l_{1} < \cdots < l_{r+s} $ and  $ \varepsilon $ is the sign of the permutation that has been carried out. So we have that

 $$ \begin{array}{r l r}{\lefteqn{d(\omega_{1}\wedge\omega_{2})\big|_{g}=d(\varepsilon f\cdot g\;d x_{i_{1}}\wedge\dots\wedge d x_{i_{r+\varepsilon}})\big|_{g}}}\\ &{}&{=\varepsilon\big(d f_{g}\cdot g(p)+f(p)\;d g_{g}\big)\wedge d x_{i_{1}}\big|_{g}\wedge\dots\wedge d x_{i_{r+\varepsilon}}\big|_{g}}\\ &{}&{=\big(d f_{g}\wedge d x_{i_{1}}\big|_{g}\wedge\dots\wedge d x_{i_{r}}\big|_{g}\big)\wedge\big(g(p)\;d x_{i_{1}}\big|_{g}\wedge\dots\wedge d x_{i_{r}}\big|_{g}\big)}\\ &{}&{+~(-1)^{r}\big(f(p)\;d x_{i_{1}}\big|_{g}\wedge\dots\wedge d x_{i_{r}}\big|_{g}\big)}\\ &{}&{\wedge\big(d g_{g}\wedge d x_{i_{1}}\big|_{g}\wedge\dots\wedge d x_{i_{r}}\big|_{g}\big)}\\ &{}&{=d\omega_{1}\big|_{g}\wedge\omega_{2}\big|_{g}+(-1)^{r}\omega_{1}\big|_{g}\wedge d\omega_{2}\big|_{g}.}\end{array} $$ 

(e) If $f$ is a $C^\infty$ function on a neighborhood of $p$, then $d(df)|_{p}=0$. For on (domain $f)\cap U$, $df=\sum(\partial f/\partial x_i)dx_i$, so that

 $$ d(d f)|_{p}=\sum d\left(\frac{\partial f}{\partial x_{i}}\right)\Bigg|_{p}\wedge d x_{i}\big|_{p}=\sum_{i,j}\frac{\partial^{2}f}{\partial x_{j}\partial x_{i}}\Bigg|_{p}d x_{j}\big|_{p}\wedge d x_{i}\big|_{p}. $$ 

But  $ (\partial^2f/\partial x_j\,\partial x_i)(p)=(\partial^2f/\partial x_i\,\partial x_j)(p) $, whereas  $ dx_j\big|_{p}\wedge dx_i\big|_{p}=-dx_i\big|_{p}\wedge dx_j\big|_{p} $. So  $ d(df)\big|_{p}=0 $.

Now we claim that the definition of $d$ at $p$ is independent of the coordinates chosen. For let $d'$ be defined on $E^*(p)$ relative to another coordinate system, and let $\omega \in E^*(p)$. Then $\omega$ on (domain $\omega$) $\cap U$ is given by (3), and since $d'$ must also satisfy properties (a)–(e), it follows that

 $$ \begin{array}{r l r}{(5)\quad d^{\prime}(\omega)\big\vert_{p}}&{=d^{\prime}(\sum a_{\Phi}d x_{i_{1}}\wedge\dots\wedge d x_{i_{r}})\big\vert_{p}}&{\quad\mathrm{(b y~(b))}}\\ &{=\sum d^{\prime}(a_{\Phi}d x_{i_{1}}\wedge\dots\wedge d x_{i_{r}})\big\vert_{p}}&{\quad\mathrm{(b y~(c))}}\\ &{=\sum d^{\prime}(a_{\Phi})\big\vert_{p}\wedge d x_{i_{1}}\big\vert_{p}\wedge\dots\wedge d x_{i_{r}}\big\vert_{p}}\\ &{\quad+\sum(-1)^{k-1}a_{\Phi}\big\vert_{p}d x_{i_{1}}\big\vert_{p}\wedge\dots\wedge d^{\prime}(d x_{i_{b}})\big\vert_{p}\wedge\dots\wedge d x_{i_{r}}\big\vert_{p}}\\ &{}&{\quad\mathrm{(b y~(d))}}\\ &{=\sum d(a_{\Phi})\big\vert_{p}\wedge d x_{i_{1}}\big\vert_{p}\wedge\dots\wedge d x_{i_{r}}\big\vert_{p}}&{\quad\mathrm{(b y~(e))}}\\ &{=d\omega_{p}.}\end{array} $$ 

Now, if $\omega \in E^*(M)$, we define $d\omega$ to be the form which as a lifting of $M$ into $\Lambda^*(M)$ sends $p$ to $d\omega_p$. It follows that $d^2 = 0$, since if $\omega \in E^*(M)$ and $p \in M$, $d\omega$ has the form $\sum da_\oplus \wedge dx_\oplus$ on a coordinate neighborhood of $p$, and thus

 $$ d(d\omega)|_{s}=\sum d(d a_{\Phi}\wedge d x_{\Phi})|_{s}=0 $$ 

by properties (e) and (d). It follows that $d$ is an anti-derivation of $E^{*}(M)$ of degree +1 satisfying (1) and (2).

Uniqueness Let $d'$ also be an anti-derivation of $E^{*}(M)$ of degree +1 satisfying (1) and (2). We first show that if $\omega \in E^{*}(M)$ and $\omega$ vanishes on a neighborhood $W$ of $p$, then $d'\omega|_{p} = 0$. Choose a $C^{\infty}$ function $\varphi$ which is 0 on a neighborhood of $p$ and 1 on a neighborhood of $M - W$. Then $\varphi\omega = \omega$ and

 $$ d^{\prime}(\omega)\big|_{\mathfrak{s}}=d^{\prime}(\varphi\omega)\big|_{\mathfrak{s}}=d^{\prime}(\varphi)\big|_{\mathfrak{s}}\wedge\omega_{\mathfrak{s}}+\varphi(p)\:d^{\prime}\omega\big|_{\mathfrak{s}}=0. $$ 

Now $d'$ is defined only on elements of $E^{*}(M)$, that is, on globally defined forms on $M$. We wish to define $d'$ on $E^{*}(p)$ for each $p \in M$. If $\omega \in E^{*}(p)$, we can extend $\omega$ to a form on $M$ having the same germ at $p$ as does $\omega$. Simply let $\varphi$ be a $C^{\infty}$ function which is 1 on a neighborhood of $p$ and has support in the domain of $\omega$. Then $\varphi\omega \in E^{*}(M)$ ($\varphi\omega$ is defined to be 0 outside of the domain of $\omega$), and $\varphi\omega$ agrees with $\omega$ on a neighborhood of $p$. Thus we can define

 $$ d^{\prime}(\omega)|_{s}=d^{\prime}(\varphi\omega)|_{s}, $$ 

and by the above remarks this definition is independent of the extension chosen. Thus  $ d'(\omega)|_{p} $ is defined for all  $ \omega $ in  $ E^{*}(p) $ and clearly satisfies properties (a)–(e). (In (d), extend  $ \omega_{1} \wedge \omega_{2} $ to a form on M by using  $ \varphi\omega_{1} \wedge \varphi\omega_{2} $ for a suitable  $ \varphi $; and in (e), observe that  $ d'(df)|_{p}=d'(\varphi df)|_{p}=d'(d(\varphi f))|_{p}=0 $, since  $ d\varphi(p)=0 $ and since  $ d' $ satisfies (1) and (2).) The equations (5) now imply that whenever  $ \omega \in E^{*}(p) $ in particular whenever  $ \omega \in E^{*}(M) $,  $ d'(\omega)|_{p}=d(\omega)|_{p} $. This proves uniqueness.

Observe that it is clear from the above proof that  $ d\omega \mid U = d(\omega \mid U) $ whenever U is an open set in M.

2.21 Interior Multiplication by Vector Fields Let $X$ be a smooth vector field on $M$, and let $\omega \in E^*(M)$. Interior multiplication of $\omega$ by $X$ is the form $i(X)\omega$ whose value at $m$ is the interior multiple of $\omega_m$ by $X_m$ (see 2.11(2)):

 $$ \left(i(X)\omega\right)\big|_{m}=i(X_{m})(\omega_{m}). $$ 

That $i(X)\omega$ is smooth follows easily from 2.16(2); and from 2.12 it follows that $i(X)\colon E^{*}(M)\to E^{*}(M)$ is an anti-derivation of degree -1.

2.22 Effect of Mappings Let $\psi: M \to N$ be a smooth map, and let $m \in M$. Then we have the differential $d\psi: M_m \to N_{\psi(m)}$, its transpose $\delta\psi: N_{\psi(m)}^* \to M_m^*$, and the induced algebra homomorphism $\delta\psi: \Lambda(N_{\psi(m)}^* \to \Lambda(M_m^*)$. If $\omega$ is a form on $N$, then we can pull $\omega$ back to a form on $M$ by setting

 $$ \delta\psi(\omega)|_{m}=\delta\psi(\omega|_{\psi(m)}). $$ 

This is one of the particularly nice features of differential forms. Under a smooth mapping, they can be pulled back from the range to the domain of the map. Vector fields, on the other hand, do not display such pleasing behavior under mappings.

2.23 Proposition Let  $ \psi\colon M \to N $ be a smooth map. Then

(a)  $ \delta\psi\colon E^{*}(N)\to E^{*}(M) $ and is an algebra homemorphism.

(b)  $ \delta\psi $ commutes with  $ d $; that is,  $ d(\delta\psi(\omega)) = \delta\psi(d\omega) $ ( $ \omega \in E^*(N) $).

(c)  $ \delta\psi(\omega)(X_1,\ldots,X_k)(m)=\omega_{\psi(m)}(d\psi(X_1(m)),\ldots,d\psi(X_k(m))) $ for  $ \omega\in E^k(N) $ and for vector fields  $ X_1,\ldots,X_k $ on  $ M $.

PROOF Result (c) is clear from 2.13(3); and 2.13(2) and the definition 2.22(1) imply that $\delta\psi$ is an algebra homomorphism. Before we check that $\delta\psi(\omega)$ is actually a smooth form for $\omega\in E^{*}(N)$, observe the following special case of (b): If $f\in C^\infty(N)$, then $\delta\psi(f)=f\circ\psi\in C^\infty(M)$, and 1.23(d) implies that

 $$ \delta\psi(d f)=d(f\circ\psi)=d(\delta\psi(f)). $$ 

Now let $\omega \in E^{*}(N)$, and let $m \in M$. Choose a coordinate system $(U, x_1, \ldots, x_d)$ about $\psi(m)$ and a neighborhood $V$ of $m$ such that $\psi(V) \subset U$. Then there are $C^\infty$ functions $a_\bullet$ on $U$ such that

 $$ \omega\mid U=\sum a_{\bullet}d x_{i_{1}}\wedge\cdots\wedge d x_{i_{r}}. $$ 

It follows that

 $$ \delta\psi(\omega)\bigm|V=\sum a_{\Phi}\circ\psi\;d(x_{i_{1}}\circ\psi)\wedge\dots\wedge d(x_{i_{r}}\circ\psi), $$ 

which is a smooth form on $V$. Hence $\delta\psi(\omega)\in E^{*}(M)$, and thus (a) is proved. To complete (b), we use (3):

 $$ \begin{aligned}{d\big(\delta\psi(\omega)\big)\big|_{m}}&{{}=d\big(\textstyle\sum a_{\oplus}\circ\psi d(x_{i_{1}}\circ\psi)\wedge\cdots\wedge d(x_{i_{r}}\circ\psi)\big)\big|_{m}}\\ {}&{{}=\textstyle\sum\big(d(a_{\oplus}\circ\psi)\wedge d(x_{i_{1}}\circ\psi)\wedge\cdots\wedge d(x_{i_{r}}\circ\psi)\big)\big|_{m}}\\ {}&{{}=\delta\psi(\textstyle\sum d a_{\oplus}\wedge d x_{i_{1}}\wedge\cdots\wedge d x_{i_{r}}\big)\big|_{m}}\\ {}&{{}=\delta\psi(d\omega)\big|_{m}.}\\ \end{aligned} $$ 

Thus (b) is proved, and the proof is complete.

##### THE LIE DERIVATIVE

2.24 Definition Tensor fields and differential forms can be differentiated with respect to a vector field. The resulting derivative is known as the Lie derivative and is defined as follows. Fix a smooth vector field $X$ on a manifold $M$. Recall (see 1.48) that we use $X_t$ to denote the local 1-parameter group of transformations associated with $X$. Let $Y$ be another smooth vector field on $M$. We shall define the derivative of $Y$ with respect to $X$ at the point $m \in M$. First we follow the integral curve of $X$ through $m$ out to the point $X_t(m)$ and evaluate $Y$ there. Then we transfer $Y_{x_t(m)}$ back to $M_m$ via the differential $dX_{-t}$ of the diffeomorphism $X_{-t}$. In $M_m$ we take the difference of the vectors $dX_{-t}(Y_{x_t(m)})$ and $Y_m$, divide the difference by $t$, and then take the limit as $t \to 0$. In other words, we consider the smooth $M_m$-valued function $t \mapsto dX_{-t}(Y_{x_t(m)})$, and we take its derivative at $t = 0$. The result is a vector in $M_m$ which is called the Lie derivative of $Y$ with respect to $X$ at $m$ and which is denoted by $(L_X Y)_m$. Thus we define

 $$ (L_{X}Y)_{m}=\operatorname*{l i m}_{t\to0}\frac{d X_{-t}(Y_{X_{t}(m)})-Y_{m}}{t}=\frac{d}{d t}\bigg|_{t=0}\big(d X_{-t}(Y_{X_{t}(m)})\big). $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//540a91b5-f1c2-4086-b901-3b0990256a35/markdown_0/imgs/img_in_image_box_144_859_801_1175.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A22Z%2F-1%2F%2F2a9b79b0f03b4ef63bc4341e16fa083884c6d2370a5b2900b05b5d03a67c595e" alt="Image" width="69%" /></div>


In a similar way we define the Lie derivative of a differential form $\omega$ with respect to the vector field $X$, except that in this case we evaluate $\omega$ at $X_t(m)$ and then pull back via $\delta X_t$ to $\Lambda(M_m^*)$ where we take the difference with $\omega(m)$, divide by $t$, and take the limit as $t \to 0$. Thus we define

 $$ (L_{\mathbb{X}}\omega)_{m}=\operatorname*{l i m}_{t\to0}\frac{\delta X_{t}(\omega_{\mathbb{X}_{t}(m)})-\omega_{m}}{t}=\frac{d}{d t}\bigg|_{t=0}\big(\delta X_{t}(\omega_{\mathbb{X}_{t}(m)})\big). $$ 

Smoothness of $L_{x}\omega$ and of $L_{x}Y$ is asserted in Proposition 2.25. The Lie derivative $L_{x}$ can be extended to arbitrary tensor fields in the obvious way. If $T$ is a tensor field of type $(r,s)$, then $(L_{x}T)_{m}$ is the derivative at $t=0$ of the $(M_{m})_{(r,s)}$-valued function whose value at $t$ is

 $$ d X_{-t}(v_{1}\otimes\cdots\otimes v_{r})\otimes\delta X_{t}(v_{1}^{*}\otimes\cdots\otimes v_{t}^{*}) $$ 

if

 $$ T\big|_{X_{t}(m)}=v_{1}\otimes\cdots\otimes v_{r}\otimes v_{1}^{*}\otimes\cdots\otimes v_{s}^{*}. $$ 

2.25 Proposition Let $X$ be a $C^{\infty}$ vector field on $M$. Then

(a)  $ L_{X}f = X(f) $ whenever  $ f \in C^{\infty}(M) $.

(b)  $ L_{X}Y = [X,Y] $ for each  $ C^{\infty} $ vector field Y on M.

(c)  $ L_{X}\colon E^{*}(M)\to E^{*}(M) $, and is a derivation which commutes with  $ d $.

(d) On  $ E^{*}(M) $,  $ L_{X} = i(X) \circ d + d \circ i(X) $.

(e) Let $\omega \in E^{p}(M)$, and let $Y_{0}, \ldots, Y_{p}$ be $C^{\infty}$ vector fields on $M$. Then

 $$ \begin{aligned}{L_{Y_{0}}\big(\omega(Y_{1},\ldots,Y_{p})\big)}&{{}=(L_{Y_{0}}\omega)(Y_{1},\ldots,Y_{p})}\\ {}&{{}+\sum_{i=1}^{p}\omega(Y_{1},\ldots,Y_{i-1},L_{Y_{0}}Y_{i},Y_{i+1},\ldots,Y_{p}).}\\ \end{aligned} $$ 

(f) Assumption as in (e). Then

 $$ \begin{aligned}{d\omega(Y_{0},\ldots,Y_{p})}&{{}=\sum_{i=0}^{p}(-1)^{i}Y_{i}\omega(Y_{0},\ldots,\widehat{Y_{i}},\ldots,Y_{p})}\\ {+}&{{}\sum_{i<j}(-1)^{i+j}\omega([Y_{i},Y_{j}],\;Y_{0},\ldots,\widehat{Y_{i}},\ldots,\widehat{Y_{j}},\ldots,Y_{p}).}\\ \end{aligned} $$ 

PROOF We leave result (a) as an exercise. For (b), we need only show that  $ L_{X}Y(f)=[X,Y] $ for each  $ f\in C^{\infty}(M) $. Let  $ m\in M $. Then

 $$ \begin{aligned}{(L_{\mathcal{X}}Y)(f)}&{{}=\bigg(\varliminf_{t\to0}\frac{d X_{-t}Y_{X_{t}(m)}-Y_{m}}{t}\bigg)(f)}\\ {}&{{}=\frac{d}{d t}\bigg|_{t=0}\big[\big(d X_{-t}(Y_{X_{t}(m)})\big)(f)\big]}\\ {}&{{}=\frac{d}{d t}\bigg|_{t=0}[Y_{X_{t}(m)}(f\circ X_{-t})].}\\ \end{aligned} $$ 

Define a real-valued function $H$ on a neighborhood of $(0,0)$ in $\mathbb{R}^{2}$ by setting

 $$ H(t,u)=f\bigl(X_{-t}(Y_{u}(X_{t}(m)))\bigr). $$ 

Then by (a),

 $$ Y_{\mathbb{X}_{t(m)}}(f\circ X_{-t})=\frac{\partial}{\partial r_{2}}\bigg\vert_{(t,0)}H(t,u), $$ 

and (1) becomes

 $$ (L_{X}Y)_{m}(f)=\frac{\partial^{2}H}{\partial r_{1}\partial r_{2}}\bigg|_{(0,0)}. $$ 

To evaluate this derivative, we set

 $$ K(t,u,s)=f\bigl(X_{s}(Y_{u}(X_{t}(m)))\bigr). $$ 

Then  $ H(t,u) = K(t,u,-t) $. It follows from the chain rule that

 $$ \frac{\partial^{2}H}{\partial r_{1}\partial r_{2}}\bigg|_{(0,0)}=\frac{\partial^{2}K}{\partial r_{1}\partial r_{2}}\bigg|_{(0,0,0)}-\frac{\partial^{2}K}{\partial r_{3}\partial r_{2}}\bigg|_{(0,0,0)}. $$ 

Now,  $ K(t,u,0) = f(Y_u(X_t(m))) $. Hence

 $$ \left.\frac{\partial K}{\partial r_{2}}\right|_{(t,0,0)}=Y_{X_{t}(m)}(f), $$ 

(7)

 $$ \frac{\partial^{2}K}{\partial r_{1}\partial r_{2}}\bigg|_{(0,0,0)}=X_{m}(Y f). $$ 

Also  $ K(0,u,s) = f(X_s(Y_u(m))) $. Hence

 $$ \frac{\partial K}{\partial r_{3}}\bigg|_{(0,u,0)}=X f\big(Y_{u}(m)\big), $$ 

 $$ \frac{\partial^{2}K}{\partial r_{2}\partial r_{3}}\bigg|_{(0,0,0)}=Y_{m}(X f). $$ 

Part (b) now follows from (4), (6), (7), and (8). One immediate consequence of (b) is that $L_{x}Y$ is a smooth vector field.

For result (c), first consider $L_{x}$ as a mapping of $E^{*}(M)$ into forms which are not apriori smooth, and observe that the derivation property follows immediately from adding and subtracting suitable terms before taking the limit in the definition 2.24(1). Next we check that $L_{x}$ commutes with $d$ when applied to functions; that is,

## 72 Tensors and Differential Forms

 $$ \big(L_{X}(d f)\big)_{m}=d(L_{X}f)_{m}\qquad\big(f\in C^{\infty}(M);m\in M\big). $$ 

Since both sides of (9) are elements of  $ M_{m}^{*} $, we need only prove that they have the same effect when applied to an arbitrary vector  $ Y_{m} $ in  $ M_{m} $. The right-hand side gives

 $$ d(L_{\mathbb{X}}f)_{\mathfrak{m}}(Y_{\mathfrak{m}})=Y_{\mathfrak{m}}(L_{\mathbb{X}}f)=Y_{\mathfrak{m}}\biggl(\frac{d}{d t}\bigg\vert_{t=0}(f\circ X_{t})\biggr), $$ 

where $f\circ X_{t}$ can be considered as a $C^{\infty}$ function on $(-\varepsilon,\varepsilon)\times W$ for some $\varepsilon>0$ and some neighborhood $W$ of $m$ in $M$ (1.48(d)). The left-hand side of (9) gives

 $$ \begin{aligned}{\big(L_{X}(d f)\big)_{m}(Y_{m})}&{{}=\bigg\{\frac{d}{d t}\bigg|_{t=0}\big(\delta X_{t}(d f_{X_{t}(m)})\big)\bigg\}(Y_{m})}\\ {}&{{}=\frac{d}{d t}\bigg|_{t=0}\big(\delta X_{t}(d f_{\varSigma_{t}(m)})(Y_{m})\big)}\\ {}&{{}=\frac{d}{d t}\bigg|_{t=0}\big(d f(d X_{t}(Y_{m}))\big)=\frac{d}{d t}\bigg|_{t=0}\big(Y_{m}(f\circ X_{t})\big).}\\ \end{aligned}. $$ 

Now let $Y$ be an extension of $Y_{\infty}$ to a vector field on $W$. Then, according to Exercise 24(c) of Chapter 1, $d/dt$ and $Y$ have canonical extensions to vector fields on $(-\varepsilon,\varepsilon)\times W$ where they satisfy $[d/dt,Y] \equiv 0$. This fact together with (10) and (11) implies (9). Finally, to see that the form $L_{X}\omega$ is actually smooth and to check that $L_{X}$ commutes with $d$ on all of $E^{*}(M)$, simply express an arbitrary form $\omega$ in local coordinates as in 2.16(2), and compute using equation (9), result (a), and the fact that $L_{X}$ is a derivation.

For result (d), observe that both $L_{X}$ and $i(X)\circ d+d\circ i(X)$ are derivations on $E^{*}(M)$ which commute with $d$, and both have the same effect on functions. Then (d) follows from a simple computation in local coordinates.

We shall leave (e) as an exercise. The proof is not difficult—one simply has to be persistent enough in unwinding the definitions. Again, one checks the identity by restricting to a local coordinate system. Try it first for the case  $ \omega = fdx_1 \wedge dx_2 $ in a coordinate neighborhood.

Finally, result (f) follows from (e) by using (d) and induction on p. For the case p = 1, we have from (e) that

 $$ L_{Y_{0}}\big(\omega(Y_{1})\big)=(L_{Y_{0}}\omega)(Y_{1})+\omega[Y_{0},Y_{1}]. $$ 

Applying (a) and (d) to (12), one obtains

 $$ \begin{aligned}{Y_{0}\omega(Y_{1})}&{{}=\big((i(Y_{0})\circ d+d\circ i(\tilde{Y}_{0}))\omega\big)(Y_{1})+\omega[Y_{0},Y_{1}]}\\ {}&{{}=d\omega(Y_{0},Y_{1})+Y_{1}\big(\omega(Y_{0})\big)+\omega[Y_{0},Y_{1}],}\\ \end{aligned} $$ 

which is result (f) in the case p = 1. Now assume that (f) holds for p - 1. Then (f) is obtained for p by again starting with (e) and applying (d) and the induction hypothesis.

##### DIFFERENTIAL IDEALS

Our objective here is to give a version of the Frobenius theorem in terms of differential forms, and then to describe E. Cartan's useful method of obtaining maps by looking for their graphs.

2.26 Definitions Let $\mathcal{D}$ be a $p$-dimensional $C^{\infty}$ distribution on $M$. A $q$-form $\omega$ is said to annihilate $\mathcal{D}$ if for each $m\in M$

 $ \omega_m(v_1, \ldots, v_q) = 0 $ whenever  $ v_1, \ldots, v_q \in \mathcal{D}(m) $.

A form  $ \omega \in E^*(M) $ is said to annihilate  $ \mathcal{D} $ if each of the homogeneous parts of  $ \omega $ annihilates  $ \mathcal{D} $. We let

 $ \mathcal{I}(\mathcal{D}) = \{\omega \in E^*(M)\colon \omega \text{ annihilates } \mathcal{D}\}. $

2.27 Definition A collection  $ \omega_1, \ldots, \omega_n $ of 1-forms on  $ M $ is called independent if they form an independent set in  $ M_m^* $ for each  $ m \in M $.

2.28 Proposition Let D be a smooth p-dimensional distribution on M. Then

(a)  $ \mathcal{I}(\mathcal{D}) $ is an ideal in  $ E^{*}(M) $.

(b) $\mathcal{I}(\mathcal{D})$ is locally generated by $d-p$ independent 1-forms. (That is, to each $m\in M$ there corresponds a neighborhood $U$ of $m$ and a set of independent 1-forms $\omega_{1},\ldots,\omega_{d-p}$ on $U$ such that:

(i) If $\omega \in \mathcal{I}(\mathcal{D})$, then $\omega \mid U$ belongs to the ideal in $E^{*}(U)$ generated by $\omega_1, \ldots, \omega_{d-p}$.

(ii) If $\omega \in E^*(M)$, and if there is a cover of $M$ by sets $U$ (as above) such that for each $U$ in the cover, $\omega \mid U$ belongs to the ideal generated by $\omega_1, \ldots, \omega_{d-p}$, then $\omega \in \mathcal{I}(\mathcal{D})$.)

(c) If $\mathcal{I} \subset E^{*}(M)$ is an ideal locally generated by $d - p$ independent 1-forms, then there exists a unique $C^{\infty}$ distribution $\mathcal{D}$ of dimension $p$ on $M$ for which $\mathcal{I} = \mathcal{I}(\mathcal{D})$.

PROOF Part (a) follows from the definition of  $ \mathcal{I}(\mathcal{D}) $ and the definition of multiplication in  $ E^{*}(M) $.

Let $m \in M$. Since $\mathcal{D}$ is smooth and $p$-dimensional, there exist $C^\infty$ vector fields $X_{d-p+1},\ldots,X_d$ defined and spanning $\mathcal{D}$ at each point of a neighborhood of $m$. This collection can be completed to a collection $X_1,\ldots,X_d$ of smooth vector fields forming a basis of $M_n$ for each $n$ in a neighborhood $U$ of $m$. Let $\omega_1,\ldots,\omega_d$ be the dual 1-forms; that is,

 $$ \omega_{i}(X_{j})(n)=\delta_{i j}\qquad\mathrm{(K r o n e c k e r~i n d e x)} $$ 

for each $n$ in $U$. Then $\omega_{1},\ldots,\omega_{d-p}$ are the desired 1-forms on $U$.

#### Tensors and Differential Forms

They are independent smooth 1-forms on $U$. If $\omega \in \mathcal{J}(\mathcal{D})$, $\omega \mid U = \sum a_0 \omega_{i_b} \wedge \cdots \wedge \omega_{i_r}$, where $\Phi$ runs over nonempty subsets $\{i_1, \ldots, i_r\} \subset \{1, \ldots, d\}$, and where the $a_0$ must be identically zero unless $\{i_1, \ldots, i_r\} \cap \{1, \ldots, d-p\} \neq \emptyset$. Thus $\omega \mid U$ belongs to the ideal in $E^*(U)$ generated by $\omega_{1}, \ldots, \omega_{d-p}$. Conversely, if $\omega$ is a form such that for each such $U$ in some covering of $M$, $\omega \mid U$ belongs to the ideal in $E^*(U)$ generated by $\omega_1, \ldots, \omega_{d-p}$, then clearly $\omega \in \mathcal{J}(\mathcal{D})$. This proves (b).

For part (c), let $m \in M$, and let the independent 1-forms $\omega_1, \ldots, \omega_{\delta-p}$ generate $\mathcal{I}$ on a neighborhood $U$ of $m$. Define $\mathcal{D}(m)$ to be the subspace of $M_m$ whose annihilator is the subspace of $M_m^*$ spanned by the collection $\{\omega_t(m): t=1, \ldots, d-p\}$. It follows that $\mathcal{D}$ is a smooth $p$-dimensional distribution on $M$ and that $\mathcal{I} = \mathcal{I}(\mathcal{D})$. Uniqueness of $\mathcal{D}$ follows from the fact that $\mathcal{D} \neq \mathcal{D}_1$ implies $\mathcal{I}(\mathcal{D}) \neq \mathcal{I}(\mathcal{D}_1)$.

2.29 Definition An ideal $\mathcal{I} \subset E^{*}(M)$ is called a differential ideal if it is closed under exterior differentiation $d$; that is,

 $$ d(\mathcal{I})\subset\mathcal{I}. $$ 

2.30 Proposition $A C^{\infty}$ distribution $\mathcal{D}$ on $M$ is involutive if and only if the ideal $\mathcal{I}(\mathcal{D})$ is a differential ideal.

PROOF Let $\omega$ be a $q$-form in $\mathcal{I}(\mathcal{D})$, and let $X_0, \ldots, X_q$ be smooth vector fields lying in $\mathcal{D}$. Then $2.25(\mathfrak{f})$ together with the involutiveness of $\mathcal{D}$ implies that $d\omega(X_0, \ldots, X_q) \equiv 0$. Hence $d\omega \in \mathcal{I}(\mathcal{D})$, and $\mathcal{I}(\mathcal{D})$ is a differential ideal. Conversely, suppose that $\mathcal{I}(\mathcal{D})$ is a differential ideal. Let $Y_0$ and $Y_1$ be vector fields lying in $\mathcal{D}$, and let $m \in M$. By $2.28(\mathrm{~b})$, there are independent 1-forms $\omega_1, \ldots, \omega_{d-y}$ generating $\mathcal{I}(\mathcal{D})$ on a neighborhood $U$ of $m$. Extend these forms to $M$ by multiplying by a $C^\infty$ function which is 1 on a neighborhood of $m$ and has support in $U$. We shall denote the extended forms similarly by $\omega_1, \ldots, \omega_{d-y}$. By $2.25(\mathfrak{f})$,

 $$ \omega_{i}[Y_{0},Y_{1}]=-d\omega_{i}(Y_{0},Y_{1})+Y_{0}\omega_{i}(Y_{1})-Y_{1}\omega_{i}(Y_{0}) $$ 

for $i=1,\ldots,d-p$. The right-hand side of (1) is identically zero on $M$ since $\mathcal{I}(\mathcal{D})$ is a differential ideal and since $\omega_i\in\mathcal{I}(\mathcal{D})$. Thus $\omega_i([Y_0,Y_1])(m)=0$ for $i=1,\ldots,d-p$. Now $\mathcal{D}(m)$ is the subspace of $M_m$ whose annihilator is the subspace of $M_m^*$ spanned by the collection $\{\omega_i(m):i=1,\ldots,d-p\}$. Thus $[Y_0,Y_1](m)\in\mathcal{D}(m)$, and $\mathcal{D}$ is involutive.

2.31 Definition A submanifold $(N,\psi)$ of $M$ is an integral manifold of an ideal $\mathcal{I} \subset E^{*}(M)$ if for every $\omega \in \mathcal{I}$, $\delta\psi(\omega) \equiv 0$. A connected integral manifold of an ideal $\mathcal{I}$ is maximal if its image is not a proper subset of the image of any other connected integral manifold of the ideal.

It now follows immediately that we have the following version of the Frobenius theorem 1.64 in terms of differential ideals.

2.32 Theorem Let $\mathcal{I} \subset E^{*}(M)$ be a differential ideal locally generated by $d-p$ independent 1-forms. Let $m \in M$. Then there exists a unique maximal, connected, integral manifold of $\mathcal{I}$ through $m$, and this integral manifold has dimension $p$.

2.33 We shall now consider a technique which in certain situations enables one to find a map by looking for its graph as an integral manifold of a differential ideal. This will have important applications in the theory of Lie groups in Chapter 3, and also has important applications in such areas as isometric imbeddings in Riemannian geometry.

Suppose that $f\colon N^{c}\to M^{d}$ is $C^{\infty}$ and that $\{\omega_{i}\}$ is some collection of forms on $M$. Let $\pi_{1}$ and $\pi_{2}$ denote the natural projections of $N\times M$ onto $N$ and $M$ respectively. For each $i$, we define a form $\mu_{i}$ on $N\times M$ by setting

 $$ \mu_{i}=\delta\pi_{1}\delta f(\omega_{i})-\delta\pi_{2}(\omega_{i}). $$ 

Let  $ \mathcal{I} $ be the ideal in  $ E^{*}(N \times M) $ generated by the  $ \mu_i $.

Now the graph of f is the submanifold $(N,g)$ of $N\times M$ where

 $$ g(n)=(n,f(n)). $$ 

We claim that the graph is an integral manifold of the ideal $\mathscr{F}$. For this, it suffices to show that $\delta g(\mu_{t})=0$ for each $i$. Now, $\pi_{1}\circ g=\mathrm{id}$, and $\pi_{2}\circ g=f$, and thus it follows that

 $$ \delta g(\mu_{i})=\delta(\pi_{1}\circ g)\delta f(\omega_{i})-\delta(\pi_{2}\circ g)(\omega_{i})=\delta f(\omega_{i})-\delta f(\omega_{i})=0. $$ 

Thus starting with a map $f\colon N\to M$ and a collection of forms on $M$, we have observed that the graph $f$ is an integral manifold of a certain ideal of forms on $N\times M$. Now, suppose that we start with the manifold $M^d$, and suppose that there exists a basis $\omega_1,\ldots,\omega_d$ of 1-forms on $M$, that is, $\{\omega_i(m)\}$ is a basis of $M_m^*$ for each $m\in M$. (Such a basis does not generally exist, but it does exist in a number of interesting situations for which the following technique is quite useful.) Suppose also that we have a manifold $N^c$ and a collection $\alpha_1,\ldots,\alpha_d$ of 1-forms on $N$ and that we wish to find a map $f\colon N\to M$ such that

 $$ \delta f(\omega_{i})=\alpha_{i} $$ 

for $i=1,\ldots,d$. If the map $f$ exists, then, as we have observed, its graph will be an integral manifold of a certain ideal of forms. So we attempt to find the graph from the ideal. We define forms $\mu_{i}$ on $N\times M$ by setting

 $$ \mu_{i}=\delta\pi_{1}(\alpha_{i})-\delta\pi_{2}(\omega_{i}), $$ 

and we let $\mathcal{I}$ be the ideal in $E^{*}(N \times M)$ which they generate. If $\mathcal{I}$ happens to be a differential ideal, then we can obtain the desired map $f$ (at least locally) from an integral manifold of $\mathcal{I}$. That is, one gets at $f$ by looking for

its graph as an integral manifold of a suitable differential ideal. So suppose that $\mathcal{F}$ is a differential ideal, and let $(n_{\theta},m_{\theta})\in N\times M$. Then since $\mathcal{F}$ is locally (in fact globally) generated by $d$ independent 1-forms, the Frobenius theorem guarantees that there is a maximal, connected, integral manifold $I$ of $\mathcal{F}$ of dimension $c$ through $(n_{\theta},m_{\theta})$. Let $q\in I$. We claim that $d\pi_{1}\mid I_{\theta}$ is 1:1. For suppose that $v\in I_{\theta}$ and that $d\pi_{1}(v)=0$. Then since $\mu_{1}(v)=0$, it follows from (4) that $\omega_{i}(d\pi_{2}(v))=0$ for $i=1,\ldots,d$; and this implies that $d\pi_{2}(v)=0$ since the $\omega_{i}$ form a basis of 1-forms on $M$. But now if both $d\pi_{1}(v)=0$ and $d\pi_{2}(v)=0$, then $v=0$. Hence $d\pi_{1}\mid I_{\theta}$ is 1:1. Thus $\pi_{1}\mid I:I\to N$ is locally a diffeomorphism. So there exist neighborhoods $V$ of $(n_{\theta},m_{\theta})$ in $I$ and $U$ of $n_{\theta}$ such that $\pi_{1}\mid V:V\to U$ is a diffeomorphism. We define $f:U\to M$ by setting

 $$ f=\pi_{2}\circ(\pi_{1}\mid V)^{-1}. $$ 

Then  $ f(n_{0}) = m_{0} $, the graph of f is an open submanifold of I, and moreover,

 $$ \delta f(\omega_{i})=\alpha_{i}\mid U. $$ 

For let  $ v \in U_{n} $ for some  $ n \in U $. Then by (4),

 $$ \begin{aligned}{0}&{{}=\mu_{i}\big(d(\pi_{1}\mid V)^{-1}(v)\big)}\\ {}&{{}=\alpha_{i}(v)-\omega_{i}\big(d\pi_{2}\circ d(\pi_{1}\mid V)^{-1}(v)\big)=\alpha_{i}(v)-\delta f(\omega_{i})(v),}\\ \end{aligned} $$ 

which proves (6). Thus we have obtained the desired map locally. That is, given $n_{\theta} \in N$ and an arbitrary choice of $m_{\theta} \in M$, then under the assumption that the ideal $\mathcal{J}$ generated by (4) is a differential ideal, we have found an open neighborhood $U$ of $n_{\theta}$ and a $C^{\infty}$ map $f: U \to M$ such that $f(n_{\theta}) = m_{\theta}$ and such that $\delta f(\omega_{t}) = \alpha_{t} \mid U$. Moreover, there is a unique such map. More precisely, if $m_{\theta} \in M$, and if $U$ is any connected open neighborhood of $n_{\theta}$ in $N$ for which there exists a $C^{\infty}$ map $f: U \to M$ such that $f(n_{\theta}) = m_{\theta}$ and such that $\delta f(\omega_{t}) = \alpha_{t} \mid U$ for $t = 1, \ldots, d$, then there is a unique such map on $U$. For let $\tilde{f}$ be any other such map. Let $(U, \tilde{g})$ and $(U, g)$ be the graphs of $\tilde{f}$ and $f$ over $U$ respectively. Thus

 $$ \tilde{g}(n)=\left(n,\tilde{f}(n)\right)\quad\mathrm{~a n d~}\quad g(n)=\left(n,f(n)\right) $$ 

for $n \in U$. Then, according to our remarks near the beginning of this section, not only is $(U,g)$ an integral manifold of $\mathcal{J}$ through $(n_{\theta},m_{\theta})$, but so is $(U,\tilde{g})$. Now, the subset of $U$ on which $g$ and $\tilde{g}$ agree is non-empty since it contains $n_{\theta}$, and is closed by continuity, and is moreover open. For let $\tilde{g}(n) = g(n)$. Then it follows from the uniqueness of integral manifolds that there exist sufficiently small neighborhoods $W$ and $\tilde{W}$ of $n$ so that

 $$ g(W)=\tilde{g}(\tilde{W}). $$ 

It follows then from (7) that  $ W = \tilde{W} $ and that

 $$ g\mid W=\tilde{g}\mid W. $$ 

Hence, since $U$ is connected, $g = \tilde{g}$ on $U$, which implies that $f = \tilde{f}$ on $U$. This proves uniqueness.

In suitable situations one can conclude that  $ \pi_{1}|I $ is a covering of  $ N $; and then if  $ N $ is simply connected, one can conclude that there exists a unique  $ C^{\infty} $ map  $ f: N \to M $ such that  $ f(n_{0}) = m_{0} $ and such that (3) holds. In Chapter 3 we shall make several concrete applications of this method for proving existence and uniqueness of certain maps. This technique was originally used by E. Cartan for the problem of finding local isometric imbeddings of Riemannian manifolds in Euclidean space.

We summarize the results of this section in the following.

2.34 Theorem Let $N^{c}$ and $M^{d}$ be differentiable manifolds, and let $\pi_{1}$ and $\pi_{2}$ be the canonical projections of $N\times M$ onto $N$ and $M$ respectively. Suppose that there exists a basis $\{\omega_{i}: i=1,\ldots,d\}$ for the 1-forms on $M$.

(a) If $f: N \to M$ is $C^{\infty}$, then the graph of $f$ is an integral manifold of the ideal of forms on $N \times M$ generated by

 $$ \{\delta\pi_{1}\delta f(\omega_{i})-\delta\pi_{\mathbf{z}}(\omega_{i})\colon i=1,\ldots,d\}. $$ 

(b) If\{ $ \alpha_{i} $:  $ i=1,\ldots,d $ are 1-forms on N, and if the ideal of forms on  $ N \times M $ generated by

 $$ \{\delta\pi_{1}(\alpha_{i})-\delta\pi_{\mathbf{z}}(\omega_{i})\colon i=1,\ldots,d\} $$ 

is a differential ideal, then given $n_{0}\in N$ and $m_{0}\in M$ there exists a neighborhood $U$ of $n_{0}$ and a $C^{\infty}$ map $f\colon U\to M$ such that $f(n_{0})=m_{0}$ and such that

(3)

 $$ \delta f(\omega_{i})=\alpha_{i}\left|\begin{matrix}U\end{matrix}\right.\quad(i=1,\ldots,d). $$ 

Moreover, if $U$ is any connected open set containing $n_{0}$ for which there exists a $C^{\infty}$ map $f: U \to M$ satisfying both $f(n_{0}) = m_{0}$ and equation (3), then there exists a unique such map on $U$.

##### EXERCISES

1 Supply the proofs of 2.2(a)–(e).

2 (a) Show that homogeneous tensors are generally not decomposable.

(b) Show that if $\dim V \leq 3$, then every homogeneous element in $\Lambda(V)$ is decomposable.

(c) Let $\dim V > 3$. Give an example of an indecomposable homogeneous element of $\Lambda(V)$.

(d) Let  $ \alpha $ be a differential form. Is  $ \alpha \wedge \alpha \equiv 0 $?

3 Supply the proofs of 2.6(a)–(c).

4 Derive the formulas (2), (3), and (4) of 2.10.

5 Prove that  $ L_{x}f = Xf $ whenever  $ f \in C^{\infty}(M) $ and X is a  $ C^{\infty} $ vector field on M.

6 Let $X$ and $Y$ be $C^\infty$ vector fields on $M$ with corresponding local 1-parameter groups $X_t$ and $Y_t$. Let $m \in M$, and let

 $$ \beta(t)={\cal Y}_{-\sqrt{t}}{\cal X}_{-\sqrt{t}}{\cal Y}_{\sqrt{t}}{\cal X}_{\sqrt{t}}(m) $$ 

for $t$ in $(-\varepsilon,\varepsilon)$, for a sufficiently small $\varepsilon$.

Prove that

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//8925e1a1-a96e-4197-88b1-329c8d936f85/markdown_1/imgs/img_in_image_box_565_283_791_420.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A12Z%2F-1%2F%2Fa90b4a9efca45fd8ceacf0a0596bb2b25378f520cc79c0148d263569fe082181" alt="Image" width="23%" /></div>


 $$ \left[X,Y\right]\big|_{m}f=\operatorname*{l i m}_{t\rightarrow0}\frac{f\big(\beta(t)\big)-f\big(\beta(0)\big)}{t}. $$ 

If $\beta(t)$ were a smooth curve at $t=0$, then the right-hand side of (1) would simply be the effect of the tangent vector to $\beta$ at $t=0$ applied to the function $f$. However, because of the $\sqrt{t}$, $\beta$ is not generally smooth at $t=0$. Thus the existence of the limit in (1) is part of the problem, and the problem asserts that this curve $\beta$, even though it is not smooth at $t=0$, defines a tangent vector in $M_m$ in the usual way, and this vector is precisely $[X,Y]|_{m}$.

7 Prove 2.25(e).

8 Let $M$ be connected, and let $\pi: M \times N \to N$ be the natural projection. Prove that a $p$-form $\omega$ on $M \times N$ is $\delta\pi(\alpha)$ for some $p$-form $\alpha$ on $N$ if and only if $i(X)\omega = 0$ and $L_{X}\omega = 0$ for every vector field $X$ on $M \times N$ for which $d\pi(X(m,n)) = 0$ at each point $(m,n) \in M \times N$.

9 Prove that the elements  $ v_{1}, \ldots, v_{r} $ of the vector space V are linearly independent if and only if  $ v_{1} \wedge \cdots \wedge v_{r} \neq 0 $.

10 Prove that linearly independent sets $\{v_1, \ldots, v_r\}$ and $\{w_1, \ldots, w_r\}$ are bases of the same $r$-dimensional subspace of a vector space $V$ if and only if $v_1 \wedge \cdots \wedge v_r = cw_1 \wedge \cdots \wedge w_r$ where necessarily $c \neq 0$; and in this case, $c = \det A$ where $A = (a_{ij})$ and $v_i = \sum a_{ij}w_i$.

11 Let $\mathcal{I}$ be an ideal of forms on $M$ locally generated by $r$ independent 1-forms. Say $\mathcal{I}$ is generated by $\omega_{1},\ldots,\omega_{r}$ on $U$. Then the condition that $\mathcal{I}$ be a differential ideal is equivalent to each of:

(a)  $ d\omega_i = \sum_j \omega_{ij} \wedge \omega_j $ for some 1-forms  $ \omega_{ij} $ (for each such  $ (U, \omega_1, \ldots, \omega_r) $).

(b) If  $ \omega = \omega_1 \wedge \cdots \wedge \omega_r $, then  $ d\omega = \alpha \wedge \omega $ for some 1-form  $ \alpha $ (for each such  $ (U, \omega_1, \ldots, \omega_r) $).

12 Let $V$ be an $n$-dimensional vector space, and let $l$ be a linear transformation on $V$. Since $\Lambda_n(V)$ is one-dimensional, the linear transformation which $l$ induces on $\Lambda_n(V)$ is simply multiplication by a constant. Define the determinant of $l$ to be this constant. If $A$ is an $n \times n$ matrix, let $v_1, \ldots, v_n$ be a basis of $V$, and let $l$ be the linear transformation on $V$ whose matrix with respect to this basis is $A$. Then define the determinant of $A$ to be the determinant of $l$. Prove that the determinant of $A$ does not depend on the basis $v_1, \ldots, v_n$ chosen. Using this definition, derive the standard properties of determinants. For example, derive the expansion

 $$ \det A=\sum_{\pi}(\operatorname{sgn}\pi)a_{1\pi(1)}\cdots a_{n\pi(n)} $$ 

where  $ A=(a_{ij}) $,  $ \mathrm{sgn}\pi $ is the sign of the permutation  $ \pi $, and  $ \pi $ runs over all permutations on n letters. Prove also that the determinant of the product of two matrices is the product of their determinants.

13 Let $V$ be an $n$-dimensional real inner product space. We extend the inner product from $V$ to all of $\Lambda(V)$ by setting the inner product of elements which are homogeneous of different degrees equal to zero, and by setting

 $$ \langle w_{1}\wedge\cdots\wedge w_{p},v_{1}\wedge\cdots\wedge v_{p}\rangle=\operatorname*{d e t}\langle w_{i},v_{j}\rangle $$ 

and then extending bilinearly to all of $\Lambda_{p}(V)$. Prove that if $e_{1},\ldots,e_{n}$ is an orthonormal basis of $V$, then the corresponding basis 2.6(1) of $\Lambda(V)$ is an orthonormal basis for $\Lambda(V)$.

Since $\Lambda_{n}(V)$ is one-dimensional, $\Lambda_{n}(V) - \{0\}$ has two components. An orientation on $V$ is a choice of a component of $\Lambda_{n}(V) - \{0\}$. If $V$ is an oriented inner product space, then there is a linear transformation

 $$ *:\Lambda(V)\to\Lambda(V), $$ 

called $star$, which is well-defined by the requirement that for any orthonormal basis $e_{1},\ldots,e_{n}$ of $V$ (in particular, for any re-ordering of a given basis),

 $$ \begin{align*}*(1)&=\pm e_{1}\wedge\cdots\wedge e_{n},\qquad*(e_{1}\wedge\cdots\wedge e_{n})=\pm1,\\&\quad*(e_{1}\wedge\cdots\wedge e_{p})=\pm e_{p+1}\wedge\cdots\wedge e_{n},\end{align*} $$ 

where one takes “+” if  $ e_1 \wedge \cdots \wedge e_n $ lies in the component of  $ \Lambda_n(V) - \{0\} $ determined by the orientation and “−” otherwise.

Observe that

 $$ \ast\colon\Lambda_{p}(V)\to\Lambda_{n-p}(V). $$ 

## 80 Tensors and Differential Forms

Prove that on  $ \Lambda_{p}(V) $,

 $$ **=(-1)^{g(n-y)}. $$ 

Also prove that for arbitrary $v, w \in \Lambda_{g}(V)$, their inner product is given by

(6)

 $$ \langle v,w\rangle=\ast(w\wedge\ast v)\ast=\ast(v\wedge\ast w). $$ 

14 Let $V$ be a real inner product space, as in Exercise 13. Let $\gamma: \Lambda_{p+1}(V) \to \Lambda_p(V)$ be the adjoint of left exterior multiplication by $\xi \in V$. That is,

 $$ \langle\gamma(v),w\rangle=\langle v,\xi\wedge w\rangle $$ 

for  $ v \in \Lambda_{p+1}(V) $ and  $ w \in \Lambda_p(V) $. Prove that

 $$ \gamma(v)=(-1)^{n v}*\big(\xi\wedge(*v)\big). $$ 

15 Let  $ \xi \in V $. Prove that the composition

 $$ \Lambda_{p}(V)\xrightarrow{\xi\land}\Lambda_{p+1}(V)\xrightarrow{\xi\land}\Lambda_{p+3}(V) $$ 

of left exterior multiplication by $\xi$ with itself is an exact sequence; that is, the image of the first map is the kernel of the second.

16 Cartan Lemma Let $p \leq d$, and let $\omega_{1}, \ldots, \omega_{p}$ be 1-forms on $M^{d}$ which are linearly independent pointwise. Let $\theta_{1}, \ldots, \theta_{p}$ be 1-forms on $M$ such that

 $$ \sum_{i=1}^{p}\theta_{i}\wedge\omega_{i}=0. $$ 

Prove that there exist $C^{\infty}$ functions $A_{ij}$ on $M$ with $A_{ij}=A_{ji}$ such that

 $$ \theta_{i}=\sum_{j=1}^{p}A_{i j}\omega_{j}\qquad(i=1,\ldots,p). $$ 

Lie groups are without doubt the most important special class of differentiable manifolds. Lie groups are differentiable manifolds which are also groups and in which the group operations are smooth. Well-known examples include the general linear group, the unitary group, the orthogonal group, and the special linear group.

In this chapter we shall set the foundations for the study of Lie groups. Of central importance for Lie theory is the relationship between a Lie group and its Lie algebra of left invariant vector fields. We shall study the correspondence between subgroups and subalgebras and between homomorphisms of Lie groups and homomorphisms of their Lie algebras. We shall study the properties of the exponential mapping which is a generalization to arbitrary Lie groups of the exponentiation of matrices and which provides a key link between a Lie group and its Lie algebra. We shall investigate the adjoint representation, shall prove the closed subgroup theorem, and shall consider basic properties and examples of homogeneous manifolds. Along the way we shall derive many properties of the classical linear groups.

##### LIE GROUPS AND THEIR LIE ALGEBRAS

3.1 Definition A Lie group $G$ is a differentiable manifold which is also endowed with a group structure such that the map $G \times G \to G$ defined by $(\sigma, \tau) \mapsto \sigma\tau^{-1}$ is $C^\infty$.

Throughout this chapter, G and H will denote Lie groups, and we shall universally use e to denote the identity element of a Lie group.

### 3.2 Remarks

(a) Let $G$ be a Lie group. Then the map $\tau \mapsto \tau^{-1}$ is $C^\infty$ since it is the composition $\tau \mapsto (e, \tau) \mapsto \tau^{-1}$ of $C^\infty$ maps. Also, the map $(\sigma, \tau) \mapsto \sigma\tau$ of $G \times G \to G$ is $C^\infty$ since it is the composition $(\sigma, \tau) \mapsto (\sigma, \tau^{-1}) \mapsto \sigma\tau$ of $C^\infty$ maps.

(b) The identity component of a Lie group is itself a Lie group; and the components of a Lie group are mutually diffeomorphic.

(c) Since we have included second countability in the definition 1.4 of differentiable manifold, Lie groups for us will always be second countable. In particular, they can have at most countably many components. It should be observed, however, that if second countability is dropped from the definition of Lie group, then connected Lie groups (hence also those with countably many components) would still be second countable. We leave the proof of this as an exercise. You will need to use the fact that a connected Lie group is the union of powers of any neighborhood of its identity (see 3.18).

### 3.3 Examples of Lie Groups

(a) The Euclidean space  $ R^{*} $ is a Lie group under vector addition.

(b) The non-zero complex numbers  $ C^{*} $ form a Lie group under multiplication.

(c) The unit circle  $ S^{1} \subset C^{*} $ is a Lie group with the multiplication induced from  $ C^{*} $.

(d) The product $G \times H$ of two Lie groups is itself a Lie group with the product manifold structure and the direct product group structure; that is, $(\sigma_{1},\tau_{1})(\sigma_{2},\tau_{2}) = (\sigma_{1}\sigma_{2},\tau_{1}\tau_{2})$.

(e) The $n$-torus $T^{n}$ ($n$ an integer $>0$) is the Lie group which is the product of the Lie group $S^{1}$ with itself $n$ times.

(f) The manifold $Gl(n,\mathbb{R})$ of all $n\times n$ non-singular real matrices is a Lie group under matrix multiplication.

(g) The set of all super-triangular $n \times n$ real matrices (all entries below the diagonal are zero) is a Lie group under matrix multiplication.

(h) Let $\mathbb{R}^{*}$ denote the non-zero real numbers, and let $K$ be the product manifold $\mathbb{R}^{*} \times \mathbb{R}$. With a group structure on $K$ defined by

 $$ (s,t)(s_{1},t_{1})=(s s_{1}\;,\;s t_{1}+t), $$ 

K becomes a Lie group. This Lie group is the group of affine motions of  $ \mathbb{R} $, for if we identify the element  $ (s,t) $ of K with the affine motion  $ x \mapsto sx + t $, then the multiplication in K is composition of affine motions.

(i) Let $K$ be the product manifold $GI(n,\mathbb{R}) \times \mathbb{R}^n$. We define a group structure on $K$ by setting $(A,v)(A_1,v_1)=(AA_1,Av_1+v)$. With this group structure, $K$ becomes a Lie group. This Lie group is the group of affine motions of $\mathbb{R}^n$, for if we identify the element $(A,v)$ of $K$ with the affine motion $x \mapsto Ax + v$ of $\mathbb{R}^n$, then the multiplication in $K$ is composition of affine motions.

## 84 Lie Groups

3.4 Definition A Lie algebra g over  $ \mathbb{R} $ is a real vector space g together with a bilinear operator [, ]:  $ g \times g \to g $ (called the bracket) such that for all x, y, z  $ \in $ g,

 $$ [x,y]=-[y,x]. $$ 

(anti-commutativity)

(b)

 $$ [[x,y],z]+[[y,z],x]+[[z,x],y]=0. $$ 

(Jacobi identity)

The importance of the concept of Lie algebra is that there is a special finite dimensional Lie algebra intimately associated with each Lie group, and that properties of the Lie group are reflected in properties of its Lie algebra. We shall see, for example, that the connected, simply connected Lie groups are completely determined (up to isomorphism) by their Lie algebras. The study of these Lie groups then reduces in large part to a study of their Lie algebras.

### 3.5 Examples of Lie Algebras

(a) The vector space of all smooth vector fields on the manifold M forms a Lie algebra under the Lie bracket operation on vector fields.

(b) Any vector space becomes a Lie algebra if all brackets are set equal to 0. Such a Lie algebra is called abelian.

(c) The vector space  $ \mathrm{gl}(n,\mathbb{R}) $ of all  $ n \times n $ real matrices forms a Lie algebra if we set

 $$ [A,B]=A B-B A. $$ 

(d) A 2-dimensional vector space with basis x, y becomes a Lie algebra if we set

 $$ [x,x]=[y,y]=0\qquad\mathrm{a n d}\qquad[x,y]=y,\quad\therefore\quad\forall x\in\mathcal{X}. $$ 

and extend bilinearly.

(e)  $ R^{3} $ with the bilinear operation  $ X \times Y $ of the vector cross product is a Lie algebra.

The proof that the above are Lie algebras is left to the reader as an exercise.

3.6 Definitions Let $\sigma \in G$. Left translation by $\sigma$ and right translation by $\sigma$ are respectively the diffeomorphisms $l_{\sigma}$ and $r_{\sigma}$ of $G$ defined by

 $$ \begin{aligned}{}&{{}l_{\sigma}(\tau)=\sigma\tau,}\\ {}&{{}r_{\sigma}(\tau)=\tau\sigma}\\ \end{aligned} $$ 

for all $\tau \in G$. If $V$ is a subset of $G$, we denote $r_e(V)$ and $l_e(V)$ by $V\sigma$ and $\sigma V$ respectively. A vector field $X$ (not assumed a priori to be smooth) on $G$ is called left invariant if for each $\sigma \in G$, $X$ is $l_e$-related to itself; that is,

 $$ d l_{e}\circ x=x\circ l_{e}. $$ 

The set of all left invariant vector fields on a Lie group G will be denoted by the corresponding lowercase German letter g.

3.7 Proposition Let G be a Lie group and g its set of left invariant vector fields.

(a) g is a real vector space, and the map $\alpha: \mathfrak{g} \to G_e$ defined by $\alpha(X) = X(e)$ is an isomorphism of g with the tangent space $G_e$ to G at the identity. Consequently, $\dim \mathfrak{g} = \dim G_e = \dim G$.

(c) The Lie bracket of two left invariant vector fields is itself a left invariant vector field.

(b) Left invariant vector fields are smooth.

(d) g forms a Lie algebra under the Lie bracket operation on vector fields.

PROOF That g is a real vector space and that $\alpha$ is linear is clear. $\alpha$ is injective, for if $\alpha(X) = \alpha(Y)$, then for each $\sigma \in G$

 $$ X(\sigma)=d l_{\sigma}\big(X(e)\big)=d l_{\sigma}\big(Y(e)\big)=Y(\sigma); $$ 

hence $X = Y$. Moreover, $\alpha$ is surjective; for if $x \in G_e$, we let $X(\sigma) = dl_\sigma(x)$ for each $\sigma \in G$. Then $\alpha(X) = x$, and $X$ is left invariant since

 $$ X(\tau\sigma)=d l_{\tau\sigma}(x)=d l_{\tau}d l_{\sigma}(x)=d l_{\tau}\big(X(\sigma)\big) $$ 

for all  $ \sigma $ and  $ \tau $ in G. This proves part (a).

For (b), let  $ X \in g $, and let  $ f \in C^\infty(G) $. We need only show that  $ X f \in C^\infty(G) $. Now,

 $$ X f(\sigma)=X_{\sigma}f=d l_{\sigma}(X_{e})f=X_{e}(f\circ l_{\sigma}). $$ 

Thus we need to show that $\sigma \mapsto X_e(f \circ l_\sigma)$ is a $C^\infty$ function on $G$. We do this by exhibiting this function as a suitable composition of $C^\infty$ maps. Let $\varphi: G \times G \to G$ denote group multiplication, $\varphi(\sigma, \tau) = \sigma\tau$. And let $i_\sigma^1$ and $i_\sigma^2$ be the maps of $G \to G \times G$ defined by

 $$ \begin{aligned}{}&{{}i_{e}{}^{1}(\tau)=(\tau,e),}\\ {}&{{}i_{o}{}^{2}(\tau)=(\sigma,\tau).}\\ \end{aligned} $$ 

Let $Y$ be any $C^\infty$ vector field on $G$ such that $Y(e) = X(e)$. Then $(0,Y)$ is a smooth vector field on $G \times G$, and $[(0,Y)(f \circ \varphi)] \circ i_e^1$ is a $C^\infty$ function on $G$. Using part (d) of Exercise 24, Chapter 1, we obtain

 $$ \begin{aligned}{[(0,Y)(f\circ\varphi)]\circ i_{e}^{1}(\sigma)}&{{}=(0,Y)_{(\sigma,e)}(f\circ\varphi)}\\ {}&{{}=0_{\sigma}(f\circ\varphi\circ i_{e}^{1})+Y_{e}(f\circ\varphi\circ i_{\sigma}^{2})}\\ {}&{{}=X_{e}(f\circ\varphi\circ i_{\sigma}^{2})=X_{e}(f\circ l_{\sigma}).}\\ \end{aligned} $$ 

Thus $\sigma \mapsto X_{e}(f \circ I_{\sigma})$ is a smooth function on $G$, which proves part (b).

Since, by (b), left invariant vector fields are smooth, their Lie brackets are defined. Now, if $X$ is $l_{\sigma}$-related to itself, and $Y$ is $l_{\sigma}$-related to itself, then according to 1.55, $[X,Y]$ is $l_{\sigma}$-related to $[X,Y]$. Thus the Lie bracket of two left invariant vector fields is again a left invariant vector field. Part (d) is now an immediate consequence of 1.45.

3.8 Definition We define the Lie algebra of the Lie group G to be the Lie algebra g of left invariant vector fields on G. Alternatively, we could take as the Lie algebra of G the tangent space  $ G_{s} $ at the identity with Lie algebra structure induced by requiring the vector space isomorphism 3.7(a) of g with  $ G_{s} $ to be an isomorphism of Lie algebras. It will be convenient at times to consider the Lie algebra from this alternate point of view. In particular, we shall see (3.10 and 3.37) that the Lie algebras of the classical groups admit particularly nice interpretations in terms of their tangent spaces at the identity.

3.9 Remarks on Vector Spaces as Manifolds In 1.5(b) we observe that any finite dimensional real vector space $V$ is, in a natural way, a differentiable manifold. Let $\{e_i\}$ be a basis of $V$, and let $\{r_i\}$ be the dual basis. Now let $p \in V$. Then there is a natural identification of the tangent space $V_p$, to $V$ at $p$ with $V$ itself, given by

 $$ \left.\Sigma a_{i}\frac{\partial}{\partial r_{i}}\right\vert_{p}\leftrightarrow\left.\Sigma a_{i}e_{i}.\right. $$ 

It is easily seen that this identification is independent of the basis chosen. We shall often make use of this identification in describing tangent vectors to a vector space as elements of the vector space itself. In particular, if $\sigma(t)$ is a smooth curve in $V$, then

 $$ \dot{\sigma}(t_{0})=\operatorname*{l i m}_{t\to t_{0}}\frac{\sigma(t)-\sigma(t_{0})}{t-t_{0}}. $$ 

### 3.10 Examples of Lie Groups and Their Lie Algebras

(a) The real line  $ \mathbb{R} $ is a Lie group under addition. The left invariant vector fields are simply the constant vector fields  $ \{\lambda(d/dr): \lambda \in \mathbb{R}\} $. The bracket of any two such vector fields is 0.

(b) The General Linear Group. The set  $ \mathrm{gl}(n, \mathbb{R}) $ of all  $ n \times n $ real matrices is a real vector space of dimension  $ n^2 $. Matrices are added and multiplied by scalars componentwise. As we have already remarked,  $ \mathrm{gl}(n, \mathbb{R}) $ becomes a Lie algebra if we set  $ [A, B] = AB - BA $.

The general linear group $GI(n,\mathbb{R})$ inherits its manifold structure as the open subset of $gl(n,\mathbb{R})$ where the determinant function does not vanish, and is a Lie group under matrix multiplication. Let $x_{i}$ be the global coordinate function on $gl(n,\mathbb{R})$ which assigns to each matrix

its $ijth$ entry. Then if $\sigma, \tau \in Gl(n, \mathbb{R})$, $x_{ij}(\sigma\tau^{-1})$ is a rational function of $\{x_{kl}(\sigma)\}$ and $\{x_{kl}(\tau)\}$ with non-zero denominator, which proves that the map $(\sigma, \tau) \to \sigma\tau^{-1}$ is $C^\infty$.

Now let $g$ be the Lie algebra of $GI(n,\mathbb{R})$. Let $\alpha: \mathrm{gl}(n,\mathbb{R})_e \to \mathrm{gl}(n,\mathbb{R})$ be the canonical identification of the tangent space to $\mathrm{gl}(n,\mathbb{R})$ at the identity matrix $e$ with $\mathrm{gl}(n,\mathbb{R})$ itself. Thus for $v \in \mathrm{gl}(n,\mathbb{R})_e$,

 $$ \alpha(v)_{i j}=v(x_{i j}). $$ 

Then since $Gl(n,\mathbb{R})_{e}=gl(n,\mathbb{R})_{e}$, we have a natural map $\beta\colon\mathfrak{g}\to\mathfrak{gl}(n,\mathbb{R})$ defined by

 $$ \beta(X)=\alpha\bigl(X(e)\bigr). $$ 

We claim that $\beta$ is a Lie algebra isomorphism, and in this way we consider $\mathrm{gl}(n,\mathbb{R})$ to be the Lie algebra of $Gl(n,\mathbb{R})$. $\beta$ is clearly a vector space isomorphism. We need only show that

 $$ \beta([X,Y])=[\beta(X),\beta(Y)] $$ 

whenever $X, Y \in \mathfrak{g}$. Now,

 $$ (x_{i j}\circ l_{\sigma})(\tau)=x_{i j}(\sigma\tau)=\sum_{k}x_{i k}(\sigma)x_{k j}(\tau). $$ 

Since Y is a left invariant vector field,

 $$ \begin{aligned}{\big(Y(x_{i j})\big)(\sigma)}&{{}={d}l_{e}(Y_{e})(x_{i j})=Y_{e}(x_{i j}\circ l_{\sigma})}\\ {}&{{}=\sum_{k}x_{i k}(\sigma)Y_{e}(x_{k j})=\sum_{k}x_{i k}(\sigma)\alpha(Y_{e})_{k j}}\\ {}&{{}=\sum_{k}x_{i k}(\sigma)\beta(Y)_{k j}.}\\ \end{aligned} $$ 

Using (5), we now compute the  $ ijth $ component of  $ \beta([X,Y]) $:

 $$ \begin{aligned}{\beta([X,Y])_{i j}}&{{}=[X,Y]_{\sigma}(x_{i j})=X_{\sigma}\big(Y(x_{i j})\big)-Y_{\sigma}\big(X(x_{i j})\big)}\\ {}&{{}=\sum_{k}\left\{X_{\sigma}(x_{i k})\beta(Y)_{k j}-Y_{\sigma}(x_{i k})\beta(X)_{k i}\right\}}\\ {}&{{}=\sum_{k}\left\{\beta(X)_{i k}\beta(Y)_{k j}-\beta(Y)_{i k}\beta(X)_{k j}\right\}}\\ {}&{{}=[\beta(X),\beta(Y)]_{i j}.}\\ \end{aligned} $$ 

Hence $\beta$ is a Lie algebra isomorphism.

(c) Let $V$ be an $n$-dimensional real vector space. Let $\mathrm{End}(V)$ denote the set of all linear operators on $V$ (the set of endomorphisms of $V$), and let $\mathrm{Aut}(V) \subset \mathrm{End}(V)$ denote the subset of non-singular operators (the automorphisms). $\mathrm{End}(V)$ is a real vector space of dimension $n^{2}$, and it becomes a Lie algebra if we set

 $$ [I_{1},I_{2}]=I_{1}\circ I_{2}-I_{2}\circ I_{1}. $$ 

(7)

A basis of $V$ determines a diffeomorphism of $\mathrm{End}(V)$ with $\mathrm{gl}(n, \mathbb{R})$ sending $\mathrm{Aut}(V)$ onto $GI(n, \mathbb{R})$. It follows that $\mathrm{Aut}(V)$ inherits a manifold structure as an open subset of $\mathrm{End}(V)$ and is a Lie group under composition. Under the natural identification of $\mathrm{End}(V)$ with $\mathrm{End}(V)_e = \mathrm{Aut}(V)_e$ (where $e$ denotes the identity transformation on $V$), $\mathrm{End}(V)$ inherits a Lie algebra structure from the Lie algebra of $\mathrm{Aut}(V)$. This induced Lie algebra structure is precisely the one described in (7).

(d) Let $\mathrm{gl}(n,\mathbb{C})$ denote the set of all $n\times n$ complex matrices, and let $G\mathrm{l}(n,\mathbb{C})\subset\mathrm{gl}(n,\mathbb{C})$ be the subset of non-singular ones. $G\mathrm{l}(n,\mathbb{C})$ is known as the complex general linear group. $\mathrm{gl}(n,\mathbb{C})$ is a $2n^{2}$-dimensional real vector space, with a basis consisting of the matrices $\delta_{ij}$ and $\sqrt{-1}\delta_{ij}(i,j=1,\ldots,n)$ where $\delta_{ij}$ is the matrix all of whose entries are zero except for a $1$ in the $ij$th spot; and $\mathrm{gl}(n,\mathbb{C})$ forms a Lie algebra if we set $[A,B]=AB-BA$. $G\mathrm{l}(n,\mathbb{C})$ inherits a manifold structure as an open subset of $\mathrm{gl}(n,\mathbb{C})$ and is a Lie group under matrix multiplication. With considerations entirely analogous to those in Example (b), one sees that the natural identification of the Lie algebra of $G\mathrm{l}(n,\mathbb{C})$ with $\mathrm{gl}(n,\mathbb{C})$ is a Lie algebra isomorphism. Thus we may consider $\mathrm{gl}(n,\mathbb{C})$ as the Lie algebra of $G\mathrm{l}(n,\mathbb{C})$.

(e) Similarly, in analogy with Example (c), if $V$ is a complex $n$-dimensional vector space, and if $\mathrm{End}(V)$ denotes the set of complex linear transformations of $V$, and $\mathrm{Aut}(V) \subset \mathrm{End}(V)$ denotes the non-singular ones, then $\mathrm{Aut}(V)$ is a $2n^{2}$-dimensional Lie group with Lie algebra $\mathrm{End}(V)$.

### 3.11 Definition A form  $ \omega $ on G is called left invariant if

 $$ \delta l_{a}\omega=\omega $$ 

for each $\sigma \in G$. As in the case of left invariant vector fields, it is not necessary to assume that left invariant forms are smooth, for smoothness is a consequence of the left invariance. We shall denote the vector space of left invariant $p$-forms on $G$ by $E_{l \operatorname{inv}}^{\bullet}(G)$, and we let

 $$ E_{l^{*}_{\mathrm{i n v}}}(G)=\sum_{p=0}^{\mathrm{d i m}G}E_{l\mathrm{i n v}}^{p}(G). $$ 

Left invariant 1-forms are also known as Maurer-Cartan forms.

The following proposition is the analog for left invariant forms of 3.7. The proofs are straightforward, and we leave them to the reader as an exercise.

### 3.12 Proposition

(a) Left invariant forms are smooth.

(b) $E^{*}_{1\mathrm{inv}}(G)$ is a subalgebra of the algebra $E^{*}(G)$ of all smooth forms on $G$, and the map $\omega \to \omega(e)$ is an algebra isomorphism of $E^{*}_{1\mathrm{inv}}(G)$ onto $\Lambda(G_e^*)$. In particular, this map gives a natural isomorphism of $E^1_{1\mathrm{inv}}(G)$ with $G_e^*$ and hence with $g^*$. (In this way we shall consider $E^1_{1\mathrm{inv}}(G)$ as the dual space of the Lie algebra of $G$.)

(c) If $\omega$ is a left invariant 1-form and $X$ a left invariant vector field, then $\omega(X)$ is a constant function on $G$, and this constant is precisely the effect $\omega$ has on $X$ when $\omega$ is considered as an element of the dual space of $g$ as in part (b). (We shall consider $\omega(X)$ either as a constant function on $G$ or as the corresponding real number, the particular choice depending on the context.)

(d) If  $ \omega \in E_{\ell_{\mathrm{inv}}}^{1}(G) $ and  $ X, Y \in \mathfrak{g} $, then it follows from 2.25(f) that

 $$ d\omega(X,Y)=-\omega[X,Y]. $$ 

(e) Let $\{X_{1}, \ldots, X_{d}\}$ be a basis of g with dual basis $\{\omega_{1}, \ldots, \omega_{d}\}$ for $E_{l\text{inv}}^{1}(G)$. Then there exist constants $c_{ijk}$ such that

 $$ [X_{i},X_{j}]=\sum_{k=1}^{d}c_{i j k}X_{k}. $$ 

(The $c_{ijk}$ are called the structural constants of $G$ with respect to the basis $\{X_{i}\}$ of g.) They satisfy

(3)

 $$ \begin{array}{c}{c_{i j k}+c_{j i k}=0,}\\ {\sum_{r}(c_{i j r}c_{r k s}+c_{j k r}c_{r i e}+c_{k i r}c_{r j e})=0.}\\ \end{array} $$ 

The exterior derivatives of the $\omega_{i}$ are given by the Maurer-Cartan equations

 $$ d\omega_{i}=\sum_{j<k}c_{j k i}\omega_{k}\wedge\omega_{j}. $$ 

##### HOMOMORPHISMS

3.13 Definitions A map $\varphi: G \to H$ is a (Lie group) homomorphism if $\varphi$ is both $C^\infty$ and a group homomorphism of the abstract groups. We call $\varphi$ an isomorphism if, in addition, $\varphi$ is a diffeomorphism. An isomorphism of a Lie group with itself is called an automorphism. If $H = \text{Aut}(V)$ for some vector space $V$, or if $H = \text{Gl}(n, \mathbb{C})$ or $\text{Gl}(n, \mathbb{R})$, then a homomorphism $\varphi: G \to H$ is called a representation of the Lie group $G$.

If $g$ and $b$ are Lie algebras, a map $\psi: g \to b$ is a (Lie algebra) homomorphism if it is linear and preserves brackets $(\psi[X,Y]=[\psi(X),\psi(Y)]$ for all $X,Y\in g)$. If, in addition, $\psi$ is 1:1 and onto, then $\psi$ is an isomorphism. An isomorphism of $g$ with itself is called an automorphism. If $b=\mathrm{End}(V)$ for some vector space $V$, or if $b=\mathrm{gl}(n,\mathbb{C})$ or $\mathrm{gl}(n,\mathbb{R})$, then a homomorphism $\psi: g \to b$ is called a representation of the Lie algebra $g$.

Let $\varphi: G \to H$ be a homomorphism. Then since $\varphi$ maps the identity of $G$ to the identity of $H$, the differential $d\varphi$ of $\varphi$ is a linear transformation of $G_e$ into $H_e$. By means of the natural identifications of the tangent spaces at the identities with the Lie algebras, this linear transformation $d\varphi$ of $G_e$ into $H_e$ induces a linear transformation of $g$ into $b$ which we shall denote also by $d\varphi$. Thus

 $$ d\varphi\colon{\mathfrak{g}}\to{\mathfrak{b}}, $$ 

where if $X \in g$, then $d\varphi(X)$ is the unique left invariant vector field on $H$ such that

 $$ d\varphi(X)(e)=d\varphi\bigl(X(e)\bigr). $$ 

3.14 Theorem Let G and H be Lie groups with Lie algebras g and h respectively, and let $\varphi: G \to H$ be a homomorphism. Then

(a) $X$ and $d\varphi(X)$ are $\varphi$-related for each $X\in\mathfrak{g}$.

(b)  $ d\varphi: \mathfrak{g} \to \mathfrak{h} $ is a Lie algebra homomorphism.

PROOF Let  $ \tilde{X} = d\varphi(X) $. Then  $ \tilde{X} $ and  $ X $ are  $ \varphi $-related. For since  $ \varphi $ is a homomorphism,  $ l_{\varphi(\sigma)} \circ \varphi = \varphi \circ l_{\sigma} $; hence

 $$ \begin{aligned}{\tilde{X}\big(\varphi(\sigma)\big)}&{{}=d l_{\varphi(\sigma)}\tilde{X}(e)=d l_{\varphi(\sigma)}d\varphi\big(X(e)\big)}\\ {}&{{}=d(l_{\varphi(\sigma)}\circ\varphi)X(e)=d(\varphi\circ l_{\sigma})X(e)=d\varphi\big(X(\sigma)\big).}\\ \end{aligned} $$ 

This proves part (a). Now let $X, Y \in \mathfrak{g}$. Then for part (b), we must show that

 $$ [\widetilde{X,Y}]=[\widetilde{X},\widetilde{Y}]. $$ 

By 1.55, [X,Y] is  $ \varphi $-related to the left invariant vector field  $ [\tilde{X},\tilde{Y}] $. In particular,

 $$ [\tilde{X},\tilde{Y}](e)=d\varphi\big([X,Y](e)\big). $$ 

But  $ [X,Y] $, by Definition 3.13(2), is the unique left invariant vector field on H whose value at the identity is  $ d\phi([X,Y](e)) $. Thus (2) holds, and the theorem is proved.

3.15 Effect of Homomorphisms on Left Invariant Forms Let  $ \varphi: G \to H $ be a homomorphism. Then  $ \delta\varphi $ pulls left invariant forms on H back to left invariant forms on G, since whenever  $ \omega $ is a left invariant form

on H,

 $$ \begin{aligned}{\delta I_{\sigma}\delta\varphi(\omega)}&{{}=\delta(\varphi\circ l_{\sigma})\omega=\delta(l_{\varphi(\sigma)}\circ\varphi)\omega}\\ {}&{{}=\delta\varphi\dot{\varrho}l_{\varphi(\sigma)}(\omega)=\delta\varphi(\omega).}\\ \end{aligned} $$ 

Moreover, the mapping $\delta\varphi\colon E_{\ell_{\mathrm{inv}}}^{\ell}(H)\to E_{\ell_{\mathrm{inv}}}^{\ell}(G)$, considered as a mapping of the dual space of $\mathfrak{h}$ to the dual space of $\mathfrak{g}$, is precisely the transpose of $d\varphi\colon\mathfrak{g}\to\mathfrak{h}$; that is,

 $$ \big(\delta\varphi(\omega)\big)(X)=\omega\big(d\varphi(X)\big)\qquad\big(\omega\in E_{l\operatorname{l n}\mathtt{v}}^{1}(H);\quad X\in\mathfrak{g}\big). $$ 

Recall that if $\{\omega_1, \ldots, \omega_d\}$ is a basis of $E_{\mathrm{inv}}^{t}(H)$, then there are structural constants $\{c_{ijk}\}$ (see 3.12(4)) such that

 $$ \bar{d}\omega_{i}=\sum_{j<k}c_{j k i}\omega_{k}\wedge\omega_{j}. $$ 

Thus since $d$ and $\delta\phi$ commute,

 $$ \bar{d}\big(\delta\varphi(\omega_{i})\big)=\sum_{j<k}c_{j k i}\;\delta\varphi(\omega_{k})\wedge\delta\varphi(\omega_{j}). $$ 

Now let $\pi_{1}$ and $\pi_{2}$ be the canonical projections of $G \times H$ onto $G$ and $H$ respectively. Then the ideal $\mathcal{J}$ of forms on $G \times H$ generated by the collection of independent 1-forms

 $$ \{\delta\pi_{1}\delta\varphi(\omega_{i})-\delta\pi_{2}(\omega_{i})\colon i=1,\ldots,d\} $$ 

is a differential ideal; for using (4), we obtain for each i,

 $$ \begin{aligned}{d\big(\delta\pi_{1}\delta\varphi(\omega_{i})}&{{}-\delta\pi_{\mathtt{z}}(\omega_{i})\big)}\\ {}&{{}=\sum_{j<k}c_{j k i}\big(\delta\pi_{1}\delta\varphi(\omega_{k})\wedge\delta\pi_{1}\delta\varphi(\omega_{j})-\delta\pi_{\mathtt{z}}(\omega_{k})\wedge\delta\pi_{\mathtt{z}}(\omega_{j})\big)}\\ {}&{{}=\sum_{j<k}c_{j k i}[\{\delta\pi_{1}\delta\varphi(\omega_{k})-\delta\pi_{\mathtt{z}}(\omega_{k})\}\wedge\delta\pi_{1}\delta\varphi(\omega_{j})}\\ {}&{{}\quad+\delta\pi_{\mathtt{z}}(\omega_{k})\wedge\{\delta\pi_{1}\delta\varphi(\omega_{j})-\delta\pi_{\mathtt{z}}(\omega_{j})\}],}\\ \end{aligned} $$ 

which belongs to the ideal $\mathcal{J}$. Moreover, observe that the 1-forms (5) generating the differential ideal $\mathcal{J}$ are themselves left invariant 1-forms on $G \times H$. This follows immediately from applying $\delta l_{(\sigma,\xi)}$ to the forms (5), where $(\sigma,\xi)\in G\times H$, and from using the fact that $\pi_1\circ l_{(\sigma,\xi)}=l_\sigma\circ\pi_1$ and $\pi_2\circ l_{(\sigma,\xi)}=l_\xi\circ\pi_2$. Note also that the basis $\{\omega_i\}$ of $E^1_{l_\mathrm{inv}}(H)$ is a basis of the 1-forms on $H$ in the sense of 2.33.

To carry out the above construction of a differential ideal on $G \times H$, it is sufficient to start simply with a homomorphism of the Lie algebras rather than a homomorphism of the Lie groups. Let $G$ and $H$ be Lie groups, and let $\psi: g \to h$ be a homomorphism of their Lie algebras. $\psi$ has a transpose $\psi^*: E_{l_{\text{inv}}}^1(H) \to E_{l_{\text{inv}}}^1(G)$, namely,

 $$ \big(\psi^{*}(\omega)\big)(X)=\omega\big(\psi(X)\big)\qquad\big(\omega\in E_{l\operatorname{i n v}}^{1}(H);X\in\mathfrak{g}\big). $$ 

## 92 Lie Groups

Let $\{\omega_i\}$ be a basis of $E_{\ell,\mathbf{i}\mathbf{n}\mathbf{v}}^(H)$. Then we claim that the ideal $\mathcal{I}$ of forms on $G \times H$ generated by the collection of independent 1-forms

 $$ \{\delta\pi_{1}(\psi^{*}(\omega_{i}))-\delta\pi_{2}(\omega_{i})\colon i=1,\cdots,d\} $$ 

is a differential ideal. This follows from a computation similar to (6) together with the observation that

 $$ d\bigl(\psi^{*}(\omega_{i})\bigr)=\sum_{j<k}c_{j k i}\psi^{*}(\omega_{k})\wedge\psi^{*}(\omega_{j}). $$ 

To prove (9), it suffices to prove that both sides have the same effect on an arbitrary pair X, Y of left invariant vector fields on G:

 $$ \begin{aligned}{d\big(\psi^{*}(\omega_{i})\big)(X,Y)}&{{}=-\psi^{*}(\omega_{i})[X,Y]=-\omega_{i}[\psi(X),\psi(Y)]}\\ {}&{{}=d\omega_{i}\big(\psi(X),\psi(Y)\big)}\\ {}&{{}=\sum_{j<k}c_{j k i}\omega_{k}\wedge\omega_{j}\big(\psi(X),\psi(Y)\big)}\\ {}&{{}=\sum_{j<k}c_{j k i}\psi^{*}(\omega_{k})\wedge\psi^{*}(\omega_{j})(X,Y).}\\ \end{aligned} $$ 

Here the first and third equalities follow from 3.12(1). Finally, observe that, in this case also, the forms (8) are left invariant on  $ G \times H $.

We shall make use of these ideals on  $ G \times H $ in proving existence and uniqueness of homomorphisms in various situations.

3.16 Theorem Let G be connected, and let $\varphi$ and $\psi$ be homomorphisms of G into $H$ such that the Lie algebra homomorphisms $d\varphi$ and $d\psi$ of $\mathfrak{g}$ into $h$ are identical. Then $\varphi = \psi$.

PROOF Since  $ d\varphi = d\psi $, we have

 $$ \begin{array}{r}{\delta\varphi=\delta\psi\colon E_{l\mathrm{i n v}}^{1}(H)\to E_{l\mathrm{i n v}}^{1}(G).}\end{array} $$ 

Thus we have two $C^\infty$ maps $\varphi$ and $\psi$ of the connected manifold $G$ into $H$, both agreeing at $e\in G$, and both having the same effect of pulling back a basis of 1-forms from $H$. Thus since the ideal of forms on $G\times H$ generated by the 1-forms 3.15(5) is a differential ideal, it follows from 2.34(b) that $\varphi=\psi$.

##### LIE SUBGROUPS

3.17 Definitions $(H,\varphi)$ is a Lie subgroup of the Lie group $G$ if

(a) H is a Lie group;

(b)  $ (H,\varphi) $ is a submanifold of G;

(c)  $ \varphi\colon H \to G $ is a group homomorphism.

 $ (H,\varphi) $ is called a closed subgroup of G if, in addition,  $ \varphi(H) $ is a closed subset of G.

Let g be a Lie algebra. A subspace $\mathfrak{h} \subset \mathfrak{g}$ is a subalgebra if $[X, Y] \in \mathfrak{h}$ whenever $X, Y \in \mathfrak{h}$. A subalgebra $\mathfrak{h} \subseteq \mathfrak{g}$ clearly forms a Lie algebra under the bracket induced from $\mathfrak{g}$.

Let $(H,\varphi)$ be a Lie subgroup of $G$, and let $\mathfrak{h}$ and $g$ be their respective Lie algebras. Then $d\varphi$ gives an isomorphism of $\mathfrak{h}$ with the subalgebra $d\varphi(\mathfrak{h})$ of $g$.

Various theorems assert the existence of unique subgroups satisfying certain conditions, and as in the case of submanifolds (1.33 is pertinent), uniqueness needs a little explanation in view of our definition of subgroup. We will consider two subgroups $(H,\varphi)$ and $(H_{1},\varphi_{1})$ of $G$ equivalent if there exists a Lie group isomorphism $\alpha: H \to H_{1}$ such that $\varphi_{1} \circ \alpha = \varphi$. This is an equivalence relation on the Lie subgroups of $G$, and uniqueness for Lie subgroups means uniqueness up to this equivalence. As in the case of submanifolds (see 1.33), each equivalence class of Lie subgroups of $G$ has a unique representative of the form $(A,i)$, where $A$ is a subset of $G$ which is an abstract subgroup of $G$ and which has a manifold structure (not necessarily with the relative topology) making $A$ into a Lie group such that the inclusion $i: A \to G$ yields a submanifold and hence a Lie subgroup of $G$. When we wish to consider a subgroup of $G$ in this latter form (i.e. as an actual subset of $G$) we usually drop any reference to a mapping and speak simply of the Lie subgroup $A$ of $G$, the inclusion map being understood. Also, we usually identify the Lie algebra $a$ of $A$ with $di(a)$ and simply speak of the Lie algebra of $A$ as a subalgebra of the Lie algebra of $G$. In particular, we identify a left invariant vector field $X$ on $A$ with the left invariant vector field $di(X)$ on $G$ with which it is inclusion-related.

We are now going to prove one of the fundamental theorems of Lie group theory, which asserts that there is a 1:1 correspondence between connected Lie subgroups of a Lie group and subalgebras of its Lie algebra. But first, we will need the following proposition.

3.18 Proposition Let G be a connected Lie group, and let U be a neighborhood of e. Then

 $$ G=\bigcup_{n=1}^{\infty}U^{n} $$ 

where $U^{n}$ consists of all $n$-fold products of elements of $U$. (We say that $U$ generates $G$)

PROOF Let $V$ be an open subset of $U$ containing $e$ such that $V = V^{-1}$ (where $V^{-1} = \{\sigma^{-1}: \sigma \in V\}$). For example, $V = U \cap U^{-1}$ will do. Let

 $$ H=\bigcup_{n=1}^{\infty}V^{n}\subset\bigcup_{n=1}^{\infty}U^{n}. $$ 

## 94 Lie Groups

Then $H$ is an abstract subgroup of $G$ and is an open subset of $G$ since $\sigma \in H$ implies $\sigma V \subset H$. Thus each coset mod $H$ is open in $G$. Now, $H$ is the complement in $G$ of the union of all the cosets mod $H$ different from $H$ itself. Therefore $H$ is also a closed subset of $G$. Since $G$ is connected, and $H$ is also non-empty, $H$ must be all of $G$. This together with (2) implies (1).

3.19 Theorem Let $G$ be a Lie group with $L_{ie}$ algebra $\mathfrak{g}$, and let $\widetilde{\mathfrak{h}} \subset \mathfrak{g}$ be a subalgebra. Then there is a unique connected $L_{ie}$ subgroup $(H, \varphi)$ of $G$ such that $d\varphi(\mathfrak{h}) = \widetilde{\mathfrak{h}}$.

PROOF We define a distribution D on G by setting

 $$ \mathcal{D}(\sigma)=\{X(\sigma)\colon X\in\tilde{\mathfrak{h}}\} $$ 

for each $\sigma \in G$. Let $\dim \widetilde{b} = d$. Then $\mathcal{D}$ is of dimension $d$. $\mathcal{D}$ is smooth since $\mathcal{D}$ is globally spanned by a basis $X_1, \ldots, X_d$ for $\widetilde{b}$. Moreover, $\mathcal{D}$ is involutive, since if $X$ and $Y$ are vector fields lying in $\mathcal{D}$, then there are $C^\infty$ functions $\{a_i\}$ and $\{b_i\}$ on $G$ such that $X = \sum a_i X_i$ and $Y = \sum b_i X_i$, and thus

 $$ [X,Y]=\sum_{i,j=1}^{d}\{a_{i}b_{j}[X_{i},X_{j}]+a_{i}X_{i}(b_{j})X_{j}-b_{j}X_{j}(a_{i})X_{i}\}, $$ 

which again is a vector field in D since b is a subalgebra of g.

Let $(H,\varphi)$ be a maximal connected integral manifold of $\mathcal{D}$ through $e$ (see 1.64). Let $\sigma\in\varphi(H)$. Since $\mathcal{D}$ is invariant under left translations, $(H,I_{\varphi^{-1}}\circ\varphi)$ is also an integral manifold of $\mathcal{D}$ through $e$. Thus by the maximality, $I_{\varphi^{-1}}\circ\varphi(H)\subset\varphi(H)$. Therefore if $\sigma\in\varphi(H)$ and $\tau\in\varphi(H)$, then also $\sigma^{-1}\tau\in\varphi(H)$. It follows that $\varphi(H)$ is an abstract subgroup of $G$. Thus we can induce a group structure on $H$ so that $\varphi:H\to G$ is a homomorphism of abstract groups. It remains only to check that $H$ is a Lie group, that is, the map $\alpha:H\times H\to H$ where $\alpha(\sigma,\tau)=\sigma\tau^{-1}$ is $C^\infty$. Now, the map $\beta:H\times H\to G$ sending $(\sigma,\tau)\mapsto\varphi(\sigma)\varphi(\tau)^{-1}$ is $C^\infty$, and we have the following commutative diagram:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//ffebdd2f-6528-4bab-9626-b1ae4d195e35/markdown_1/imgs/img_in_image_box_353_929_594_1061.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2F5579a5192fcc53383e627fb14132deec748a33a7dd6e5b90ef21520b16d92bbb" alt="Image" width="24%" /></div>


Since $(H,\varphi)$ is an integral manifold of an involutive distribution on $G$, it follows from 1.62 that $\alpha$ is $C^\infty$. Thus $(H,\varphi)$ is a Lie subgroup of $G$; and if $\mathfrak{h}$ is the Lie algebra of $H$, clearly $d\varphi(\mathfrak{h})=\widetilde{\mathfrak{h}}$.

For uniqueness, let $(K,\psi)$ be another connected Lie subgroup of $G$ with $d\psi(\mathfrak{f})=\widetilde{\mathfrak{h}}$. Then $(K,\psi)$ must also be an integral manifold of $\mathcal{D}$ through $e$. By the maximality of $(H,\varphi)$, $\psi(K)\subset\varphi(H)$, and there is uniquely determined a map $\eta$ such that $\varphi\circ\eta=\psi$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//ffebdd2f-6528-4bab-9626-b1ae4d195e35/markdown_2/imgs/img_in_image_box_399_221_592_346.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A14Z%2F-1%2F%2Ffa10b9d31e6cc1b49acfdd65e35b8e6718be5acabab8c05b076e59997080172a" alt="Image" width="20%" /></div>


$\eta$ is smooth by 1.62, and consequently is an injective Lie group homomorphism. Moreover, $\eta$ is everywhere non-singular; in particular, $\eta$ is a diffeomorphism on a neighborhood of the identity, and therefore is surjective by 3.18. Thus $\eta$ is a Lie group isomorphism, and the subgroups $(K,\psi)$ and $(H,\varphi)$ are equivalent. This proves uniqueness.

Corollary (a) There is a 1:1 correspondence between connected Lie subgroups of a Lie group and subalgebras of its Lie algebra.

Corollary (b) Let $(H,\varphi)$ be a Lie subgroup of $G$. Then if $\tilde{H}$ is a component of $H$, $(\tilde{H},\varphi|\tilde{H})$ is a maximal connected integral manifold of the involutive distribution on $G$ determined by the subalgebra $d\varphi(h)$ of $g$.

We can restate the content of part of the proof of Theorem 3.19 in terms of differential ideals on G as follows (cf. Exercise 6):

Corollary (c) Suppose that the ideal $\mathcal{I}$ generated by a collection $\{\omega_1, \ldots, \omega_{c-d}\}$ of independent left invariant 1-forms on a Lie group $G^c$ is a differential ideal. Then the maximal connected integral manifold $I^a$ of $\mathcal{I}$ through $e \in G$ is a Lie subgroup of $G$.

The following theorem should be compared with the situation for submanifolds (see 1.33).

3.20 Theorem If an abstract subgroup $A$ of a Lie group $G$ has a manifold structure (that is, a second countable locally Euclidean topology together with a differentiable structure) which makes $(A,i)$ into a submanifold of $G$, where $i$ is the inclusion map, then it has a unique such manifold structure, and in this manifold structure, $A$ is a Lie group, and hence $(A,i)$ is a Lie subgroup of $G$.

PROOF We show first that in any such manifold structure, $A$ is a Lie group. Let $\mathcal{D}$ be the distribution on $G$ determined by left translations of the tangent space to $A$ at the identity. We claim that $(A,i)$ is an integral manifold of $\mathcal{D}$ through the identity $e\in G$.

We caution that this is not evident and that its proof requires a little care. The problem is that if $\gamma(t)$ is a smooth curve in $A$, and if $\sigma$ lies in $A$, then $I_{\sigma} \circ \gamma(t)$ is a smooth curve in $G$ which lies in $A$ but apriori may no longer be smooth in $A$. Thus it could be that there are elements of $\mathcal{D}(\sigma)$ which are not tangent vectors to $A$. We must show that this cannot occur. Let $\dim A = k$. If for some $\sigma \in A$ the tangent space $A_{\sigma}$ is not contained in $\mathcal{D}(\sigma)$, then we can find $k + 1$ curves which are smooth in $G$, lie in $A$, and have independent tangent vectors at $\sigma$. Translating to the identity, we have curves $\gamma_{1}(t), \ldots, \gamma_{k+1}(t)$ which are smooth in $G$, lie in $A$, pass through $e$ at $t = 0$, and have independent tangent vectors there. Notice that this is not yet a contradiction. For example, there are two smooth curves in the plane $\mathbb{R}^{k}$ with independent tangent vectors at the origin and lying in the one-dimensional figure-8 submanifold (see 1.31). Now consider the map

 $$ (t_{1},\ldots,t_{k+1})\mapsto\gamma_{1}(t_{1})\cdot\cdot\cdot\gamma_{k+1}(t_{k+1}). $$ 

This map is non-singular at the origin, thus is a diffeomorphism of a neighborhood of the origin in $\mathbb{R}^{k+1}$ into $G$, and has its image contained in $A$ since the individual curves $\gamma_t$ lie in $A$, and $A$ is a subgroup. The map (5) can be extended to a diffeomorphism of a neighborhood of the origin in $\mathbb{R}^*$ with a neighborhood $U$ of the identity in $G$, where $n = \dim G$. Composing the inverse of this diffeomorphism with the inclusion $I: A \to G$, we obtain a $C^\infty$ immersion of the open submanifold $U \cap A$ of $A$ into $\mathbb{R}^*$ with image containing an open set in $\mathbb{R}^{k+1} \subset \mathbb{R}^*$. This now contradicts the fact that $A$ is second countable and has dimension $k$. (See Exercise 6, Chapter 1.) Thus $A_e = D(\sigma)$ for each $\sigma \in A$ and consequently $(A, i)$ is an integral manifold of $\mathcal{D}$.

It follows that for any $\sigma\in G$, $(A,I_{e})$ is an integral manifold of $\mathcal{D}$ through $\sigma$. Thus by 1.59, $\mathcal{D}$ is an involutive distribution; and now it follows from an argument as in 3.19(3) that the map $(\sigma,\tau)\to\sigma\tau^{-1}$ of $A\times A\to A$ is $C^{\infty}$, which proves that $A$ is a Lie group. Now suppose that we have two manifold structures on $A$ for which $(A,i)$ is a submanifold. Denote $A$ with these manifold structures by $A_{1}$ and $A_{2}$ respectively. Then $(A_{1},i)$ and $(A_{2},i)$ are both integral manifolds of involutive distributions on $G$; hence 1.62 applied to the commutative diagram

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//ffebdd2f-6528-4bab-9626-b1ae4d195e35/markdown_3/imgs/img_in_image_box_365_968_576_1111.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A14Z%2F-1%2F%2F900ea5643cf10391db1b5dc8d21d62d53722b0ad471a3371d6c05bfb8a173dab" alt="Image" width="21%" /></div>


implies that the identity map id: $A_{1} \to A_{2}$ is a diffeomorphism. Thus there is a unique such manifold structure on $A$.

Hence if a subset of a Lie group can be made into a Lie subgroup under the inclusion map, it can be made so in one and only one way—the group structure, topology, and differentiable structure are uniquely determined. Consequently, it is unambiguous to assert that a subset A of a Lie group G is a Lie subgroup of G. This means that A is an abstract subgroup of G and has a manifold structure (and hence a unique one) making A into a Lie group and  $ (A,i) $ into a Lie subgroup of G.

We are now in a position to describe exactly in which situation a Lie subgroup $A \subseteq G$ has the relative topology.

3.21 Theorem Let $(H^{a},\varphi)$ be a Lie subgroup of $G^{c}$. Then $\varphi$ is an imbedding (that is, $\varphi$ is a homeomorphism of $H$ with $\varphi(H)$ in the relative topology) if and only if $(H,\varphi)$ is a closed subgroup of $G$ (that is, $\varphi(H)$ is closed in $G$).

PROOF Assume that $\varphi(H)$ is closed in $G$. It suffices to prove that there is some non-empty open set $V \subset H$ such that $\varphi \mid V$ is a homeomorphism of $V$ into $\varphi(H)$ where $\varphi(H)$ has the relative topology. For then it follows from the fact that $\varphi$ commutes with left translations $(\varphi \circ I_e) = I_{\varphi(e)} \circ \varphi)$ that $\varphi$ is an imbedding on all of $H$. By 3.19, Corollary (b), and by 1.60, there exists a cubic-centered coordinate system $(U, \tau)$ about $e \in G$ such that $\varphi(H) \cap U$ consists of a union (at most countable) of slices of the form

 $$ \tau_{i}=\mathtt{c o n s t a n t}\qquad\mathrm{f o r~a l l~}i\in\{d+1,\ldots,c\}, $$ 

including at least the slice through $e$. Let $C$ be a closed subset of $U$ containing $e$ whose image under $\tau$ is a cube, and let $S$ be the slice of $C$ given by

 $$ \tau_{1}=0,\ldots,\tau_{d}=0. $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//343ed485-5e7c-4aa2-bb5c-9fdcbe4c76d3/markdown_0/imgs/img_in_image_box_343_810_737_1070.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A26Z%2F-1%2F%2F63c6189a67f6512423681626fc5c196ea04e43dc63042e7b5f1771fc9cb92c51" alt="Image" width="41%" /></div>


Then  $ \tau(\varphi(H) \cap S) $ is a non-empty, closed, countable subset of  $ \mathbb{R}^{c-d} $. Now, any closed countable subset of Euclidean space must have an isolated point. Otherwise, such a set with the induced metric would be a

complete metric space representable as a countable union of nowhere dense sets, which is impossible according to the Baire category theorem [27]. Thus there is an isolated slice, call it $S_0$, among the collection of slices $\varphi(H) \cap U$; and thus $\varphi^{-1}(S_0)$ is an open subset of $H$ on which $\varphi$ gives an imbedding into $\varphi(H)$.

Conversely, suppose that $\varphi$ is an imbedding. Let $\{\sigma_i\}$ be a sequence of points in $\varphi(H)$ converging to the point $\sigma \in G$. Since $\varphi$ is an imbedding, there exists a cubic coordinate system $(U, \tau)$ about the identity $e \in G$ such that $\varphi(H) \cap U$ consists of a single slice—call it $S$. Choose neighborhoods $V \subset W \subset U$ of the identity, cubic relative to $\tau$, so that $V^{-1}V \subset W \subset U$. Since $\sigma_i \to \sigma$, there is an $N$ sufficiently large so that $\sigma_n \in \sigma V$ for $n \geq N$. Therefore $\sigma_N^{-1} \sigma_n \in \overline{W}$ for $n \geq N$. Also $\sigma_N^{-1} \sigma_n \in \varphi(H)$. Thus $\sigma_N^{-1} \sigma_n \in S \cap \overline{W}$ and converges to $\sigma_N^{-1} \sigma$ which therefore must also lie in $S \cap \overline{W}$. Therefore $\sigma_N^{-1} \sigma \in \varphi(H)$. Hence $\sigma \in \varphi(H)$, and thus $\varphi(H)$ is closed.

##### COVERINGS

We shall assume that the reader has some familiarity with the notions of homotopy, fundamental group, simple connectivity, and covering space. In Theorem 3.23 we state three of the fundamental facts on covering spaces which we shall need. The proofs are sketched in Exercise 7 at the end of this chapter. Details of the proofs and additional facts on covering spaces may be found, for example, in [26] or [28].

3.22 Definition Before stating Theorem 3.23, we recall a few definitions and establish some notation. We let  $ \pi_1(X, x_0) $ denote the fundamental group of the topological space  $ X $ with base point  $ x_0 \in X $. We let  $ \pi \colon (X, x_0) \to (Y, y_0) $ denote a mapping of the topological space  $ X $ into the topological space  $ Y $ sending the base point  $ x_0 $ in  $ X $ to the base point  $ y_0 $ in  $ Y $, and we denote the corresponding induced homomorphism of the fundamental groups by  $ \pi_* \colon \pi_1(X, x_0) \to \pi_1(Y, y_0) $.

We shall assume connectedness in the definition of "simply connected." That is, we shall assume a simply connected space X to be a connected topological space whose fundamental group is trivial.

A continuous surjection $\pi: X \to Y$ is called a covering if $X$ is a connected, locally pathwise connected (each neighborhood of a point contains a pathwise connected neighborhood of that point) topological space, and if each point $y \in Y$ has a neighborhood $V$ whose inverse image under $\pi$ is a disjoint union of open sets in $X$ each homeomorphic with $V$ under $\pi$. Such neighborhoods $V$ in $Y$ are called evenly covered. If $\pi: X \to Y$ is a covering, then $Y$ is called the base of the covering, and $X$ is called the covering space.

A topological space Y is called semi-locally 1-connected if each point $y \in Y$ has a neighborhood U such that each loop based at $y$ and lying in U is homotopic in Y, through loops based at $y$, to the constant loop.

### 3.23 Theorem

(a) Let $\pi: (X, x_0) \to (Y, y_0)$ be a covering. Let $Z$ be a pathwise connected and locally pathwise connected topological space, and let $\alpha: (Z, z_0) \to (Y, y_0)$ be a continuous map such that $\alpha_*(\pi_1(Z, z_0)) \subset \pi_*(\pi_1(X, x_0))$. Then there exists a unique continuous map $\tilde{\alpha}: (Z, z_0) \to (X, x_0)$ such that $\pi \circ \tilde{\alpha} = \alpha$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//343ed485-5e7c-4aa2-bb5c-9fdcbe4c76d3/markdown_2/imgs/img_in_image_box_353_266_620_408.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A28Z%2F-1%2F%2Fda85c451b29eee72a6a95b0cc50e4950995d64ddfd7f7021a6dca8ff682511e8" alt="Image" width="28%" /></div>


(b) If X is a pathwise connected, locally pathwise connected, and semilocally 1-connected topological space, then X has a simply connected covering space.

(c) If  $ \pi: X \to Y $ is a covering and Y is simply connected, then  $ \pi $ is a homeomorphism.

3.24 Simply Connected Covering Group Let $\pi: \overrightarrow{M} \to M$ be a covering of a differentiable manifold $M$. Then $\overrightarrow{M}$ is automatically a locally Euclidean, second countable (cf. Exercise 8) Hausdorff space, and there is a unique differentiable structure on $\overrightarrow{M}$ for which the covering map $\pi$ is $C^\infty$ and non-singular. This differentiable structure is obtained simply by requiring that the local homeomorphisms obtained from $\pi$ over evenly covered open sets be diffeomorphisms.

Now let $G$ be a connected Lie group. By $3.23(b)$, $G$ has a covering $\pi: \tilde{G} \to G$ with $\tilde{G}$ simply connected. As we have observed, $\tilde{G}$ has a unique differentiable structure for which $\pi$ is $C^\infty$ and non-singular. We shall now show that a group structure can be induced in $\tilde{G}$ making $\tilde{G}$ into a Lie group and making $\pi$ into a Lie group homomorphism. Consider the map $\alpha: \tilde{G} \times \tilde{G} \to G$ such that $\alpha(\tilde{\sigma}, \tilde{\tau}) = \pi(\tilde{\sigma}) \pi(\tilde{\tau})^{-1}$. Choose $\tilde{\varepsilon} \in \pi^{-1}(e)$. Since $\tilde{G} \times \tilde{G}$ is simply connected, it follows from $3.23(a)$ that a unique mapping $\tilde{\alpha}: \tilde{G} \times \tilde{G} \to \tilde{G}$ exists such that $\pi \circ \tilde{\alpha} = \alpha$ and such that $\tilde{\alpha}(\tilde{\varepsilon}, \tilde{\varepsilon}) = \tilde{\varepsilon}$. For $\tilde{\sigma}$ and $\tilde{\tau}$ in $\tilde{G}$ we define

 $$ \tilde{\tau}^{-1}=\tilde{\alpha}(\tilde{e},\tilde{\tau}),\quad\tilde{\sigma}\tilde{\tau}=\tilde{\alpha}(\tilde{\sigma},\tilde{\tau}^{-1}). $$ 

It follows easily from applications of the uniqueness part of 3.23(a) that $\tilde{\sigma}\tilde{e}=\tilde{e}\tilde{\sigma}=\tilde{\sigma}$, for the maps $\tilde{\sigma}\mapsto\tilde{\sigma}\tilde{e}$, $\tilde{\sigma}\mapsto\tilde{e}\tilde{\sigma}$, and $\tilde{\sigma}\mapsto\tilde{\sigma}$ of $\tilde{G}\to\tilde{G}$ all make the following diagram commute, and they all send $\tilde{e}$ to $\tilde{e}$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//343ed485-5e7c-4aa2-bb5c-9fdcbe4c76d3/markdown_2/imgs/img_in_image_box_377_1064_567_1211.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A29Z%2F-1%2F%2Fabcae376d155f555a4f06c1037dd33ff6a2ff002b327be87f46a58564b18fb96" alt="Image" width="19%" /></div>


Thus since $\tilde{G}$ is simply connected, it follows from the uniqueness in 3.23(a) that these maps are all identical. Similarly, if follows that $\tilde{\sigma}\tilde{\sigma}^{-1}=\tilde{\sigma}^{-1}\tilde{\sigma}=\tilde{\varepsilon}$, and that $(\tilde{\sigma}\tilde{\tau})\tilde{\gamma}=\tilde{\sigma}(\tilde{\tau}\tilde{\gamma})$ for all $\tilde{\sigma},\tilde{\tau},\tilde{\gamma}\in\tilde{G}$, Thus (1) makes $\tilde{G}$ into an abstract group; and since $\tilde{\alpha}$ is smooth, $\tilde{G}$ is a Lie group. Also, (1) implies that $\pi(\tilde{\tau}^{-1})=\pi(\tilde{\tau})^{-1}$ and that $\pi(\tilde{\sigma}\tilde{\tau})=\pi(\tilde{\sigma})\pi(\tilde{\tau})$; hence $\pi:\tilde{G}\to G$ is a Lie group homomorphism. Thus we have proved the following.

3.25 Theorem Each connected Lie group has a simply connected covering space which is itself a Lie group such that the covering map is a Lie group homomorphism.

3.26 Proposition Let G and H be connected Lie groups, and let $\varphi: G \to H$ be a homomorphism. Then $\varphi$ is a covering map if and only if $d\varphi: G_s \to H_s$ is an isomorphism.

PROOF Suppose first that $\varphi$ is a covering. Then $d\varphi \mid G_{\epsilon}$ must be injective. Otherwise, since $\varphi$ is a homomorphism, $d\varphi$ would have a nontrivial kernel at each point of $G$, and these kernels would form an involutive distribution on $G$, whose integral manifolds are collapsed to points under $\varphi$. Thus $\varphi$ would nowhere be locally one-to-one, contradicting the covering property. $d\varphi \mid G_{\epsilon}$ must also be surjective, for otherwise $(G,\varphi)$ would locally be a proper submanifold of $H$, again contradicting the local homeomorphism property of a covering. Thus $d\varphi:G_{\epsilon}\to H_{\epsilon}$ is an isomorphism.

Conversely, suppose that $d\varphi:G_{s}\to H_{s}$ is an isomorphism. Then $\varphi$ is everywhere a local diffeomorphism. Thus, by 3.18, $\varphi$ maps $G$ onto $H$ since $\varphi$ is a homomorphism and since $\varphi(G)$ contains a neighborhood of the identity in the connected Lie group $H$. $G$ certainly is pathwise and locally pathwise connected, so to prove that $\varphi$ is a covering map, it only remains to show that each point of $H$ is contained in an evenly covered neighborhood. Let

 $$ D=\ker\varphi=\varphi^{-1}(e). $$ 

Then since $\varphi$ is a local diffeomorphism, $D$ is a discrete normal subgroup of $G$, where “discrete” means that if $\sigma \in D$, then there is an open set $V$ in $G$ such that $V \cap D = \sigma$. Since $(\sigma, \tau) \mapsto \sigma^{-1} \tau$ is a continuous (in fact $C^\infty$) map of $G \times G \to G$, there exists a neighborhood $V$ of $e$ in $G$ such that

 $$ (V^{-1}V)\cap D=e. $$ 

We claim that $\varphi(V)$ is a neighborhood of $e$ in $H$, evenly covered by $\varphi$. First, $\varphi\big|V$ is $1:1$, since if $\sigma,\tau\in V$ and $\varphi(\sigma)=\varphi(\tau)$, then $\varphi(\sigma^{-1}\tau)=e$, whence $\sigma^{-1}\tau=e$ by (2), and thus $\sigma=\tau$. Moreover, $d\varphi$ is an isomorphism at each point of $G$. Thus $\varphi\big|V$ is a diffeomorphism of $V$ with the open neighborhood $\varphi(V)$ of $e$ in $H$. Now, we claim that

 $$ \varphi^{-1}\bigl(\varphi(V)\bigr)=\bigcup_{\theta\in D}V\theta. $$ 

The inclusion $\supset$ is obvious. To prove $\subset$, suppose that $\varphi(\sigma) \in \varphi(V)$. Then there exists $\tau \in V$ such that $\varphi(\tau) = \varphi(\sigma)$. Hence $\tau^{-1}\sigma \in D$ and $\sigma \in V\tau^{-1}\sigma$, proving (3). Finally, $V\theta_1 \cap V\theta_2 = \varnothing$ if $\theta_1 \neq \theta_2 \in D$, for if $\sigma \in V\theta_1 \cap V\theta_2$ then $\sigma = \tau\theta_1 = \eta\theta_2$ for some $\tau$, $\eta \in V$. Then $\tau^{-1}\eta \in D$ and $\tau^{-1}\eta \in V^{-1}V$; thus, by (2), $\tau = \eta$, which implies that $\theta_1 = \theta_2$. Thus $\varphi(V)$ is an evenly covered neighborhood of $e \in H$. It follows that $\varphi(\sigma V)$ is an open neighborhood of $\varphi(\sigma)$ in $H$, evenly covered by the disjoint union of the open sets $\sigma V\theta$ for $\theta \in D$. Thus $\varphi$ is a covering.

##### SIMPLY CONNECTED LIE GROUPS

3.27 Theorem Let G and H be Lie groups with Lie algebras g and h respectively and with G simply connected. Let $\psi: \mathfrak{g} \to \mathfrak{h}$ be a homomorphism. Then there exists a unique homomorphism $\psi: G \to H$ such that $d\varphi = \psi$.

PROOF Uniqueness was proved in 3.16.

Let $\{\omega_i\}$ be a basis of the left invariant 1-forms on $H$, and let $\psi^*$ be the transpose of $\psi$ (see 3.15(7)). Then according to 3.15, the 1-forms

 $$ \{\delta\pi_{1}\big(\psi^{*}(\omega_{i})\big)-\delta\pi_{2}(\omega_{i})\} $$ 

on $G \times H$ (where $\pi_1$ and $\pi_2$ are the canonical projections of $G \times H$ onto $G$ and $H$ respectively) are left invariant, and the ideal $\mathcal{J}$ which they generate is a differential ideal. Thus by 3.19, Corollary (c), the maximal connected integral manifold $I$ of $\mathcal{J}$ through $(e,e) \in G \times H$ is a Lie subgroup of $G \times H$ with dimension equal to the dimension of $G$. Now, we know from 2.33 that $(\pi_1 \mid I): I \to G$ is non-singular, and therefore by 3.26 is a covering homomorphism. $G$ was assumed to be simply connected; hence by 3.23(c) and the inverse function theorem, $\pi_1 \mid I: I \to G$ is an isomorphism. We define $\varphi: G \to H$ by setting

 $$ \varphi=\pi_{2}\circ(\pi_{1}\mid I)^{-1}. $$ 

Then $\varphi$ is a Lie group homomorphism, and according to 2.33(6),

 $$ \delta\varphi(\omega_{i})=\varphi^{*}(\omega_{i}). $$ 

Thus $d\varphi=\varphi$, and the theorem is proved.

Corollary If simply connected Lie groups G and H have isomorphic Lie algebras, then G and H are isomorphic.

There is a theorem [12, p. 199] due to Ado, which we will not prove, that every Lie algebra has a faithful (1:1) representation in $\mathrm{gl}(n,\mathbb{R})$ for some $n$. As a consequence, if $g$ is a Lie algebra, then there is a Lie group, in particular a simply connected one, with Lie algebra $g$. In view of this we have:

3.28 Theorem There is a one-to-one correspondence between isomorphism classes of Lie algebras and isomorphism classes of simply connected Lie groups.

##### EXPONENTIAL MAP

3.29 Definition A homomorphism $\varphi: \mathbb{R} \to G$ is called a 1-parameter subgroup of $G$.

3.30 Definition Let $G$ be a Lie group, and let $g$ be its Lie algebra. Let $X \in g$. Then

 $$ \lambda\frac{d}{d r}\mapsto\lambda X $$ 

is a homomorphism of the Lie algebra of  $ \mathbb{R} $ into g. Since the real line is simply connected, there exists, by 3.27, a unique 1-parameter subgroup

 $$ \mathtt{e x p}_{\mathtt{X}}\colon\mathbb{R}\to G $$ 

such that

 $$ \begin{array}{r}{d\exp_{\boldsymbol{X}}\Big(\lambda\frac{d}{d r}\Big)=\lambda\boldsymbol{X}.}\end{array} $$ 

In other words, $t \mapsto \exp_{X}(t)$ is the unique 1-parameter subgroup of $G$ whose tangent vector at $0$ is $X(e)$. We define the exponential map

 $$ \mathbf{e x p}\colon\mathfrak{g}\to G $$ 

 $$ \operatorname{e x p}(X)=\operatorname{e x p}_{X}(1). $$ 

by setting

The reason for this terminology will become apparent in 3.35(13), where we show that the exponential map for the general linear group is actually given by exponentiation of matrices.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//008e99d6-8a1d-4188-b841-b6c361e3463a/markdown_1/imgs/img_in_image_box_238_851_657_1180.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A28Z%2F-1%2F%2Fa6f8281712960fc665796099a47d45cd3b98b8fcc49721d945467336be807227" alt="Image" width="42%" /></div>


3.31 Theorem Let $X$ belong to the Lie algebra $g$ of the Lie group $G$. Then

(a)  $ \exp(tX) = \exp_X(t) $ for each  $ t \in \mathbb{R} $.

 $$ \quad\quad(b)\quad\operatorname{e x p}(t_{1}+t_{2})X=(\operatorname{e x p}t_{1}X)(\operatorname{e x p}t_{2}X)\qquad{f o r\quad a l l}t_{1},t_{2}\in\mathbb{R}. $$ 

(c)  $ \exp(-tX) = (\exp tX)^{-1} $ for each  $ t \in \mathbb{R} $.

(d) $\exp: \mathfrak{g} \to G$ is $C^{\infty}$ and $d \exp: \mathfrak{g}_{0} \to G_{*}$ is the identity map (with the usual identifications), so $\exp$ gives a diffeomorphism of a neighborhood of 0 in $\mathfrak{g}$ onto a neighborhood of $e$ in $G$.

(e) $l_{e}\circ\exp_{X}$ is the unique integral curve of $X$ which takes the value $\sigma$ at 0. As a particular consequence, left invariant vector fields are always complete.

(f) The 1-parameter group of diffeomorphisms $X_{t}$ associated with the left invariant vector field $X$ is given by

 $$ X_{t}=r_{\mathrm{e x p}_{X}}(t). $$ 

PROOF By 3.14, $(d/dr)$ and $d\exp_X(d/dr)$, which is $X$, are $\exp_X$ related. Thus $\exp_X$ is an integral curve of $X$ and is the unique one for which $\exp_X(0) = e$. Since $X$ is left invariant, $I_\sigma^\circ \circ \exp_X$ is also an integral curve of $X$ and is the unique one taking the value $\sigma$ at 0. Thus part (e) is proved; and (f) is an immediate consequence of (e). Now define $\mathbf{maps} \varphi$ and $\psi$ of $\mathbb{R}$ into $G$ by setting

 $$ \psi(t)=\exp_{s\mathbf{x}}(t)\qquad\mathrm{a n d}\qquad\varphi(t)=\exp_{x}(s t) $$ 

where $s \in \mathbb{R}$. We have observed that $\psi$ is the unique integral curve of $sX$ such that $\psi(0) = e$. Now,

 $$ d_{\Phi}\left(\frac{d}{d r}\bigg\vert_{t}\right)=d\operatorname{e x p}_{X}\left(s\frac{d}{d r}\bigg\vert_{s t}\right)=s X\big\vert_{\operatorname{e x p}_{X}(s t)}. $$ 

Thus $\varphi$ also is an integral curve of $sX$ such that $\varphi(0)=e$. By the uniqueness (1.48(c)) of integral curves, $\varphi=\psi$. Thus

 $$ \operatorname{e x p}_{s X}(t)=\operatorname{e x p}_{X}(s t)\qquad(s,\;t\in\mathbb{R}\;;\;X\in\mathfrak{g}). $$ 

Setting $t=1$ and changing $s$ to $t$, we obtain part (a). Since $\exp_X$ is a homomorphism of $\mathbb{R}$ into $G$, parts (b) and (c) follow immediately from (a). For part (d), we define a vector field $V$ on $G\times g$ by setting

 $$ V(\sigma,X)=(X(\sigma),0)\in G_{\sigma}\oplus\mathfrak{g}_{X}. $$ 

Then $V$ is a smooth vector field, and according to part (e), the integral curve of $V$ through $(\sigma,X)$ is

 $$ \iota\quad\mapsto\quad(\sigma\exp\iota X,X), $$ 

or in other words, the local 1-parameter group of transformations associated with the vector field V is given by

 $$ V_{t}(\sigma,X)=(\sigma\operatorname{e x p}t X,X). $$ 

In particular, $V$ is complete; hence $V_{1}$ is defined and smooth on all of $G \times g$. Now let $\pi: G \times g$ be the projection onto $G$. Then

 $$ \operatorname{e x p}X=\pi\circ V_{1}(e,X). $$ 

Thus we have exhibited \exp as the composition of  $ C^{\infty} $ mappings, so  $ \exp $ is  $ C^{\infty} $. That  $ d\exp: g_0 \to G_e $ is the identity map is immediate, for  $ tX $ is a curve in g whose tangent vector at  $ t = 0 $ is X, and by part (a),  $ \exp tX $ is a curve in G whose tangent vector at  $ t = 0 $ is  $ X(e) $.

3.32 Theorem Let $\varphi: H \to G$ be a homomorphism, Then the following diagram is commutative:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//008e99d6-8a1d-4188-b841-b6c361e3463a/markdown_3/imgs/img_in_image_box_336_383_573_524.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A30Z%2F-1%2F%2F33b84f688ea60c087ba206f65cfcd86ae40397c67a23afdbecc891ec6c4a4377" alt="Image" width="24%" /></div>


PROOF Let $X\in\mathfrak{h}$. Then $t\mapsto\varphi(\exp tX)$ is a smooth curve in $G$ whose tangent at $0$ is $d\varphi(X(e))$. This is also a 1-parameter subgroup of $G$ since $\varphi$ is a homomorphism. But $t\mapsto\exp t(d\varphi(X))$ is the unique 1-parameter subgroup of $G$ whose tangent at $0$ is $(d\varphi(X))(e)$. Thus

 $$ \varphi(\exp t X)=\exp t\big(d\varphi(X)\big), $$ 

whence

 $$ \varphi(\exp X)=\exp\bigl(d\varphi(X)\bigr). $$ 

3.33 Proposition Let $(H,\varphi)$ be a Lie subgroup of $G$, and let $X\in\mathfrak{g}$. If $X\in d\varphi(\mathfrak{h})$, then $\exp tX\in\varphi(H)$ for all $t$. Conversely, if $\exp tX\in\varphi(H)$ for $t$ in some open interval, then $X\in d\varphi(\mathfrak{h})$.

PROOF If $X\in d\varphi(h)$, then $\exp tX\in\varphi(H)$ for all $t$, according to 3.32. On the other hand, if $\exp tX\in\varphi(H)$ for $t$ in some interval $I$, then for $t\in I$, the map $t\mapsto\exp tX$ can be expressed as a composition $\varphi\circ\alpha$ where $\alpha$, according to 1.62, is a smooth map of $I$ into $H$. Let $t_0\in I$, and let $\tilde{X}$ be the left invariant vector field on $H$ determined by $\dot{\alpha}(t_0)$. Then $d\varphi(\tilde{X})=X$.

3.34 Theorem Let A be an abstract subgroup of a Lie group G, and let a be a subspace of g. Let U be a neighborhood of 0 in g diffeomorphic under the exponential map with a neighborhood V of the identity in G. Suppose that

 $$ \operatorname{e x p}(U\cap a)=A\cap V. $$ 

Then A with the relative topology is a Lie subgroup of G, α is a subalgebra of g, and α is the Lie algebra of A.

PROOF We need only show that in the relative topology, the subgroup $A$ has a differentiable structure such that $(A,i)$ is a submanifold of $G$, where $i$ is the inclusion map. For then, according to 3.20, with this manifold structure (and no other) $A$ is a Lie subgroup of $G$, and it follows from 3.33 that the Lie algebra of $A$ is $a$. Let

 $$ \varphi=\exp\mid U\cap a\colon U\cap a\ \to\ \mathcal{A}\cap V. $$ 

Then the desired differentiable structure on $A$ is the maximal collection of smoothly overlapping coordinate systems containing the collection

 $$ \{(A\cap\sigma V,\varphi^{-1}\circ l_{\sigma^{-1}})\colon\sigma\in A\}. $$ 

### 3.35 Example We shall see that the exponential map

 $$ \mathtt{e x p}\colon\mathrm{g l}(n,\mathbb{C})\;\to\;\mathrm{G l}(n,\mathbb{C}) $$ 

for the complex general linear group is given by exponentiation of matrices. We shall now let $I$ rather than $e$ denote the identity matrix in $Gl(n,\mathbb{C})$. Let

 $$ e^{A}=I+A+\frac{A^{2}}{2!}+\cdots+\frac{A^{j}}{j!}+\cdots $$ 

for $A \in \mathrm{gl}(n, \mathbb{C})$. To see that this makes sense, that is, to see that the right-hand side of (2) converges, observe that in fact the right-hand side of (2) converges uniformly for $A$ in a bounded region of $\mathrm{gl}(n, \mathbb{C})$. For given a bounded region $\Omega$ of $\mathrm{gl}(n, \mathbb{C})$, there is a $\mu > 0$ such that for any matrix $A$ in this region, $|x_{ik}(A)| \leq \mu$ for each component $x_{ik}(A)$ of the matrix $A$. It follows easily by induction that $|x_{ik}(A^f)| \leq n^{(f-1)}\mu^f$. Thus, by the Weierstrass $M$-test, each of the series

 $$ \sum_{j=0}^{\infty}\frac{x_{ik}(A^{j})}{j!}\qquad(1\leq i\leq n;1\leq k\leq n) $$ 

converges uniformly for $A$ in $\Omega$. Thus the right-hand side of (2) converges uniformly for $A$ in $\Omega$.

Now let $S_{i}(A)$ be the $j$th partial sum of the series (2), that is,

 $$ S_{j}(A)=I+A+\frac{A^{2}}{2!}+\cdots+\frac{A^{j}}{j!}, $$ 

and let $B \in \mathrm{gl}(n,\mathbb{C})$. Then since $C \mapsto BC$ is a continuous map of $\mathrm{gl}(n,\mathbb{C})$ into itself, it follows that

 $$ B\left(\operatorname*{l i m}_{j\to\infty}S_{j}(A)\right)=\operatorname*{l i m}_{j\to\infty}\bigl(B S_{j}(A)\bigr). $$ 

In particular, if $B \in G l(n, \mathbb{C})$, then $B\left(\lim_{j \to \infty} S_j(A)\right)B^{-1} = \lim_{j \to \infty} BS_j(A)B^{-1}$, from which it follows that

 $$ B e^{A}B^{-1}=e^{B\Delta B^{-1}}. $$ 

There exists a $B\in G/(n,\mathbb{C})$ such that $BAB^{-1}$ is super-triangular; that is, all entries below the diagonal are zero. (Simply take $B$ to be the inverse of the matrix whose columns $v_1,\ldots,v_n$ are determined as follows: Let $I$ be the linear transformation of $\mathbb{C}^n$ whose matrix with respect to the canonical basis is $A$, let $v_1$ be an eigenvector of $I$, and inductively let $v_{i+1}$ be an eigenvector of $\pi_i\circ I\mid W_i$ where $W_i$ is any complement of the subspace $V_i$ of $C^n$ spanned by $v_1,\ldots,v_i$ and where $\pi_i$ is projection of $\mathbb{C}^n=V_i\oplus W_i$ onto $W_i$. If the diagonal entries of $BAB^{-1}$ are $\lambda_1,\ldots,\lambda_n$, then $e^{BAB^{-1}}$ is also super-triangular, with diagonal entries $e^{\lambda_1},\ldots,e^{\lambda_n}$. In particular, det $e^{BAB^{-1}}\neq0$, so it follows from (6) that

 $$ e^{A}\in\mathbb{G l}(n,\mathbb{C})\quad\mathrm{f o r~e a c h}\quad A\in\mathrm{g l}(n,\mathbb{C}). $$ 

Since the trace of a matrix is the sum of its eigenvalues, and the determinant is the product of its eigenvalues, we have also shown that

 $$ \det e^{A}=e^{\mathrm{t r a c e}A}. $$ 

Next we shall prove that

 $$ e^{A+B}=e^{A}e^{B}\quad\mathrm{i f}\quad A B=B A. $$ 

By definition,  $ e^{A+B} = \lim_{j \to \infty} S_j(A + B) $. It follows from the fact that matrix multiplication gives a continuous map of  $ \mathrm{gl}(n, \mathbb{C}) \times \mathrm{gl}(n, \mathbb{C}) $ into  $ \mathrm{gl}(n, \mathbb{C}) $ that  $ e^A e^B = \lim_{j \to \infty} S_j(A) \cdot S_j(B) $. So to prove (9), it suffices to show that

 $$ \operatorname*{l i m}_{j\to\infty}\left\{S_{j}(A)S_{j}(B)-S_{j}(A+B)\right\}=0. $$ 

Now,

 $$ S_{j}(A)S_{j}(B)-S_{j}(A+B)=\sum\frac{B^{l}A^{k}}{l!k!} $$ 

where the sum is over all integers $l$ and $k$ for which $1 \leq l \leq j$, $1 \leq k \leq j$, and $j + 1 \leq l + k \leq 2j$. If $\mu > 1$ is an upper bound for the absolute value of each of the entries of $A$ and $B$, then it follows that each entry of the right-hand side of (11) is bounded in absolute value by

 $$ \begin{array}{r}{\sum\frac{n^{(i+k-1)}\mu^{(i+k)}}{|I!k!}\leq\frac{(n\mu)^{8j}(j^{8})}{[j/2]!}}\end{array} $$ 

where [j/2] is the greatest integer less than or equal to j/2. The estimate on the right-hand side of (12) goes to zero as $j \to \infty$, which proves (10) and hence proves (9).

Consider the map $t \mapsto e^{t\Delta}$ of $\mathbb{R}$ into $Gl(n,\mathbb{C})$. It is smooth since the real and imaginary components of each entry of $e^{t\Delta}$ are power series in $t$ with infinite radii of convergence. Its tangent vector at $0$ is $A$ (simply differentiate the power series term by term), and this map is a homomorphism by (9).

Thus $t \mapsto e^{t\mathcal{A}}$ is the unique 1-parameter subgroup of $Gl(n,\mathbb{C})$ whose tangent vector at 0 is $A$. So the exponential map (1) for $Gl(n,\mathbb{C})$ is given by exponentiation of matrices:

 $$ \operatorname{e x p}(A)=e^{A}\qquad\big(A\in\operatorname{g l}(n,\mathbb{C})\big). $$ 

If $A \in \mathrm{gl}(n, \mathbb{R})$, then $e^A \in \mathrm{Gl}(n, \mathbb{R})$, and $A \to e^A$ is the exponential map for the real general linear group. Similarly, the exponential map

 $$ \operatorname{e x p}\colon\operatorname{E n d}(V)\;\to\;\operatorname{A u t}(V), $$ 

where $V$ is a real or complex vector space, is given by exponentiation of endomorphisms. If $l \in \mathrm{End}(V)$, then

 $$ \exp(l)=e^{l}=1+l+\frac{l^{2}}{2!}+\cdots+\frac{l^{s}}{j!}+\cdots $$ 

where $l^{\prime\prime}$ means “$l$ composed with itself $j$ times,” and where $l$ is the identity transformation.

3.36 Remarks If $\varphi: G \to \mathrm{Aut}(V)$ is a representation, and $X \in \mathfrak{g}$, then it follows from 3.35(15) and 3.32 that

 $$ \varphi(\exp X)=1+d\varphi(X)+\frac{\left(d\varphi(X)\right)^{8}}{2!}+\cdots, $$ 

and it follows from 3.32 and 3.9(2) that

 $$ d\varphi(X)=\lim_{t\to0}\frac{\varphi(\exp tX)-1}{t}=\left.\frac{d}{dt}\right|_{t=0}(\varphi(\exp tX)). $$ 

3.37 Subgroups of $GI(n,\mathbb{C})$ Using 3.34 and 3.35, we shall now obtain some of the classical Lie subgroups of $GI(n,\mathbb{C})$ by exponentiating subalgebras of $\mathfrak{gl}(n,\mathbb{C})$. We already have one example, namely, $GI(n,\mathbb{R})$ is a closed Lie subgroup of $GI(n,\mathbb{C})$ with Lie algebra $\mathfrak{gl}(n,\mathbb{R}) \subset \mathfrak{gl}(n,\mathbb{C})$. Let $A \in \mathfrak{gl}(n,\mathbb{C})$. Then the transpose of $A$ is the matrix $A^t$ such that $(A^t)_{ij} = A_{ji}$; and the complex conjugate of $A$ is the matrix $\bar{A}$ whose $ij$th entry $(\bar{A})_{ij}$ is the complex conjugate $\overline{A_{ij}}$ of $A_{ij}$. And $n$, of course, is an integer $\geq 1$.

(a) Unitary group

 $$ U(n)=\{A\in G l(n,\mathbb{C})\colon A^{-1}=\overline{{A^{t}}}\}. $$ 

(b) Special linear group

 $$ S l(n,\mathbb{C})=\{A\in G l(n,\mathbb{C})\colon\operatorname*{d e t}A=1\}. $$ 

(c) Complex orthogonal group

 $$ O(n,\mathbb{C})=\{A\in G l(n,\mathbb{C})\colon A^{-1}=A^{\mathfrak{t}}\}. $$ 

Each of these is an abstract subgroup and a closed subset of $GI(n,\mathbb{C})$. We shall use 3.34 to show that they are Lie subgroups. Their Lie algebras will be

(a') Skew-hermitian matrices

 $$ \mathbf{u}(n)=\{A\in\mathfrak{g l}(n,\mathbb{C})\colon\bar{A}+\mathcal{A}^{t}=0\}. $$ 

(b') Matrices of trace 0

 $$ \mathtt{s l}(n,\mathbb{C})=\{A\in\mathsf{g l}(n,\mathbb{C})\colon\mathrm{t r a c e}A=0\}. $$ 

(c') Skew-symmetric matrices

 $$ \mathfrak{d}(n,\mathbb{C})=\{A\in\mathfrak{g l}(n,\mathbb{C})\colon A+A^{t}=0\}. $$ 

Each of these examples is a subalgebra of $\mathrm{gl}(n,\mathbb{C})$. To apply 3.34, let $U$ be a neighborhood of $0$ in $\mathrm{gl}(n,\mathbb{C})$, diffeomorphic under the exponential map with a neighborhood $V$ of the identity in $Gl(n,\mathbb{C})$. We can assume, in addition, that if $A\in U$, then $\widetilde{A}, A^t$, and $-A$ belong to $U$, and $|\mathrm{trace}A|<2\pi$. For let $W$ be a neighborhood of $0$ in $\mathrm{gl}(n,\mathbb{C})$ that is small enough for the exponential map to be a diffeomorphism and also small enough for the trace condition to be satisfied, and then let $U=W\cap\overline{W}\cap W^t\cap(-W)$. We shall also assume that $\exp(U\cap\mathrm{gl}(n,\mathbb{R}))=Gl(n,\mathbb{R})\cap V$.

If $A \in U \cap u(n)$, then $(\overline{e^A})^t = e^{\overline{A}^t} = e^{-\overline{A}};$ hence $(\overline{e^A})^t e^A = e^{-\overline{A}} e^A = e^B = I$, which implies that $e^A \in U(n) \cap V$. Conversely, suppose that $A \in U$ and that $e^A \in U(n) \cap V$. Then $e^{-A} = (e^A)^{-1} = (\overline{e^A})^t = e^{\overline{A}^t}$, which implies that $-A = \overline{A}^t$ since $-A$ and $\overline{A}^t$ also belong to $U$ and since the exponential map is 1:1 on $U$. Thus $A \in U \cap u(n)$. It follows from 3.34 that $U(n)$ is a closed Lie subgroup of $Gl(n, \mathbb{C})$ with Lie algebra $u(n)$. A similar argument shows that $O(n, \mathbb{C})$ is a closed Lie subgroup of $Gl(n, \mathbb{C})$ with Lie algebra $o(n, \mathbb{C})$.

If $A \in \mathrm{sl}(n,\mathbb{C})$, then by 3.35(8), $\det e^A = 1$; hence $e^A \in \mathrm{Sl}(n,\mathbb{C})$. Conversely, if $\det e^A = 1$, then according to 3.35(8), $\mathrm{trace} A = (2\pi i)j$ for some integer $j$. If in addition $A \in U$, then $\mathrm{trace} A = 0$. Thus 3.34 implies that $\mathrm{Sl}(n,\mathbb{C})$ is a closed Lie subgroup of $\mathrm{Gl}(n,\mathbb{C})$ with Lie algebra $\mathrm{sl}(n,\mathbb{C})$.

It follows immediately from 3.34 and from considerations as given above that the special unitary group $SU(n)$, which is by definition $U(n)\cap S(n,\mathbb{C})$, is a closed Lie subgroup of $G(n,\mathbb{C})$ with Lie algebra $\mathfrak{s}(n)$ the subalgebra of $\mathfrak{g}(n,\mathbb{C})$ consisting of skew-hermitian matrices of trace $0$; the real special linear group $S(n,\mathbb{R})$, which is by definition $S(n,\mathbb{C})\cap G(n,\mathbb{R})$, is a closed Lie subgroup of $G(n,\mathbb{R})$ with Lie algebra $\mathfrak{s}(n,\mathbb{R})$ the real matrices of trace $0$; the orthogonal group $O(n)$, which is by definition $\mathcal{G}(n)\cap G(n,\mathbb{R})$, is a closed Lie subgroup of $G(n,\mathbb{R})$ with Lie algebra $o(n)$ the real skew-symmetric matrices; and the special orthogonal group $SO(n)$, which is by definition $O(n)\cap S(n,\mathbb{R})$, is a closed Lie subgroup of $G(n,\mathbb{R})$ also with Lie algebra $o(n)$ the real skew-symmetric matrices.

Each of these examples is a closed subgroup of either $GI(n,\mathbb{R})$ or $GI(n,\mathbb{C})$, and it follows from either 3.34 or 3.21 that in each case the Lie topology is the relative topology.

The unitary group is compact since not only is it closed, but also it is bounded in $GI(n,\mathbb{C})$, for $A^t\bar{A}=I$ implies that $\sum_j|A_{ij}|^a=1$ for each $i$, which implies that $|A_{ij}|^a\leq1$. It follows that $SU(n)$, $O(n)$, and $SO(n)$ are also compact.

The dimensions of these Lie groups are easily computed from their Lie algebras. $U(n)$ has dimension $n^2$; $Sl(n,\mathbb{C})$ has dimension $2n^2 - 2$; $O(n,\mathbb{C})$ has dimension $n(n - 1)$; $SU(n)$ has dimension $n^2 - 1$; $Sl(n,\mathbb{R})$ has dimension $n^2 - 1$; $O(n)$ and $SO(n)$ both have dimension $n(n - 1)/2$.

##### CONTINUOUS HOMOMORPHISMS

3.38 Theorem Let $\varphi: \mathbb{R} \to G$ be a continuous homomorphism of the real line $\mathbb{R}$ into the Lie group $G$. Then $\varphi$ is $C^\infty$.

PROOF It suffices to prove that $\varphi$ is $C^{\infty}$ on a neighborhood of $0$, for then it follows from composition with suitable left translations that $\varphi$ is $C^{\infty}$ everywhere. Let $V$ be a neighborhood of $e\in G$ diffeomorphic with a neighborhood $U$ of $0\in g$ under the exponential map. We can assume that $U$ is starlike, that is, $tX\in U$ for $0\leq t\leq 1$ whenever $X\in U$, and we let

 $$ U^{\prime}=\{X/2\colon X\in U\}. $$ 

Choose $t_0 > 0$ small enough so that $\varphi(t) \in \exp(U')$ for $|t| \leq t_0$. Let $n$ be a positive integer. Then there are uniquely determined elements $X$ and $Y$ of $U'$ such that $\exp X = \varphi(t_0/n)$ and $\exp Y = \varphi(t_0)$. We claim that $nX = Y$. Since

 $$ \operatorname{e x p}(n X)=\varphi(t_{0})=\operatorname{e x p}(Y), $$ 

and since  $ \exp $ is injective on  $ U' $, we need only show that  $ nX \in U' $. Now,  $ X \in U' $, so let  $ 1 \leq j < n $, and assume that  $ jX \in U' $. We will prove that  $ (j+1)X \in U' $. Now,  $ (j+1)X \in U $, and  $ \exp((j+1)X) = \varphi((j+1)t_0/n) $ which by assumption belongs to  $ \exp(U') $. Since  $ \exp $ is injective on  $ U $, it follows that  $ (j+1)X \in U' $. Hence  $ nX \in U' $ and  $ nX = Y $, as claimed. Now, let  $ n_1 $ be an integer with  $ 0 < |m| \leq n $. If  $ m $ is positive, then  $ \varphi(m t_0/n) = \varphi(t_0/n)^m = \exp(Y/n)^m = \exp(m Y/n) $. If  $ m $ is negative, then also  $ \varphi(m t_0/n) = \varphi((-m)t_0/n)^{-1} = \exp((-m)Y/n)^{-1} = \exp(m Y/n) $. It follows by continuity that  $ \varphi(t) = \exp(t/Y/t_0) $ for  $ |t| \leq t_0 $. Thus  $ \varphi $ is  $ C^\infty $.

3.39 Theorem Let $\varphi: H \to G$ be a continuous homomorphism of Lie groups. Then $\varphi$ is $C^\infty$.

PROOF Let $H$ be of dimension $d$, and let $X_{1}, \ldots, X_{d}$ be a basis of $b$. The map $\alpha: \mathbb{R}^{d} \to H$ defined by

(1)

 $$ \alpha(t_{1},\ldots,t_{d})=(\exp t_{1}X_{1})\cdots(\exp t_{d}X_{d}) $$ 

is $C^{\infty}$, and is non-singular at $0\in\mathbb{R}^{d}$ by 3.31(d); so there is a neighborhood $V$ of $0\in\mathbb{R}^{d}$ diffeomorphic under $\alpha$ with a neighborhood $U$ of $e$ in $H$. Now, $t\mapsto\varphi(\exp tX_{t})$ is a continuous homomorphism of $\mathbb{R}$ into $G$, and so is $C^{\infty}$ by 3.38. Thus $\varphi\circ\alpha$ is $C^{\infty}$, and therefore $\varphi\mid U$, which can be expressed as $(\varphi\circ\alpha)\circ\alpha^{-1}\mid U$, is $C^{\infty}$. Since $\varphi\mid\sigma U=\mid\varphi(\sigma)\circ\varphi\circ\sigma\mid\sigma U$, $\varphi$ is $C^{\infty}$ on all of $H$.

3.40 Definition A topological group $G$ is an abstract group $G$ which has a topology such that the map $(\sigma,\tau) \mapsto \sigma\tau^{-1}$ of $G \times G \to G$ is continuous.

3.41 Corollary to Theorem 3.39 A second countable locally Euclidean topological group can have at most one differentiable structure making it into a Lie group.

PROOF The identity map would give a diffeomorphism of any two such differentiable structures.

One of the outstanding problems in the theory of Lie groups was that of deciding whether every connected locally Euclidean topological group has a differentiable structure which makes it into a Lie group. The problem was posed by Hilbert in his famous address to the International Congress of Mathematics in 1900, and was solved with an affirmative answer by Gleason together with Montgomery and Zippen in 1952; see [20].

We have dealt exclusively with the $C^{\infty}$ structure on Lie groups. It can be shown [23] that the $C^{\infty}$ structure on a Lie group contains an analytic structure, that is, a collection of coordinate systems which overlap analytically (the compositions $\varphi_{\alpha}\circ\varphi_{\beta}^{-1}$ of coordinate maps being locally represented by convergent power series). In this context, the analog of 3.39 would state that every continuous homomorphism of Lie groups is analytic, from which it follows that the $C^{\infty}$ structure on a Lie group contains a unique analytic structure.

##### CLOSED SUBGROUPS

3.42 Theorem Let G be a Lie group, and let A be a closed abstract subgroup of G. Then A has a unique manifold structure which makes A into a Lie subgroup of G.

According to 3.21, the topology in this manifold structure on A must be the relative topology.

PROOF Uniqueness has been proved in 3.20. Let

 $$ a=\{X\in\mathfrak{g}\colon\operatorname{e x p}{t X\in A}\mathrm{~f o r~a l l~}t\in\mathbb{R}\}. $$ 

The idea of the proof is to show that $a$ is a subspace of $g$, and to apply 3.34. It is clear from the definition (1) that if $X \in a$, then also $tX \in a$ for any $t \in \mathbb{R}$. Now, let $X, Y \in a$. Suppose that

 $$ \operatorname*{l i m}_{n\to\infty}\Big(\mathtt{e x p}\frac{t}{n}X\mathtt{e x p}\frac{t}{n}Y\Big)^{n}=\mathtt{e x p}\big(t(X+Y)\big). $$ 

Since $A$ is closed, the left-hand side of (2) belongs to $A$. Thus (2) implies that $(X + Y) \in a$. Assuming (2) for the moment, we have proved that $a$ is a subspace of $g$ and shall use this to complete the proof of the theorem. We shall return to the proof of (2) in a separate lemma.

The theorem will follow from 3.34 once we have shown that there exists a neighborhood U of 0 in g, diffeomorphic under the exponential map with a neighborhood V of e in G such that

 $$ \operatorname{e x p}(U\cap a)=V\cap A. $$ 

Suppose, on the contrary, that no such $U$ exists. Then there is a neighborhood $W$ of 0 in $a$ and a sequence $\{\sigma_k\} \subset A$ such that $\sigma_k \to e$ in $G$ and

 $$ \sigma_{k}\notin\operatorname{e x p}(W). $$ 

Let $b$ be any complementary subspace to $a$ in $g$. It follows from 3.31(d) that the map $\alpha: a \times b \to G$ defined by $\alpha(X, Y) = \exp X \exp Y$ is $C^\infty$ and non-singular at $(0,0)$. Thus there are neighborhoods $W_a \subset W$ of $0$ in $a$ and $W_b$ of $0$ in $b$ such that $\alpha \big| W_a \times W_b$ is a diffeomorphism of $W_a \times W_b$ with a neighborhood $\tilde{V}$ of $e$ in $G$. If we can choose $W_b$ small enough that

 $$ A\cap\operatorname{e x p}(W_{\flat}-\{0\})=\varnothing, $$ 

then we can reach a contradiction as follows. For $k$ large enough, $\sigma_k \in \tilde{V}$, and thus $\sigma_k = \exp X_k \exp Y_k$ for $X_k \in W_a$ and $Y_k \in W_b$, where $Y_k \neq 0$ by (4). But $\sigma_k \in A$, as also $\exp X_k \in A$; so $\exp Y_k \in A$, contradicting (5).

Finally, we show that $W_b$ can be chosen satisfying (5). Again we argue by contradiction. Suppose that there is a sequence $\{Y_i\} \subset W_b$ such that $Y_i \neq 0$, $Y_i \to 0$, and $\exp Y_i \in A$. Then there is a subsequence $\{Y_j\}$ and a sequence $\{t_j\}$ of positive real numbers with $t_j \to 0$ such that the sequence $\{Y_j/t_j\}$ converges to some $Y \neq 0$ in $W_b$ (choose a norm on the vector space $W_b$, and let $t_i$ be the norm of $Y_i$). For $t > 0$, let $n_j(t)$ be the largest integer less than or equal to $(t/t_j)$. Then

 $$ \begin{array}{r}{\frac{t}{t_{j}}-1<n_{j}(t)\leq\frac{t}{t_{j}},}\end{array} $$ 

so  $ \lim_{t \to \infty} t_j n_j(t) = t $. Thus

 $$ \mathbf{e x p}\;t Y=\mathbf{e x p}\biggl(\operatorname*{l i m}_{j\to\infty}n_{j}(t)Y_{j}\biggr)=\operatorname*{l i m}_{j\to\infty}(\mathbf{e x p}\;Y_{j})^{n_{j}(t)}, $$ 

which belongs to $A$. Since $\exp(-tY) = (\exp{tY})^{-1}$, then $\exp{tY} \in A$ for all real numbers $t$, which implies that $Y \in a$. This contradicts the fact that $Y$ is a non-zero element of $W_b$.

To complete the proof we need the following lemma, which clearly implies (2).

## 112 Lie Groups

Lemma Let G be a Lie group with Lie algebra g. If $X, Y \in \mathfrak{g}$, then for $t$ sufficiently small,

 $$ \operatorname{e x p}t X\operatorname{e x p}t Y=\operatorname{e x p}\{t(X+Y)+O(t^{s})\}, $$ 

where $O(t^{8})$ denotes a g-valued $C^{\infty}$ function of $t$ such that $(1/t^{8})O(t^{8})$ is bounded at $t=0$.

PROOF For $t$ small enough, there is a $C^{\infty}$ curve $Z(t)$ in $g$ such that

 $$ \operatorname{e x p}t X\operatorname{e x p}t Y=\operatorname{e x p}Z(t). $$ 

Since the tangent vector to the curve

 $$ t\mapsto\exp t X\exp t Y $$ 

at $t=0$ is $X(e)+Y(e)$ (see Exercise 11), it follows that the tangent vector to $Z(t)$ at $t=0$ is $X+Y$, so the Taylor expansion with integral remainder of $Z(t)$ about $t=0$ has the form

 $$ Z(t)=t(X+Y)+O(t^{s}), $$ 

where $O(t^{2})$ is a $C^{\infty}$ g-valued function of $t$ such that $(1/t^{2})O(t^{2})$ is bounded at $t=0$. From (7) and (8) we obtain (6).

3.43 Theorem Let $\psi: G \to K$ be a homomorphism of Lie groups. If $A = \ker \psi$ and $a = \ker d\psi$, then $A$ is a closed Lie subgroup of $G$ with Lie algebra a.

PROOF $A$ is a closed abstract subgroup of $G$, hence, by 3.42, is a Lie subgroup of $G$. If $X \in g$, then according to 3.33 (with $H = A$ and $\varphi$ the inclusion map), $X$ belongs to the Lie algebra of $A$ if and only if $\exp t X \in A$ for all $t \in \mathbb{R}$, and this occurs if and only if $\psi(\exp t X) = e$ for all $t \in \mathbb{R}$. By 3.32, this latter condition is equivalent to having $\exp t \, d\psi(X) = e$ for all $t \in \mathbb{R}$, and this occurs if and only if $d\psi(X) = 0$ or $X \in a$.

##### THE ADJOINT REPRESENTATION

3.44 Definitions Let $M$ be a manifold, and let $G$ be a Lie group. $A$ $C^{\infty}$ map $\mu: G \times M \to M$ such that

 $$ \mu(\sigma\tau,m)=\mu\big(\sigma,\mu(\tau,m)\big),\qquad\mu(e,m)=m $$ 

for all $\sigma, \tau \in G$ and $m \in M$ is called an action of $G$ on $M$ on the left. If $\mu: G \times M \to M$ is an action of $G$ on $M$ on the left, then for a fixed $\sigma \in G$ the map $m \mapsto \mu(\sigma, m)$ is a diffeomorphism of $M$ which we shall denote by $\mu_{\sigma}$. Similarly, a $C^{\infty}$ map $\mu: M \times G \to M$ such that

 $$ \mu(m,\sigma\tau)=\mu\big(\mu(m,\sigma),\tau\big),\qquad\mu(m,e)=m $$ 

for all $\sigma, \tau \in G$ and $m \in M$ is called an action of $G$ on $M$ on the right.

3.45 Theorem Let $\mu: G \times M \to M$ be an action of $G$ on $M$ on the left. Assume that $m_0 \in M$ is a fixed point, that is, $\mu_\sigma(m_0) = m_0$ for each $\sigma \in G$. Then the map

 $$ \psi\colon G\to\mathrm{A u t}(M_{m_{0}}) $$ 

defined by

 $$ \psi(\sigma)=d\mu_{o}\mid M_{m_{o}} $$ 

is a representation of G.

PROOF  $ \psi $ is a homomorphism for

 $$ \psi(\sigma\tau)=d\mu_{\sigma\tau}\left|M_{m_{0}}=d(\mu_{\sigma}\circ\mu_{\tau})\right|M_{m_{0}}=\psi(\sigma)\circ\psi(\tau). $$ 

It remains only to prove that $\psi$ is $C^{\infty}$. For this, it suffices to prove that $\psi$ composed with an arbitrary coordinate function on $\mathrm{Aut}(M_{m_0})$ is $C^{\infty}$. Now, one gets a coordinate system on $\mathrm{Aut}(M_{m_0})$ by choosing a basis for $M_{m_0}$ and then by using this basis to identify $\mathrm{Aut}(M_{m_0})$ with non-singular matrices. One gets the matrix associated with an element of $\mathrm{Aut}(M_{m_0})$ by applying this element to the basis of $M_{m_0}$ and then applying the dual basis. So it suffices to prove that if $v_0 \in M_{m_0}$ and if $\alpha \in M_{m_0}^*$, then

 $$ \sigma\mapsto\alpha\left(d\mu_{\sigma}(v_{0})\right) $$ 

is a $C^{\infty}$ function on $G$. For (3), it suffices to prove that

 $$ \sigma\mapsto d\mu_{\sigma}(v_{0}) $$ 

is a $C^{\infty}$ map of $G$ into $M_{m_{0}}$, or equivalently that (4) is a $C^{\infty}$ map of $G$ into $T(M)$. But (4) is exactly the composition of $C^{\infty}$ maps

 $$ G\to T(G)\times T(M)\to T(G\times M)\to T(M) $$ 

in which the first map sends $\sigma \mapsto \big((\sigma,0),(m_0,v_0)\big)$, the second map is the canonical diffeomorphism of $T(G) \times T(M)$ with $T(G \times M)$, and the third map is $d\mu$. Thus $\psi$ is $C^\infty$.

3.46 The Adjoint Representation A Lie group G acts on itself on the left by inner automorphisms:

 $$ a\colon G\times G\to G,\qquad a(\sigma,\tau)=\sigma\tau\sigma^{-1}=a_{\sigma}(\tau). $$ 

The identity is a fixed point of this action. Hence, by 3.45, the map

 $$ \sigma\mapsto d a_{\sigma}\mid G_{e}\cong g $$ 

is a representation of $G$ into $\operatorname{Aut}(g)$. This is called the adjoint representation and is denoted by

 $$ \mathsf{A d}\colon G\to\mathsf{A u t}(\mathfrak{g}). $$ 

We let the differential of the adjoint representation be denoted by ad.

 $$ d(\mathbf{A d})={\cdot}\mathbf{a d}, $$ 

and we denote $\mathrm{Ad}(\sigma)$ by $\mathrm{Ad}_{\sigma}$ and $\mathrm{ad}(X)$ by $\mathrm{ad}_{X}$. Thus by 3.32 we have a commutative diagram

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//e006bf97-c486-454f-b40d-7a66ef2d28b8/markdown_1/imgs/img_in_image_box_329_219_602_347.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2F138d535ac3aab9115d34c44305ad9635921517883bdc4555f65bc4b94b31989a" alt="Image" width="27%" /></div>


Also applying 3.32 to the automorphism $a_{\sigma}$ of $G$, we obtain the commutative diagram

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//e006bf97-c486-454f-b40d-7a66ef2d28b8/markdown_1/imgs/img_in_image_box_340_404_587_530.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2Fb961bab64d8cfc67287c764901315bb5444af0b9fe2aaa20bb6dfdec8f990060" alt="Image" width="25%" /></div>


In other words,

 $$ \operatorname{e x p}t\operatorname{A d}_{\sigma}(X)=\sigma(\operatorname{e x p}t X)\sigma^{-1}. $$ 

In the special case in which $G = \mathrm{Aut}(V)$, the above diagrams become

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//e006bf97-c486-454f-b40d-7a66ef2d28b8/markdown_1/imgs/img_in_image_box_297_635_642_767.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2Ffa5860e4fca410b7d16d653f4ce67331744850752006c43531425be5ad7aced7" alt="Image" width="35%" /></div>


<div style="text-align: center;"><div style="text-align: center;">(8)</div> </div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//e006bf97-c486-454f-b40d-7a66ef2d28b8/markdown_1/imgs/img_in_image_box_299_797_601_924.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2Fc66a14850408cfdabc145de8b8bf7d511a0df3d3bdd98e744d6f1a08c07028b2" alt="Image" width="30%" /></div>


where  $ B \in \text{Aut}(V) $. If in addition  $ C \in \text{End}(V) $, then

 $$ \mathsf{A d}_{B}(C)=B\circ C\circ B^{-1}. $$ 

For from 3.36(2), using 3.35(15) and 3.35(6), we obtain

 $$ \begin{align*}\mathrm{Ad}_{B}(C)&=\frac{d}{dt}\bigg|_{t=0}\big(a_{B}(\exp t C)\big)=\frac{d}{dt}\bigg|_{t=0}(B\circ e^{tC}\circ B^{-1})\\&=\frac{d}{dt}\bigg|_{t=0}e^{t B\circ C\circ B^{-1}}=B\circ C\circ B^{-1}.\end{align*} $$ 

Similarly, in the case in which $G = Gl(n, \mathbb{R})(\text{or } Gl(n, \mathbb{C}))$ and $B \in Gl(n, \mathbb{R})$ and $C \in gl(n, \mathbb{R})$, then

 $$ \mathrm{A d}_{B}(C)=B C B^{-1}. $$ 

3.47 Proposition Let G be a Lie group with Lie algebra g, and let X, Y ∈ g. Then

(1)

 $$ \mathbf{a d}_{X}Y=[X,Y]. $$ 

PROOF By 3.36(2),

(2)

 $$ \begin{align*}\mathrm{ad}_{X}Y&=\left(\frac{d}{dt}\bigg|_{t=0}\mathrm{Ad}(\exp tX)\right)Y\\&=\frac{d}{dt}\bigg|_{t=0}\mathrm{Ad}_{\exp tX}(Y)=\frac{d}{dt}\bigg|_{t=0}d(a_{\exp tX})(Y).\end{align*} $$ 

Thus if $X_{t}$ denotes, as usual, the 1-parameter group of diffeomorphisms associated with $X$, then

 $$ \begin{aligned}{\operatorname{a d}_{\underline{{X}}}Y(e)}&{{}=\frac{d}{d t}\bigg|_{t=0}d(r_{\operatorname{e x p}(-t\underline{{X}})})\big(d(l_{\operatorname{e x p}t\underline{{X}}})(Y(e))\big)}\\ {}&{{}=\frac{d}{d t}\bigg|_{t=0}d(r_{\operatorname{e x p}(-t\underline{{X}})})(Y\big|_{\operatorname{e x p}t\underline{{X}}})}\\ {}&{{}=\frac{d}{d t}\bigg|_{t=0}d(X_{-t})(Y_{X_{t}(e)})}\\ {}&{{}=(L_{\underline{{X}}}Y)(e)=[X,Y](e).}\\ \end{aligned} $$ 

The last equality follows from 2.25(b). Since $\operatorname{ad}_{X}Y$ and $[X,Y]$ are both left invariant, (1) is an immediate consequence of (3).

3.48 Theorem Let $A \subseteq G$ be a connected Lie subgroup of a connected Lie group $G$. Then $A$ is a normal subgroup of $G$ if and only if the Lie algebra $a$ of $A$ is an ideal in $g$.

PROOF Assume that a is an ideal in g. Let  $ Y \in a $, let  $ X \in g $, and let  $ \sigma = \exp X $. Then

(1)

 $$ \begin{aligned}{{})\quad\sigma(\operatorname{e x p}Y)\sigma^{-1}}&{{}=\operatorname{e x p}\operatorname{A d}_{\sigma}(Y)}\\ {}&{{}=\operatorname{e x p}\bigl((\operatorname{e x p}\operatorname{a d}_{X})(Y)\bigr)}\\ \end{aligned} $$ 

 $$ \exp\left(Y+[X,Y]+\frac{(\mathrm{ad})^{2}X}{2!}(Y)+\cdots\right). $$ 

Under the assumption that a is an ideal in g, the series in the last term in (1) converges to an element of a, so that

 $$ \sigma(\exp Y)\sigma^{-1}\in A. $$ 

Now, by 3.18 and 3.31(d), $A$ is generated by elements of the form $\exp Y$, and $G$ is generated by elements of the form $\exp X$. This, together with (2), implies that $A$ is a normal subgroup of $G$.

Conversely, assume that $A$ is normal in $G$. Let $s$ and $t$ be real numbers, let $Y \in \alpha$ and $X \in g$, and let $\sigma = \exp t X$. Then, according to (1),

 $$ \sigma(\operatorname{e x p}s Y)\sigma^{-1}=\operatorname{e x p}\operatorname{A d}_{\sigma}(s Y)=\operatorname{e x p}s\big\{(\operatorname{e x p}\operatorname{a d}_{t X})(Y)\big\}. $$ 

Since $A$ is normal, $\sigma(\exp sY)\sigma^{-1}\in A$; so it follows from (3) and 3.33 that $(\exp ad_{tX})(Y)\in a$ for all $t\in\mathbb{R}$. Now

(4)

 $$ \begin{aligned}{(\operatorname{e x p}\operatorname{a d}_{t X})(Y)}&{{}=\big(\operatorname{e x p}t(\operatorname{a d}_{X})\big)(Y)}\\ {}&{{}=Y+t[X,Y]+\frac{t^{8}}{2!}\left[X,[X,Y]\right]+\cdots,}\\ \end{aligned} $$ 

which is a smooth curve in a whose tangent vector at $t = 0$ is $[X, Y]$. Thus $[X, Y] \in \alpha$, and $\alpha$ is an ideal in $g$.

### 3.49 Definitions

(a) Center of g = \{X ∈ g: [X, Y] = 0 for all Y ∈ g\}.

(b) Center of  $ G = \{\sigma \in G: \sigma \tau = \tau \sigma \text{ for all } \tau \in G\} $.

3.50 Theorem Let G be a connected Lie group. Then the center of G is the kernel of the adjoint representation.

PROOF Let  $ \sigma $ belong to the center of G, and let  $ X \in \mathfrak{g} $. Then

 $$ \operatorname{e x p}t X=\sigma(\operatorname{e x p}t X)\sigma^{-1}=\operatorname{e x p}t\operatorname{A d}_{\sigma}(X) $$ 

for all $t\in\mathbb{R}$. Thus $X=\mathrm{Ad}_{e}(X)$; so $\sigma\in\ker(\mathrm{Ad})$. Conversely, let $\sigma\in\ker(\mathrm{Ad})$. Then (1) again holds, so $\sigma$ commutes with every element in a neighborhood of $e$ in $G$. Since $G$ is connected, $\sigma$ commutes with every element of $G$. Thus $\sigma$ lies in the center of $G$.

Corollary (a) Let G be a connected Lie group. Then the center of G is a closed Lie subgroup of G with Lie algebra the center of g.

PROOF This corollary is an immediate consequence of 3.50 and 3.43.

Corollary (b) A connected Lie group G is abelian if and only if its Lie algebra g is abelian.

3.51 Proposition Let $X$, $Y$ belong to the Lie algebra $\mathfrak{g}$ of a Lie group $G$. Then

 $$ [X,Y]=0\;\Rightarrow\;\operatorname{e x p}(X+Y)=\operatorname{e x p}X\operatorname{e x p}Y. $$ 

PROOF The subspace a of g spanned by X and Y is a subalgebra of g, and the corresponding connected Lie subgroup A of G is abelian. Let

 $$ \alpha(t)=\exp t X\exp t Y. $$ 

Then $\alpha$ is a $C^{\infty}$ map of $\mathbb{R}$ into $G$ and is a homomorphism since $A$ is abelian. The tangent vector to $\alpha$ at $0$ is $X(e) + Y(e)$ (see Exercise 11), so that

 $$ \exp{t}X\exp{t}Y=\exp{t}(X+Y) $$ 

for all t.

3.52 Remark Recall that in 3.27 we stated Ado's theorem which asserts that any Lie algebra g has a faithful representation in some $\mathrm{gl}(n,\mathbb{R})$ from which it follows that there is a Lie group with Lie algebra g. If g has trivial center, we can get such a faithful representation from the adjoint representation. Simply define $ad:g \to \mathrm{Erd}(g)$ by $ad_x(Y) = [X, Y]$, and check that this is a Lie algebra homomorphism. If g has trivial center, ad is one-to-one; so we have a faithful representation of g in $\mathrm{End}(g)$. This together with 3.19 gives a simple proof that every Lie algebra with trivial center is the Lie algebra of some Lie group.

## AUTOMORPHISMS AND DERIVATIONS OF BILINEAR OPERATIONS AND FORMS

3.53 Definitions Let $V$ be a finite dimensional real or complex vector space. A bilinear operation on $V$ is a linear map $\psi: V\otimes V \to V$ where the tensor product is taken over the real (resp. complex) numbers when $V$ is a real (resp. complex) vector space. We shall use the notation

 $$ \psi(v\otimes w)=\{v,w\}. $$ 

(a) We let

 $$ A_{v}(V)=\{\alpha\in\mathbf{A u t}(V)\colon\alpha\{v,w\}=\{\alpha(v),\alpha(w)\}\mathrm{f o r~a l l}v,w\in V\}. $$ 

The elements of $A_{w}(V)$ are the automorphisms of $V$ which preserve the bilinear operation $\psi$.

(b) We let

 $$ \mathfrak{d}_{w}=\{I\in\mathbb{E n d}(V)\colon I\{v,w\}=\{I(v),w\}+\{v,l(w)\}\mathrm{~f o r~a l l~}v,w\in V\}. $$ 

Elements of  $ b_{\psi} $ are called derivations of the bilinear operation  $ \psi $.

3.54 Theorem $A_{v}(V)$ is a closed Lie subgroup of $\mathrm{Aut}(V)$ with Lie algebra $\partial_{v}$.

PROOF It is easy to check that $b_{v}$ is a subalgebra of $\mathrm{End}(V)$ and that $A_{v}(V)$ is a closed abstract subgroup of $\mathrm{Aut}(V)$. According to Theorem 3.42, $A_{v}(V)$ is a closed Lie subgroup of $\mathrm{Aut}(V)$. Let $a$ be the Lie algebra of $A_{v}(V)$. We need only show that $a = b_{v}$.

If  $ l \in a $, then  $ \exp t l \in A_{\psi}(V) $, so that

 $$ (\mathtt{e x p}t l)\{v,w\}=\{(\mathtt{e x p}t l)(v),(\mathtt{e x p}t l)(w)\}. $$ 

Both sides of (1) are smooth curves in V. Taking their derivatives at t = 0, we obtain

 $$ l\{v,w\}=\{l(v),w\}+\{v,l(w)\}, $$ 

which proves that  $ l \in \mathfrak{b}_{\psi} $. (Observe that a curve  $ \varphi(t) \otimes \psi(t) $ in  $ V \otimes V $ has derivative (or tangent vector) at  $ t = 0 $ equal to  $ \dot{\varphi}(0) \otimes \psi(0) + \varphi(0) \otimes \psi(0) $.)

Conversely, suppose that  $ l \in \mathfrak{b}_{w} $. To prove that  $ l \in \mathfrak{a} $, we need only prove that  $ \exp t l \in A_{w}(V) $ for all  $ t $. We let  $ l \otimes 1 $ denote the endomorphism of  $ V \otimes V $ defined by

 $$ (l\otimes1)(v\otimes w)=l(v)\otimes w. $$ 

The fact that  $  l \in \mathbf{b}_{v}  $ means that

 $$ l\{v,w\}=\{l(v),w\}+\{v,l(w)\} $$ 

for all v and w in V; and this can be expressed as

 $$ l\circ\varphi=\varphi\circ(l\otimes1+1\otimes l). $$ 

It follows from (4) that

 $$ l^{n}\circ\varphi=\varphi\circ(l\otimes1+1\otimes l)^{n}, $$ 

so that

 $$ e^{t l}\circ\psi=\psi\circ e^{t(l\otimes1+1\otimes l)}. $$ 

Now,  $ (l \otimes 1) \circ (1 \otimes l) = (1 \otimes l) \circ (l \otimes 1) $, so we can apply 3.35(9) to the right-hand term in (6). Then, by the fact that  $ e^{t(l \otimes 1)} = e^{t l} \otimes 1 $, equation (6) becomes

 $$ \begin{aligned}{e^{t l}\circ\psi}&{{}=\psi\circ e^{t(i\otimes1)}\circ e^{t(i\otimes l)}=\psi\circ(e^{t l}\otimes1)\circ(1\otimes e^{t l})}\\ {}&{{}=\psi\circ e^{t l}\otimes e^{t l}.}\\ \end{aligned} $$ 

Thus

 $$ (\mathtt{e x p}t l)\{v,w\}=\{(\mathtt{e x p}t l)(v),(\mathtt{e x p}t l)(w)\} $$ 

for all $v$ and $w$ in $V$, which implies that $\exp t l \in A_{\psi}(V)$ for all $t \in \mathbb{R}$. Thus $a = b_{\psi}$, and the theorem is proved.

3.55 Definitions Again we let $V$ be a finite dimensional vector space over a field $F$ where $F$ is either $\mathbb{R}$ or $\mathbb{C}$. A bilinear form $B$ on $V$ is a linear map $B: V \otimes V \to F$. We shall use the notation $B(v \otimes w) = (v, w)$.

(a) We let

 $$ A_{B}(V)=\big\{\alpha\in\operatorname{A u t}(V)\colon(v,w)=\big(\alpha(v),\alpha(w)\big)\mathrm{f o r~a l l~}v,w\in V\big\}. $$ 

The elements of $A_{B}(V)$ are the automorphisms of $V$ which preserve the bilinear form $B$.

(b) We let

 $$ \mathfrak{d}_{B}=\big\{I\in\mathbb{E}\mathrm{e n d}(V)\colon\big(l(v),w\big)+\big(v,l(w)\big)=0\mathrm{f o r~a l l~}v,w\in V\big\}. $$ 

Elements of  $ b_{B} $ are called derivations of the bilinear form B.

3.56 Theorem  $ A_{B}(V) $ is a closed Lie subgroup of  $ \mathrm{Aut}(V) $ with Lie algebra  $ \mathfrak{d}_{B} $.

The proof is similar to the proof of Theorem 3.54, and we leave it to the reader as an exercise.

### 3.57 Applications of 3.54 and 3.56

(a) Let $V$ be a real vector space with an inner product $B$. According to Theorem 3.56, the automorphisms of $V$ which preserve the inner product form a closed Lie subgroup $A_B(V) \subset \mathrm{Aut}(V)$ whose Lie algebra is the Lie subalgebra $\mathfrak{b}_B \subset \mathrm{End}(V)$ of derivations of the inner product $B$. Choose an orthonormal basis for $V$. Now consider the Lie group isomorphism of $\mathrm{Aut}(V)$ with $GI(n, \mathbb{R})$ and the associated Lie algebra isomorphism of $\mathrm{End}(V)$ with $\mathrm{gl}(n, \mathbb{R})$ determined by associating with each linear transformation on $V$ its matrix relative to this basis. It is easily seen that $A_B(V)$ is mapped onto the orthogonal group $O(n) \subset GI(n, \mathbb{R})$ and that $\mathfrak{b}_B$ is mapped onto the set $\mathfrak{o}(n)$ of skew-symmetric matrices in $\mathrm{gl}(n, \mathbb{R})$. This provides another proof of the fact that the orthogonal group $O(n)$ is a closed Lie subgroup of $GI(n, \mathbb{R})$ with Lie algebra $\mathfrak{o}(n)$.

(b) A Lie algebra g has a bilinear operation—the bracket [, ]. The automorphisms of g which preserve the bracket are precisely the Lie algebra isomorphismsof g. We shall denote them by  $ A(g) $. According to 3.54,  $ A(g) $ is a closed Lie subgroup of  $ \mathrm{Aut}(g) $ with Lie algebra the derivations of [, ] which we shall denote by b(g).

Suppose that G is a simply connected Lie group with Lie algebra g. Let  $ A(G) $ be the group of all Lie group automorphisms of G. The map

 $$ \psi\colon A(G)\to A(\mathfrak{g})\quad{\mathrm{d e f i n e d~b y}}\quad\psi(\alpha)=d\alpha $$ 

is a homomorphism and is 1:1 by 3.16 and onto by 3.27. Thus we can induce via $\psi$ a manifold structure on $A(G)$, making $A(G)$ into a Lie group with Lie algebra isomorphic with $\mathfrak{b}(g)$.

##### HOMOGENEOUS MANIFOLDS

3.58 Theorem Let $H$ be a closed subgroup of a Lie group $G$, and let $G|H$ be the set $\{\sigma H: \sigma \in G\}$ of left cosets modulo $H$. Let $\pi: G \to G|H$ denote the natural projection $\pi(\sigma) = \sigma H$. Then $G|H$ has a unique manifold structure such that

(a)  $ \pi $ is  $ C^{\infty} $.

(b) There exist local smooth sections of $G/H$ in $G$; that is, if $\sigma H \in G/H$, there is a neighborhood $W$ of $\sigma H$ and a $C^\infty$ map $\tau: W \to G$ such that $\pi \circ \tau = \mathrm{id}$.

PROOF Existence We topologize $G/H$ by requiring $U$ in $G/H$ to be open if and only if $\pi^{-1}(U)$ is an open set in $G$. With this topology, $\pi$ is an open map since if $W$ is open in $G$, then

 $$ \pi^{-1}\bigl(\pi(W)\bigr)=\bigcup_{h\in H}W h, $$ 

which implies that $\pi(W)$ is open in $G/H$. Moreover, $G/H$ is Hausdorff. To see this, first observe that the set $R \subset G \times G$ consisting of all pairs $(\sigma, \tau)$ for which there exists an $h \in H$ such that $\sigma = \tau h$ is a closed set since $R = \alpha^{-1}(H)$ where $\alpha$ is the continuous map $(\sigma, \tau) \mapsto \tau^{-1}\sigma$ of $G \times G$ into $G$. Now, if $\sigma H$ and $\tau H$ are distinct points of $G/H$, $(\sigma, \tau)$ does not belong to $R$, so there exist open neighborhoods $V$ of $\sigma$ and $W$ of $\tau$ in $G$ such that $(V \times W) \cap R = \varnothing$. Then $\pi(V)$ and $\pi(W)$ are disjoint open neighborhoods of $\sigma H$ and $\tau H$ respectively, which proves that $G/H$ is Hausdorff. A countable basis for the topology on $G$ projects under $\pi$ to a countable basis for the topology on $G/H$. Thus $G/H$ is second countable.

According to 3.42, the closed subgroup $H$ is a Lie subgroup of $G$. Suppose that $G$ is of dimension $d$ and that $H$ is of dimension $d-k$. To prove that $G/H$ is locally Euclidean and to obtain a cover of smoothly overlapping coordinate systems on $G/H$, we first prove that there exists a cubic centered coordinate system $(U,\varphi)$ about $e$ in $G$, with coordinate functions $x_{1},\ldots,x_{d}$, such that distinct slices of the form

 $$ x_{i}=\mathrm{c o n s t a n t}\qquad\mathrm{f o r~a l l~}i\in\{1,\ldots,k\} $$ 

lie on distinct left cosets of $H$. Let $\mathcal{D}$ be the distribution on $G$ determined by the Lie algebra of $H$. Then, by 1.60, there is a cubic centered coordinate system $(V,\varphi)$ about $e$ in $G$, with coordinate functions $x_{1},\ldots,x_{d}$, such that the integral manifolds of $\mathcal{D}$ in $V$ are slices of the form (1). Since $H$ is a closed subgroup of $G$, and therefore as a Lie subgroup has the relative topology, $V$ can be chosen small enough so that

 $$ \bullet \quad \quad V\cap H=\mathrm{t h e~s l i c e~}S_{0}\mathrm{~t h r o u g h~}e. $$ 

Choose neighborhoods U and $V_{1}$ of $e$, cubic relative to the coordinate system $(V,\varphi)$, such that

 $$ V_{1}V_{1}\subset V\qquad\mathrm{a n d}\qquad U^{-1}U\subset V_{1}. $$ 

Now suppose that $\sigma$ and $\tau$ are points of $U$ which lie in the same coset modulo $H$, so $\sigma \in \tau H$. Then

 $$ \tau^{-1}\sigma\in V_{1}\cap H=V_{1}\cap S_{0}. $$ 

So $\sigma \in \tau(V_1 \cap S_0)$. Now $\tau(V_1 \cap S_0)$ is an integral manifold of $\mathcal{D}$ which lies in $V$ by the choice of $V_1$ in (3), and $\tau(V_1 \cap S_0)$ is connected. Therefore $\tau(V_1 \cap S_0)$ lies in a single slice of $V$. So $\sigma$ and $\tau$ lie in the same slice. Conversely, it is easily seen that a single slice lies on a single coset. Thus $(U, \phi)$ is the desired coordinate system.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//2c4fbfc3-1037-4444-a2b3-97b299b84a1b/markdown_0/imgs/img_in_image_box_110_434_764_801.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2Fbcce0d330136c78d53ba00c2edf5068146c2d7ab82b2aae0cc3f16c3ce2c45db" alt="Image" width="68%" /></div>


Let $S$ be the slice of $\varphi(U)$ on which $x_{k+1},\ldots,x_{d}$ vanish. Let $\widetilde{\varphi}^{-1}$ be the map defined by setting

 $$ \tilde{\varphi}^{-1}=\pi\circ\varphi^{-1}\bigm|S\colon S\to\pi(U). $$ 

Then $\tilde{\varphi}^{-1}$ is one-to-one by the choice of the coordinate system $(U,\varphi)$, and is also continuous and an open map; hence it is a homeomorphism. Let $\tilde{\varphi}$ be the inverse,

 $$ \tilde{\varphi}\colon\pi(U)\to S\subset\mathbb{R}^{k}. $$ 

Then $(\pi(U),\tilde{\varphi})$ is a coordinate system about the identity coset in $G/H$. We obtain coordinate systems about other points of $G/H$ by left translations. Indeed, if $\sigma\in G$, we let $l_\sigma$ be the homeomorphism of $G/H$ induced by left translation $l_\sigma$ on $G$; that is,

 $$ \tilde{l}_{o}(\tau H)=\sigma\tau H. $$ 

Then for each $\sigma H \in G/H$ we define a map $\tilde{\varphi}_{\sigma H}$ by setting

 $$ \tilde{\varphi}_{\sigma H}=\tilde{\varphi}\circ\tilde{l}_{\sigma^{-1}}\big|\tilde{l}_{\sigma}\big(\pi(U)\big). $$ 

Then  $ (\tilde{l}_{e}(\pi(U)), \tilde{\varphi}_{eH}) $ is a coordinate system about  $ \sigma H $. Note that in this notation  $ \tilde{\varphi}_{H} $ is just the map  $ \tilde{\varphi} $. Now, we claim that one obtains a differentiable structure on  $ G/H $ by maximizing the collection of coordinate systems

 $$ \big\{\big(\tilde{l}_{\sigma}\big(\pi(U)\big),\tilde{\Phi}_{\sigma H}\big)\colon\sigma\in G\big\}. $$ 

One has only to check differentiability on overlaps. So let  $ (\tilde{l}_{\sigma_{1}}(\pi(U)), \tilde{\varphi}_{\sigma_{1}H}) $ and  $ (\tilde{l}_{\sigma_{2}}(\pi(U)), \tilde{\varphi}_{\sigma_{2}H}) $ be two such coordinate systems, and let

 $$ \begin{array}{r}{\widehat{V}=\tilde{\varphi}_{\sigma_{1}H}(\tilde{l}_{\sigma_{1}}(\pi(U))\cap\tilde{l}_{\sigma_{2}}(\pi(U))).}\end{array} $$ 

We must prove that $\tilde{\varphi}_{\sigma_1H} \circ \tilde{\varphi}_{\sigma_1H}^{-1} \mid V$ is $C^\infty$. Let $t \in V$. Then since $\tilde{l}_{\sigma_1^{-1}} \circ \tilde{l}_{\sigma_1} \circ \tilde{\varphi}^{-1}(t) \in \pi(U)$, there exists an element $g \in H$ such that $\sigma_2^{-1} \sigma_1 \varphi^{-1}(t) g \in U$. It follows that there exists a neighborhood $W$ of $t$ in $V$ such that $\sigma_2^{-1} \sigma_1 \varphi^{-1}(W) g \subset U$. It suffices to prove that $\tilde{\varphi}_{\sigma_1H} \circ \tilde{\varphi}_{\sigma_1H}^{-1} \mid W$ is $C^\infty$. But we can express $\tilde{\varphi}_{\sigma_1H} \circ \tilde{\varphi}_{\sigma_1H}^{-1} \mid W$ as the following composition of $C^\infty$ maps:

 $$ \tilde{\varphi}_{\sigma_{0}H}\circ\tilde{\varphi}_{\sigma_{1}H}^{-1}\mid W=\pi_{0}\circ\varphi\circ r_{g}\circ l_{\sigma_{1}^{-1}\sigma_{1}}\circ\varphi^{-1}\mid W, $$ 

where  $ \pi_0 $ is the canonical projection of  $ \varphi(U) $ onto S. Thus  $ \widetilde{\varphi}_{\sigma_1H} \circ \widetilde{\varphi}_{\sigma_1H}^{-1} \mid V $ is  $ C^\infty $.

With this differentiable structure on $G/H$, the projection $\pi: G \to G/H$ is $C^\infty$; indeed, $\pi$ restricted to an open set of the form $I_e(U)$ is nothing other than the composition $\tilde{\varphi}_{eH}^{-1} \circ \pi_0 \circ \varphi \circ I_{e^{-1}} \mid I_e(U)$. Thus result (a) holds; and as for (b), $I_e \circ \varphi^{-1} \circ \tilde{\varphi}_{eH}$ is a local smooth section of $G/H$ in $G$ on the neighborhood $I_e(\pi(U))$ of $\sigma H$.

Uniqueness Let  $ (G/H)_{1} $ denote G/H with another differentiable structure satisfying (a) and (b).

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//2c4fbfc3-1037-4444-a2b3-97b299b84a1b/markdown_1/imgs/img_in_image_box_319_852_565_987.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A14Z%2F-1%2F%2F58cf94eba2c7393914c1165a4eedef7e3df15aacaca5971046308c423641a5e5" alt="Image" width="25%" /></div>


Then the identity map and its inverse are both $C^{\infty}$ since locally they can be expressed as the composition of local smooth sections into $G$ followed by $\pi$. Thus id is a diffeomorphism, which proves uniqueness.

3.59 Definition Manifolds of the form $G/H$ where $G$ is a Lie group, $H$ is a closed subgroup of $G$, and the manifold structure is the unique one satisfying (a) and (b) of Theorem 3.58 are called homogeneous manifolds.

3.60 Remark Observe that $f$ is a $C^{\infty}$ function on $G/H$ if and only if $f\circ\pi$ is a $C^{\infty}$ function on $G$; for if $f$ is $C^{\infty}$, then certainly $f\circ\pi$ is $C^{\infty}$. Conversely if $f\circ\pi$ is $C^{\infty}$, then $f$, which can locally be represented as the composition of a smooth section of $G/H$ in $G$ with $f\circ\pi$, is also $C^{\infty}$.

### 3.61 Definitions Let

 $$ \eta\colon G\times M\to M $$ 

be an action of G on M on the left (cf. 3.44); and, as usual, let

 $$ \eta_{\sigma}(m)=\eta(\sigma,m). $$ 

The action is called effective if $e$ is the only element of $G$ for which $\eta_{e}$ is the identity map on $M$. The action is called transitive if whenever $m$ and $n$ belong to $M$ there exists a $\sigma$ in $G$ such that $\eta_{e}(m) = n$. Let $m_{0} \in M$, and let

 $$ H=\{\sigma\in G\colon\eta_{\sigma}(m_{0})=m_{0}\}. $$ 

H is a closed subgroup of G called the isotropy group at  $ m_{0} $. The action  $ \eta $ restricted to H gives an action of H on M on the left with a fixed point  $ m_{0} $, so by 3.45 we have a representation

 $$ \alpha\colon H\to\operatorname{A u t}(M_{m_{0}})\quad\mathrm{w h e r e}\quad\alpha(\sigma)=d\eta_{\sigma}\left\vert\right.M_{m_{0}}. $$ 

The group  $ \alpha(H) $ of linear transformations of  $ M_{m_{0}} $ is called the linear isotropy group at  $ m_{0} $.

3.62 Theorem Let $\eta: G \times M \to M$ be a transitive action of the Lie group $G$ on the manifold $M$ on the left. Let $m_0 \in M$, and let $H$ be the isotropy group at $m_0$. Define a mapping

 $$ \tilde{\beta}\colon G/H\to M\quad\mathrm{b y}\quad\tilde{\beta}(\sigma H)=\eta_{\sigma}(m_{0}). $$ 

Then  $ \beta $ is a diffeomorphism.

PROOF Observe first that $\tilde{\beta}$ is well-defined since $\eta_{\sigma h}(m_0) = \eta_\sigma(\eta_h(m_0)) = \eta_\sigma(m_0)$ for any $h \in H$. $\tilde{\beta}$ is surjective since $G$ acts transitively, and is injective since if $\tilde{\beta}(\sigma H) = \tilde{\beta}(\tau H)$, then $\eta_{\tau^{-1}\sigma}(m_0) = m_0$, which implies that $\tau^{-1}\sigma$ belongs to $H$, or in other words that $\sigma H = \tau H$. In view of Exercise 6 of Chapter 1, it suffices to prove that $\tilde{\beta}$ is $C^\infty$ and that $d\tilde{\beta}$ is non-singular at each point.

According to Remark 3.60, $\beta$ is $C^{\infty}$ if and only if $\beta\circ\pi$ is $C^{\infty}$ where $\pi$ is the natural projection of $G$ onto $G/H$. But

 $$ \beta\circ\pi=\eta\circ i_{m_{0}} $$ 

where  $ i_{m} $ is the  $ C^{\infty} $ map of G into  $ G \times M $ defined by

 $$ i_{m_{0}}(\sigma)=(\sigma,m_{0}). $$ 

Thus  $ \beta $ is  $ C^{\infty} $.

Now let $\beta=\tilde{\beta}\circ\pi$. Since the kernel of $d\pi\mid G_{\sigma}$ is $(\sigma H)_{\sigma}\subset G_{\sigma}$, in order to prove that $d\tilde{\beta}\mid(G/H)_{\sigma H}$ is non-singular it is sufficient to prove that the kernel of $d\beta\mid G_{\sigma}$ is also $(\sigma H)_{\sigma}$. Since for each $\sigma\in G$,

 $$ \beta=\eta_{e}\circ\dot{\beta}\circ\dot{I}_{e^{-1}}, $$ 

it suffices to prove that the kernel of $d\beta \big| G_\theta$ is $H_\theta$. Certainly $H_\theta \subset \ker(d\beta \big| G_\theta)$. So let $x \in \ker(d\beta \big| G_\theta)$. To show that $x \in H_\theta$, we need only prove that $\exp tX \in H$ for all $t \in \mathbb{R}$ where $X$ is the left invariant vector field on $G$ determined by $x$. For this, it is sufficient to prove that the tangent vector to the curve $t \mapsto \beta(\exp tX)$ in $M$ is identically zero, for then $\beta(\exp tX) \equiv m_\theta$, which implies that $\exp tX \in H$ for all $t$. The tangent vector to this curve at $t$ is

 $$ \begin{aligned}{d\beta(X_{\operatorname{e x p}t\mathbf{X}})}&{{}=d\big(\eta_{\operatorname{e x p}t\mathbf{X}}\circ\beta\circ I_{\operatorname{e x p}(-t\mathbf{X})}\big)\big(X_{\operatorname{e x p}t\mathbf{X}}\big)}\\ {}&{{}=d\eta_{\operatorname{e x p}t\mathbf{X}}\circ d\beta\big(X(e)\big)=d\eta_{\operatorname{e x p}t\mathbf{X}}\circ d\beta(x)=0.}\\ \end{aligned} $$ 

Thus $d\tilde{\beta}$ is everywhere non-singular, and the theorem is proved.

3.63 Remarks If $G$ is a Lie group and $H$ a closed subgroup of $G$, then there is a natural action $\tilde{I}$ of $G$ on the homogeneous manifold $G/H$ on the left, namely,

 $$ \tilde{l}\colon G\times G/H\to G/H,\qquad\tilde{l}(\sigma,\tau H)\stackrel{,}{=}\sigma\tau H. $$ 

It is easily checked that $\tilde{I}$ is $C^{\infty}$ and indeed gives an action of $G$ on $G/H$ on the left. Moreover, it is obvious that $\tilde{I}$ is a transitive action. Now, for each $\sigma$ in $G$, $\tilde{I}_{e}$ (notation as in 3.61(2)) is a diffeomorphism of $G/H$; and given any two points $\tau H$ and $\gamma H$ of $G/H$ there is a diffeomorphism $\tilde{I}_{\tau\gamma^{-1}}$ taking $\gamma H$ to $\tau H$. The reason that manifolds of the form $G/H$ are called homogeneous is that they possess this transitive group of diffeomorphisms. Conversely, Theorem 3.62 shows that if a manifold $M$ has a transitive group of diffeomorphisms in the sense of 3.61(1), then $M$ is diffeomorphic with a homogeneous manifold $G/H$.

From Theorem 3.62 we get another characterization of the manifold structure on $G/H$, namely, the set $G/H$ has a unique manifold structure such that the natural map (1) is $C^{\infty}$.

3.64 Theorem Let G be a Lie group and H a closed normal subgroup of G. Then the homogeneous manifold G/H with its natural group structure is a Lie group.

PROOF One has only to check that the map

 $$ (\sigma H,\tau H)\mapsto\sigma\tau^{-1}H $$ 

of $G/H \times G/H \to G/H$ is $C^{\infty}$. Let $\alpha_{e}: W_{e} \to G$ and $\alpha_{r}: W_{r} \to G$ be local sections of $G/H$ in $G$ on neighborhoods $W_{e}$ of $\sigma H$ and $W_{r}$ of $\tau H$

respectively. Then locally the map (1) can be expressed as the following composition of $C^{\infty}$ maps:

 $$ \pi\circ\varphi\circ(\alpha_{e}\times\alpha_{r}), $$ 

where  $ \varphi: G \times G \to G $ is the map  $ \varphi(\sigma, \tau) = \sigma\tau^{-1} $.

### 3.65 Examples of homogeneous manifolds

(a) Let $\{e_i: i = 1, \ldots, n\}$ be the canonical basis of $\mathbb{R}^n$ where $e_i$ is the $n$-tuple consisting of all zeros except for a 1 in the $i$th spot. Each matrix $\sigma \in G l(n, \mathbb{R})$ uniquely determines a linear transformation on $\mathbb{R}^n$, which we shall also denote by $\sigma$, by requiring that

(1)

 $$ \sigma(e_{j})=\sum_{i}\sigma_{i j}e_{i}. $$ 

In other words, if we consider the $n$-tuples of $\mathbb{R}^n$ as $n \times 1$ matrices, then $\sigma$ acts on $\mathbb{R}^n$ in the natural way by matrix multiplication. The map $(\sigma, v) \mapsto \sigma(v)$ gives an action of $Gl(n, \mathbb{R})$ on $\mathbb{R}^n$ on the left:

 $$ G l(n,\mathbb{R})\times\mathbb{R}^{n}\to\mathbb{R}^{n}. $$ 

Let  $ \langle\quad,\quad\rangle $ denote the standard inner product on  $ \mathbb{R}^n $ with respect to which the basis  $ \{e_i\} $ is orthonormal. Then if  $ \sigma\in G l(n,\mathbb{R}) $,

 $$ \langle\sigma(v),w\rangle=\langle v,\sigma^{t}(w)\rangle. $$ 

If  $ \sigma \in O(n) $, then  $ \sigma^t \sigma = I $, so it follows from (3) that

 $$ \langle\sigma(v),\sigma(v)\rangle=\langle v,\sigma^{t}\sigma(v)\rangle=\langle v,v\rangle; $$ 

thus $\sigma$ preserves lengths of vectors. Thus the action (2) restricted to $O(n) \times S^{n-1}$ factors through the unit sphere $S^{n-1}$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//6cc4845f-bbd3-4ae5-98d8-9e81fb995a7e/markdown_0/imgs/img_in_image_box_341_806_657_927.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2F5ca098b3406897a1ae0ffc87786955b0d83fc9492832222667a1beca1b9a3571" alt="Image" width="33%" /></div>


According to 1.32, the factoring map is smooth, so we have a natural  $ C^{\infty} $ action

 $$ O(n)\times S^{n-1}\to S^{n-1} $$ 

of the orthogonal group $O(n)$ on the unit sphere $S^{n-1}$ on the left. We claim that the action (6) is transitive. If $v_1 \in S^{n-1}$, let $\{v_1, v_2, \ldots, v_n\}$ be an orthonormal basis of $\mathbb{R}^n$ containing $v_1$ as the first element. Let

 $$ v_{i}=\sum_{j}\sigma_{j i}e_{j}. $$ 

Then the matrix  $ \sigma $ whose entries are determined by (7) is orthogonal, and

 $$ \sigma(e_{1})=v_{1}. $$ 

It follows that if v and w are any two points of  $ S^{n-1} $, there is an orthogonal matrix  $ \sigma $ such that  $ \sigma(v) = w $. Thus the action (6) is transitive.

The set of matrices in  $ O(n) $ of the form

 $$ \begin{array}{r l}{\sigma=}&{{}\left(\left(\begin{array}{l l l}{}&{}&{0}\\ {\bar{\sigma}}&{}&{}\end{array}\right)\begin{array}{l}{.}\\ {.}\\ {.}\end{array}\right)}\\ {}&{{}\left(\begin{array}{l l l}{0}&{\cdots}&{0}\\ \end{array}\right.\left.\begin{array}{l}{1}\\ {1}\end{array}\right)}\end{array} $$ 

forms a closed subgroup of $O(n)$. The matrices $\tilde{\sigma}$ occurring in this subgroup are precisely the matrices in $O(n-1)$. So $O(n-1)$ sits in $O(n)$ as this natural closed subgroup. We claim that $O(n-1)$ is precisely the isotropy group for the action (6) at $e_n\in S^{n-1}$. Clearly the elements of $O(n-1)$ leave $e_n$ fixed. On the other hand, suppose that $\sigma\in O(n)$ and that $\sigma(e_n)=e_n$. Now

 $$ \sigma(e_{n})=\sum_{i}\sigma_{i n}e_{i}, $$ 

so  $ \sigma_{in}=0 $ for  $ i<n $ and  $ \sigma_{nn}=1 $. Since  $ \sigma $ is orthogonal,  $ \sigma\sigma^{t}=I $, and this implies that  $ \sum\sigma_{ni}^{2}=1 $. Since  $ \sigma_{nn}=1 $, we must have  $ \sigma_{ni}=0 $,  $ i<n $. Thus  $ \sigma\in O(n-1) $. It follows from Theorem 3.62 that the map

 $$ O(n)/O(n-1)\to S^{n-1},\qquad\sigma O(n-1)\mapsto\sigma(e_{n}) $$ 

is a diffeomorphism. Thus the sphere  $ S^{n-1} $ is in a natural way diffeomorphic with the homogeneous manifold  $ O(n)/O(n-1) $.

By a similar argument one can show that there is a diffeomorphism of the sphere  $ S^{n-1} $ with the homogeneous manifold  $ \mathrm{SO}(n)/\mathrm{SO}(n-1) $.

(b) Let $\{e_t: i = 1, \ldots, n\}$ be the canonical complex basis of $\mathbb{C}^n$ where $e_t$ is the $n$-tuple consisting of all zeros except for a 1 in the $i$th spot. Just as in Example (a), each matrix $\sigma \in G/(n, \mathbb{C})$ uniquely determines a linear transformation of $\mathbb{C}^n$, which we still denote by $\sigma$, by requiring

 $$ \sigma(e_{j})=\sum_{i}\sigma_{i j}e_{i}. $$ 

So if we consider the complex $n$-tuples of $\mathbb{C}^*$ as $n \times 1$ matrices, then $\sigma$ acts by matrix multiplication. The map $(\sigma, v) \mapsto \sigma(v)$ is an action of

the real $2n^{8}$-dimensional Lie group $GI(n,\mathbb{C})$ on the real $2n$-dimensional manifold $\mathbb{C}^{*}$ on the left:

 $$ G l(n,\mathbb{C})\times\mathbb{C}^{n}\to\mathbb{C}^{n}. $$ 

Let  $ \langle $ ,  $ \rangle $ denote the standard inner product on  $ C^{*} $, where

 $$ \left\langle\sum_{i}a_{i}e_{i},\sum_{i}b_{i}e_{i}\right\rangle=\sum_{i=1}^{n}a_{i}\bar{b}_{i}. $$ 

Then if  $ \sigma \in Gl(n, \mathbb{C}) $,

 $$ \langle\sigma(v),w\rangle=\langle v,\bar{\sigma}^{t}(w)\rangle. $$ 

If $\sigma$ is an element of the unitary group $U(n)$, then $\bar{\sigma}^{i}\sigma = I$, so it follows from (14) that $\sigma$ preserves lengths of vectors in $\mathbb{C}^{n}$. If $X$ denotes the unit sphere in $\mathbb{C}^{n}$, then the action (12) restricted to $U(n) \times X$ factors through $X$, and so, by 1.32, yields a $C^{\infty}$ action

 $$ U(n)\times X\to X $$ 

of the unitary group $U(n)$ on the unit sphere $X \subset \mathbb{C}^*$ on the left. It follows by an argument similar to that in Example (a) that the action (15) is transitive and that the isotropy group for the action (15) at the point $e_n$ is simply $U(n-1)$, which we consider to be a closed subgroup of $U(n)$ by identifying $\tilde{\sigma} \in U(n-1)$ with

 $$ \begin{array}{r l}{\sigma=}&{{}\left(\left(\begin{array}{l l l}{}&{}&{0}\\ {}&{\tilde{\sigma}}&{}\end{array}\right)\begin{array}{l}{.}\\ {.}\\ {.}\end{array}\right)}\\ {}&{{}\left(\begin{array}{l l l}{0}&{\cdots}&{0}\\ {}&{1}&{}\end{array}\right)}\end{array} $$ 

in $U(n)$. Thus, by 3.62, $X$ is diffeomorphic with the homogeneous manifold $U(n)/U(n-1)$. But now under the canonical global coordinate system on $\mathbb{C}^n$ (given by the dual basis to the real basis $\{e_1, \ldots, e_n, \sqrt{-1}e_1, \ldots, \sqrt{-1}e_n\}$ of $\mathbb{C}^n$), $X$ is diffeomorphic with $S^{2n-1} \subset \mathbb{R}^{2n}$. Thus the sphere $S^{2n-1}$ is diffeomorphic with the homogeneous manifold $U(n)/U(n-1)$.

By a similar argument, the sphere $S^{2n-1}$ is also diffeomorphic with the homogeneous manifold $SU(n)/SU(n-1)$. In particular, since $SU(1)$ consists only of the $1\times1$ identity matrix, $S^{2}$ is diffeomorphic with $SU(2)$. Thus $S^{3}$ can be given a Lie group structure. It can be shown that $S^{1}$ and $S^{3}$ are the only spheres possessing Lie group structures [25].

(c) The real projective space  $ P^{n-1} $ is the set of equivalence classes of points in  $ \mathbb{R}^n - \{0\} $ where  $ (a_1, \ldots, a_n) $ is equivalent to  $ (b_1, \ldots, b_n) $ if there is a non-zero real number  $ c $ such that  $ ca_i = b_i $ for  $ i = 1, \ldots, n $. If  $ P^{n-1} $ is given the largest topology in which the natural projection

 $$ \pi\colon(\mathbb{R}^{n}-\{0\})\to P^{n-1} $$ 

is continuous, then $\pi$ restricted to $S^{n-1}$ is a 2-fold covering of $P^{n-1}$, and it is easily established that $P^{n-1}$ has a unique differentiable structure such that this covering map is locally a diffeomorphism. By an argument similar to that in Example (a), one can show that $P^{n-1}$ is diffeomorphic with the homogeneous space $SO(n)/O(n-1)$, where we consider $O(n-1)$ as a closed subgroup of $SO(n)$ by identifying $\tilde{\sigma}\in O(n-1)$ with the following element $\sigma$ of $SO(n)$:

 $$ \sigma=\left(\left(\begin{array}{c c c}{}&{}&{0}\\ {}&{\tilde{\sigma}}&{}\\ {}&{}&{}\\ {0}&{\cdots}&{0}&{\operatorname*{d e t}\tilde{\sigma}}\\ \end{array}\right)\right. $$ 

(d) As a set, the complex projective space $CP^{n-1}$ is the set of equivalence classes of points of $C^{n}-\{0\}$ under the equivalence relation in which $(\alpha_{1},\ldots,\alpha_{n})$ is equivalent to $(\beta_{1},\ldots,\beta_{n})$ if there is a non-zero complex number $\gamma$ such that $\gamma\alpha_{i}=\beta_{i}$ for $i=1,\ldots,n$. We make $CP^{n-1}$ into a real $2(n-1)$ dimensional manifold as follows. The action of the special unitary group on the unit sphere in $C^{n}$ preserves these equivalence classes, and each element of $CP^{n-1}$ has representatives of unit length; thus we have a natural transitive action of $SU(n)$ on the set $CP^{n-1}$:

 $$ S U(n)\times\mathbb{C}P^{n-1}\to\mathbb{C}P^{n-1}. $$ 

The subgroup of $SU(n)$ leaving fixed the point of $\mathbb{C}P^{n-1}$ determined by $e_n \in \mathbb{C}^n$ is simply $U(n-1)$, which we consider to be a closed subgroup of $SU(n)$ by identifying $\tilde{\sigma} \in U(n-1)$ with

 $$ \sigma=\left(\begin{matrix}{\left(\begin{array}{c}{\tilde{\sigma}}\\ {\phantom{0}}\\ \end{array}\right)}&{\left(\begin{array}{c}{0}\\ {\cdot}\\ {\cdot}\\ {\cdot}\\ {0}\\ \end{array}\right)}\\ {0}&{\cdots}&{0}&{1/(\operatorname*{d e t}\tilde{\sigma})}\\ \end{matrix}\right). $$ 

in SU(n). It follows that the map

 $$ \sigma U(n-1)\mapsto\{\sigma(e_{n})\}, $$ 

where $\{\sigma(e_n)\}$ denotes the point of $CP^{n-1}$ determined by $\sigma(e_n)$, is a well-defined one-to-one map of $SU(n)/U(n-1)$ onto $CP^{n-1}$. We give $CP^{n-1}$ the structure of a real $2(n-1)$ dimensional manifold by requiring that the map (19) be a diffeomorphism.

(e) Let $V$ be a real $d$-dimensional vector space, and let $S_{s}(V)$ be the set of $p$-frames in $V$. That is,

 $$ S_{p}(V)=\{\tilde{w}=(w_{1},\ldots,w_{p})\colon\mathrm{t h e}w_{1},\ldots,w_{p} $$ 

are linearly independent elements of $V$.

If we choose a basis $v_{1}, \ldots, v_{d}$ for $V$, then $Gl(d,\mathbb{R})$ acts on $V$ by matrix multiplication. We define

 $$ \eta\colon G l(d,\mathbb{R})\times S_{g}(V)\to S_{g}(V) $$ 

 $$ \begin{array}{r l}{\mathrm{b y}}&{\eta\big(\sigma,(w_{1},\ldots,w_{p})\big)=\big(\sigma(w_{1}),\ldots,\sigma(w_{p})\big).}\end{array} $$ 

Observe that if $\tilde{v}$, $\tilde{w} \in S_p(V)$, then there is a $\sigma \in G l(d, \mathbb{R})$ such that $\eta(\sigma, \tilde{v}) = \tilde{w}$. Now let $\tilde{s}$ be the element of $S_p(V)$ determined by the first $p$ elements of the basis $v_1, \ldots, v_d$; hence $\tilde{s} = (v_1, \ldots, v_p)$. Let $H$ be the subset of $Gl(d, \mathbb{R})$ leaving $\tilde{s}$ fixed. Then

 $$ H=\Big\{\left(\frac{I}{O}\left|\frac{A}{B}\right.\right)\in{G l}(d,\mathbb{R})\Big\}, $$ 

where $I$ is the $p \times p$ identity matrix; thus $H$ is a closed subgroup of $Gl(d,\mathbb{R})$. It follows that the map $\sigma H \mapsto \eta(\sigma,\tilde{s})$ is a one-to-one map of the homogeneous manifold $Gl(d,\mathbb{R})/H$ onto the set $S_p(V)$. We give $S_p(V)$ the structure of a $d \cdot p$-dimensional manifold by requiring that this map be a diffeomorphism. It is easily checked that this manifold structure is independent of the basis of $V$ chosen. $S_p(V)$ is called the Stiefel manifold of $p$-frames in $V$.

(f) Again let $V$ be a real $d$-dimensional vector space, and now let $M_{k}(V)$ be the set of all $k$-dimensional subspaces $(k$-planes) of $V$. If we choose a basis $v_{1}, \ldots, v_{d}$ for $V$, then the orthogonal group $O(d)$ acts naturally on $V$ by matrix multiplication; and since non-singular linear transformations map $k$-planes to $k$-planes, we have a map

 $$ \eta\colon O(d)\times M_{k}(V)\to M_{k}(V). $$ 

Observe that if $P$ and $Q$ are $k$-planes, then there is a $\sigma \in O(d)$ such that $\eta(\sigma,P) = Q$. Now, let $P_0$ be the $k$-plane spanned by the first $k$ elements of the basis $v_1, \ldots, v_d$, and let $H$ be the subset of $O(d)$ leaving $P_0$ fixed. Then

 $$ H=\Big\{\left(\frac{\sigma}{0}\Big|\frac{0}{\tau}\right)\in O(d)\colon\sigma\in O(k),\;\tau\in O(d-k)\Big\}, $$ 

so $H$ is a closed subgroup of $O(d)$ which we can identify with $O(k) \times O(d-k)$. Then the map $\sigma(O(k) \times O(d-k)) \mapsto \eta(\sigma, P_0)$ is a one-to-one map of the homogeneous manifold $O(d)/[O(k) \times O(d-k)]$ onto the set $M_k(V)$. We make $M_k(V)$ into a $(d-k)k$ dimensional manifold by requiring that this map be a diffeomorphism. One can check that this manifold structure on $M_k(V)$ is independent of the basis chosen for $V$. $M_k(V)$ is known as the Grassmann manifold of $k$-planes in $V$.

3.66 Proposition Let H be a closed subgroup of the Lie group G. If H and G/H are connected, then G is connected.

PROOF Assume that

where U and V are non-empty open subsets of G. Then

 $$ G=U\cup V $$ 

where $\pi(U)$ and $\pi(V)$ are non-empty open subsets of $G/H$. Since $G/H$ is connected, there must be a point $\sigma H$ of $G/H$ such that

 $$ G/H=\pi(U)\cup\pi(V) $$ 

 $$ \sigma H\in\pi(U)\cap\pi(V). $$ 

Now, (1) implies that

 $$ \sigma H=(\sigma H\cap U)\cup(\sigma H\cap V) $$ 

where $(\sigma H \cap U)$ and $(\sigma H \cap V)$ are both open subsets of $\sigma H$ (since $H$ has the relative topology). According to (3), both $(\sigma H \cap U)$ and $(\sigma H \cap V)$ are non-empty; thus, since $\sigma H$ is homeomorphic with $H$ and therefore connected, we have

 $$ (\sigma H\cap U)\cap(\sigma H\cap V)\neq\varnothing, $$ 

which implies that

 $$ U\cap V\neq\varnothing, $$ 

which proves that G is connected.

3.67 Theorem Each of the Lie groups $SO(n)$, $SU(n)$, and $U(n)$ is connected for $n\geq1$, and $O(n)$ has two components ($n\geq1$).

PROOF SO(1) and SU(1) are connected since they both consist only of the  $ 1 \times 1 $ identity matrix, and U(1) is connected since

 $$ U(1)=\{(\lambda)\colon\lambda\in\mathbb{C},|\lambda|=1\}. $$ 

That $SO(n)$, $SU(n)$, and $U(n)$ are connected for all $n$ now follows from 3.66 by using induction on $n$ and the representation of spheres as homogeneous manifolds given in 3.65.

Since every matrix in $O(n)$ has determinant $\pm1$, the orthogonal group can be written as the following union of two non-empty disjoint connected open subsets:

 $$ \begin{array}{l}{O(n)=S O(n)\cup\sigma S O(n)\quad\mathrm{w h e r e}\quad\sigma=\left(\begin{matrix}{-1}&{}&{}&{0}\\ {}&{1}&{}&{}\\ {}&{}&{\cdot}&{}\\ {}&{}&{}&{\cdot}\\ {}&{}&{}&{\cdot}\\ {0}&{}&{}&{1}\\ \end{matrix}\right)}\\ {\mathrm{T h u s~}O(n)\mathrm{~h a s~t w o~c o m p o n e n t s.}}\\ \end{array} $$ 

### 3.68 Theorem  $ Gl(n,\mathbb{R}) $ has two components.

PROOF Let $GI(n,\mathbb{R})^{+}$ be the subset of $GI(n,\mathbb{R})$ consisting of matrices with positive determinant, and let $GI(n,\mathbb{R})^{-}$ be the subset consisting of matrices with negative determinant. $GI(n,\mathbb{R})^{+}$ and $GI(n,\mathbb{R})^{-}$ are disjoint homeomorphic open subsets of $GI(n,\mathbb{R})$, so it suffices to prove that $GI(n,\mathbb{R})^{+}$ is connected. To do this, we shall show that each element of $GI(n,\mathbb{R})^{+}$ can be joined to the identity matrix by a continuous curve.

First we show that each element of $Gl(n, \mathbb{R})$ has a polar decomposition; that is, each matrix $\sigma \in Gl(n, \mathbb{R})$ can be expressed in the form

 $$ \sigma=P R $$ 

where $P$ is a positive definite symmetric matrix and $R \in O(n)$. (Recall that all the eigenvalues of a symmetric matrix are real, and that a symmetric matrix is positive definite if each of its eigenvalues is strictly positive.) Since $(\sigma\sigma^t)^t = \sigma\sigma^t$, $\sigma\sigma^t$ is symmetric. Let $a$ be an eigenvalue of $\sigma\sigma^t$ with eigenvector $v \in \mathbb{R}^*$. Then, according to 3.65(3), if $\langle \cdot, \rangle$ denotes the standard inner product in $\mathbb{R}^*$,

 $$ a\langle v,v\rangle=\langle\sigma\sigma^{t}(v),v\rangle=\langle\sigma^{t}(v),\sigma^{t}(v)\rangle. $$ 

Consequently, $a \geq 0$, and since $\sigma\sigma^t$ is non-singular, we must have $a > 0$. Thus $\sigma\sigma^t$ is a positive definite symmetric matrix. Since $\sigma\sigma^t$ is symmetric, there exists an orthogonal matrix $\beta \in O(n)$ such that the matrix

 $$ \beta\sigma\sigma^{\dagger}\beta^{\dagger} $$ 

is diagonal (cf. Exercise 22(a)). Since the eigenvalues of $\sigma\sigma^{t}$ are all positive, the matrix (2) has a square root

 $$ (\beta\sigma\sigma^{t}\beta^{t})^{1/2}; $$ 

that is, (3) is a diagonal matrix, and each diagonal entry is the positive square root of the corresponding entry in the matrix (2). Let

 $$ P=\beta^{t}(\beta\sigma\sigma^{t}\beta^{t})^{\mathbf{1}/2}\beta, $$ 

and let

 $$ R=P^{-1}\sigma. $$ 

P is a positive definite symmetric matrix, and R is orthogonal since (4) implies that  $ P^{2} = \sigma\sigma^{t} $ and therefore that

 $$ \begin{aligned}{R R^{t}}&{{}=P^{-1}\sigma\sigma^{t}(P^{-1})^{t}=P^{-1}\sigma\sigma^{t}(P^{t})^{-1}}\\ {}&{{}=P^{-1}\sigma\sigma^{t}P^{-1}=P^{-1}P P P^{-1}=I.}\\ \end{aligned} $$ 

Thus  $ \sigma = PR $, as we asserted in (1).

If $\sigma \in G l(n, \mathbb{R})^+$, then $\sigma$ has a polar decomposition (1), where now $R$ must have positive determinant; thus $R \in SO(n)$. Let

 $$ P_{t}=t I+(1-t)P $$ 

for $t \in [0,1]$. Then $P_t$ is positive definite for each $t$, so the path $t \mapsto P_tR$ is a continuous curve in $Gl(n,\mathbb{R})^+$ joining $\sigma$ to $R$. Since $SO(n)$ is connected, and therefore pathwise connected, $R$ can be joined to the identity matrix $I$ by a continuous curve. Thus $Gl(n,\mathbb{R})^+$ is pathwise connected, which completes the proof that $Gl(n,\mathbb{R})$ has two components.

##### EXERCISES

1 Prove that a connected Lie group is automatically second countable; that is, the assumption of second countability in the definition of connected Lie group is redundant.

2 Show that the examples in 3.3 are Lie groups.

3 Prove that the examples in 3.5 are Lie algebras.

4 Supply a proof for Proposition 3.12.

5 Prove the necessity of the connectedness assumption in 3.16.

6 Let $\mathcal{I}$ be an ideal of forms on $G^{c}$ generated by a collection $\{\omega_{1},\ldots,\omega_{c-d}\}$ of independent left invariant 1-forms. Let $\mathfrak{h}\subseteq\mathfrak{g}$ be the $d$-dimensional subspace of the Lie algebra of $G$ annihilated by the $\omega_{i}$ ($i=1,\ldots,c-d$). Prove that $\mathfrak{h}$ is a subalgebra of $\mathfrak{g}$ if and only if $\mathcal{I}$ is a differential ideal.

7 In this exercise we outline the proof of Theorem 3.23.

(a) Let $\pi\colon (X,x_0)\to(Y,y_0)$ be a covering, and let $\alpha\colon (Z,z_0)\to(Y,y_0)$ be a continuous map where $Z$ is pathwise and locally pathwise connected, and where $a_\ast(\pi_1(Z,z_0))\subset\pi_\ast(\pi_1(X,x_0))$. Prove that there is a unique continuous map $\tilde{\alpha}\colon(Z,z_0)\to(X,x_0)$ such that $\pi\circ\tilde{\alpha}=\alpha$.

(Sketch: First prove part (a) for the case in which $Z$ is the unit rectangle $[0,1] \times [0,1]$ and $z_0 = (0,0)$. Here the condition on the fundamental groups is trivially satisfied, and the proof follows by partitioning the unit rectangle fine enough so that each subrectangle of the partition maps under $\alpha$ into an evenly covered set in $Y$. As a particular application of this case, it follows that each path in $Y$ has a unique lift to $X$ once base points are chosen.

For the general case, define the lifting $\tilde{\alpha}$ of $\alpha$ as follows. Let $z \in Z$, and let $\gamma: [0,1] \to Z$ be a path joining $z_0$ to $z$; thus $\gamma(0) = z_0$ and $\gamma(1) = z$. Then $\alpha \circ \gamma$ has a unique lift $\tilde{\gamma}$ to $X$ such that $\tilde{\gamma}(0) = x_0$. Set $\tilde{\alpha}(z) = \tilde{\gamma}(1)$. Now use the condition on the fundamental groups and the unique lifting property already established for rectangles to show that $\tilde{\alpha}$ is well-defined, independent of the choice of the path $\gamma$ from $z_0$ to $z$. Finally use the local path-connected property of $Z$ to show that $\tilde{\alpha}$ is continuous.)

(b) If $X$ is a pathwise connected, locally pathwise connected, and semi-locally 1-connected topological space, then $X$ has a simply connected covering space.

(Sketch: Fix a base point $x_0 \in X$. We define an equivalence relation on the set of all paths in $X$ with domain [0,1] and with initial point $x_0$. Two such paths $\gamma_1$, $\gamma_2$ will be called equivalent if $\gamma_1(1) = \gamma_2(1)$, and the loop $\gamma_2^{-1}\gamma_1$ at $x_0$ obtained by first traversing $\gamma_1$ and then traversing $\gamma_2$ in the reverse direction is homotopically trivial at $x_0$. The point set of the simply connected covering space $\tilde{X}$ of $X$ is the set of such equivalence classes $\{\gamma\}$. The projection map $\pi: \tilde{X} \to X$ is defined by $\pi(\{\gamma\}) = \gamma(1)$. Let $\{\gamma\} \in \tilde{X}$, and let $U$ be an open neighborhood of $\gamma(1)$ in $X$. Let $U(\{\gamma\})$ consist of all elements $\{\tau\}$ of $\tilde{X}$ possessing a representative path $\tau$ which first traverses $\gamma$ and then remains in $U$. Prove that the collection of such sets $U(\{\gamma\})$ forms a basis for a topology on $\tilde{X}$ in which $\tilde{X}$ is simply connected, and in which $\pi: \tilde{X} \to X$ becomes a covering.)

(c) A covering of a simply connected space is a homeomorphism. (This is an immediate application of part (a).)

8 Prove that if $\pi: \tilde{M} \to M$ is a covering of a differentiable manifold $M$, then $\tilde{M}$ is second countable. (It suffices to prove that $\pi_{1}(M, m)$ is countable. This follows easily from the observation that $M$ can be covered by a countable number of open sets, each homeomorphic with an open ball in Euclidean space.)

9 Let $G$ and $H$ be Lie groups with $G$ connected. Prove that a $C^{\infty}$ map $\varphi: G \to H$ sending the identity of $G$ to the identity of $H$ is a homomorphism if $\delta\varphi$ pulls left invariant forms on $H$ back to left invariant forms on $G$. Show that the assumption of connectedness for $G$ is necessary. (Hint: One can construct a differential ideal on $G \times H$ as in 3.15(5) whose maximal connected integral submanifold $I$ through $(e,e)$ is a Lie subgroup of $G \times H$. Factor the graph of $\varphi$ through $I$, and show that the natural covering homomorphism of $I$ onto $G$ is 1:1.)

10 Prove that  $ \begin{pmatrix}-2 & 0 \\ 0 & -1\end{pmatrix} $ is not  $ e^A $ for any  $ A \in \mathrm{gl}(2, \mathbb{R}) $.

11 Let  $ \sigma(t) $ and  $ \beta(t) $ be smooth curves in a Lie group G such that  $ \sigma(0) = \beta(0) = e $, and let  $ \alpha(t) = \sigma(t)\beta(t) $. Prove that

 $$ \dot{\alpha}(0)=\dot{\sigma}(0)+\dot{\beta}(0). $$ 

(Hint: Consider the group multiplication map  $ \eta\colon G\times G\to G $, that is,  $ \eta(\gamma,\tau)=\gamma\tau $. Let  $ v,w\in G_s $, and show that

 $$ d\eta(v,w)=d\eta\big((v,0)+(0,w)\big)=v+w. $$ 

12 Let $G$ be a connected Lie group, and let $\varphi: G \to H$ be a homomorphism with a discrete kernel. Prove that the kernel lies in the center of $G$. Use this fact to prove that the fundamental group of a Lie group is abelian.

13 Prove that Example 3.5(d) is, up to isomorphism, the only 2-dimensional non-abelian Lie algebra. Conclude that Example 3.3(h) is, up to isomorphism, the unique simply connected 2-dimensional non-abelian Lie group.

14 Show that there are matrices  $ A, B \in \mathrm{gl}(n, \mathbb{C}) $ such that  $ e^{A+B} \neq e^{A} e^{B} $.

15 Prove that the exponential map for $GI(n,\mathbb{C})$ is surjective. (Outline: First, by using the Jordan canonical form, reduce the problem to that of showing that each elementary Jordan matrix (a matrix with a fixed constant $\lambda$ on the diagonal, with $1$'s immediately above each diagonal entry, and with zeros elsewhere) in $GI(j,\mathbb{C})$, for $1 \leq j \leq n$, is the exponential of an element of $gl(j,\mathbb{C})$. Let $A$ be an elementary Jordan matrix. Write $A$ as $(\lambda I) \cdot N$ where the diagonal entries of $N$ are $1^s$. Prove that $\lambda I = e^{A_1}$ and that $N = e^{A_s}$, where $A_1 A_s = A_s A_1$. To find $A_s$, observe that since sufficiently high powers of the difference $I - N$ vanish, $N$ has a logarithm, namely,

 $$ \log N=-\sum_{k=1}^{\infty}\frac{(I-N)^{k}}{k}\;. $$ 

Use a formal power series argument to show that  $ e^{\log N} = N $.

16 Let $G$ be a Lie group. A vector field $Y$ on $G$ is right invariant if $Y$ is $r_\sigma$-related to itself for each $\sigma\in G$. Prove that the set of right invariant vector fields on $G$ forms a Lie algebra under the Lie bracket operation and is naturally isomorphic as a vector space with $G_\sigma$. Let $\varphi: G\to G$ be the diffeomorphism defined by $\varphi(\sigma)=\sigma^{-1}$. Prove that if $X$ is a left invariant vector field on $G$, then $d\varphi(X)$ is the right invariant vector field whose value at $e$ is $-\chi(e)$. Prove that $X\mapsto d\varphi(X)$ gives a Lie algebra isomorphism of the Lie algebra of left invariant vector fields on $G$ with the Lie algebra of right invariant vector fields on $G$.

17 Find an example of a Lie group $G$ with a Lie subgroup $A$ that is not closed in $G$.

18 Let $G$ be an $n$-dimensional abelian connected Lie group. Prove there is an integer $k$, $0 \leq k \leq n$, such that $G$ is isomorphic with $\mathbb{R}^{n-k} \times T^k$ where $T^k$ is a torus of dimension $k$. First, prove that up to isomorphism, $\mathbb{R}^n$ is the unique simply connected abelian Lie group. Next, show that if $D$ is a discrete subgroup of $\mathbb{R}^n$, then either $D = \{0\}$ or there is an integer $k$, $1 \leq k \leq n$, and $k$ linearly independent vectors $v_1, \ldots, v_k$ in $\mathbb{R}^n$ which generate $D$. To prove this, suppose that $D \neq \{0\}$, and let $k$ be the smallest integer such that $D$ is contained in a $k$-dimensional subspace $V$ of $\mathbb{R}^n$. Find a basis $w_1, \ldots, w_k$ for $V$ such that the $w_i \in D$. Let

 $$ A_{i}=\left\{\sum_{j=1}^{\epsilon}r_{j}w_{j}\colon0\leq r_{j}\leq1,r_{\epsilon}>0\right\} $$ 

for $i = 1, \ldots, k$. Choose $v_i$ to be an element of $A_i \cap D$ with smallest possible coefficient $r_i$. Then $\{v_1, \ldots, v_k\}$ will be a linearly independent set generating $D$.

19 Supply a proof for 3.56.

20 Prove that the group of automorphisms of a connected Lie group $G$ is itself a Lie group. (Outline: Let $\tilde{G}$ be the simply connected covering group of $G$, and let $\pi$ be the covering homomorphism. Let $D = \ker \pi$. We know from 3.57(b) that the group $A(\tilde{G})$ of automorphisms of $\tilde{G}$ is a Lie group. Show that the group of automorphisms of $G$ is naturally isomorphic with the (closed) subgroup of $A(\tilde{G})$ consisting of those automorphisms of $\tilde{G}$ which map $D$ onto $D$.)

21 Prove that  $ U(n) $ is diffeomorphic with  $ S^{1} \times SU(n) $.

22 (a) Deduce from a “super-triangularization” argument similar to that following 3.35(6), but now using unit eigenvectors and orthogonal complements, that if $A$ is a hermitian matrix (that is, $A$ is complex and $\bar{A}=A^{t}$), then there exists a unitary

matrix $B$ such that $BAB^{-1}$ is diagonal. By a similar argument, prove that if $A$ is a real symmetric matrix ($A = A^{t}$), then there exists a real orthogonal matrix $B$ such that $BAB^{-1}$ is diagonal.

(b) Using part (a) and 3.46(7), prove that the exponential map maps the hermitian matrices one-to-one onto the set of positive definite (all eigenvalues positive) hermitian matrices. Deduce also that the exponential map maps the real symmetric matrices one-to-one onto the set of positive definite symmetric matrices.

23 Use part (b) of Exercise 22 to prove that the polar decomposition 3.68(1) is unique. (Hint: If  $ \sigma = PR = P_{1}R_{1} $, first prove that  $ P^{2} = P_{1}^{2} $, then apply part (b) of Exercise 22 to P and  $ P_{1} $.)

24 Prove that every matrix  $ \sigma \in G l(n, \mathbb{C}) $ can uniquely be written as a product  $ \sigma = PR $, where  $ P $ is a positive definite hermitian matrix and  $ R $ is a unitary matrix.

25 Prove that $GI(n,\mathbb{C})$ is connected.

26 Complete the details of 3.65(b) and (c).

INTEGRATION ON MANIFOLDS

We shall consider integration of $p$-forms over differentiable singular $p$-chains in $n$-dimensional manifolds, and integration of $n$-forms over regular domains in oriented $n$-dimensional manifolds. For both of these situations we shall prove a version of Stokes' theorem. This is a generalization of the Fundamental Theorem of Calculus and is undoubtedly the single most important theorem in the subject. We shall also consider integration on Riemannian manifolds and on Lie groups. Finally, we shall introduce the de Rham cohomology groups and shall prove the Poincaré lemma, from which we will conclude that the de Rham cohomology groups of Euclidean space are trivial. This lemma will be of central importance for the de Rham theorem, which is stated at the end of this chapter and proved in Chapter 5.

##### ORIENTATION

4.1 Definitions Let $V$ be a real vector space of dimension $n$. The notion of an orientation on $V$ was introduced in Exercise 13 of Chapter 2. Recall that the $n$th exterior power $\Lambda_n(V)$ is 1-dimensional, so that $\Lambda_n(V) - \{0\}$ has two components. An orientation on $V$ is a choice of a component of $\Lambda_n(V) - \{0\}$.

Now let $M$ be a connected differentiable manifold of dimension $n$. We shall call $M$ orientable if it is possible to choose in a consistent way an orientation on $M_m^*$ for each $m \in M$. More precisely, let $O$ be the “0-section” of the exterior $n$-bundle $\Lambda_n^*(M)$; that is,

 $$ O=\bigcup_{m\in\mathcal{M}}\left\{0\in\Lambda_{n}(M_{m}^{*})\right\}. $$ 

Then since each $\Lambda_n(M_m^*) - \{0\}$ has exactly two components, it follows easily that $\Lambda_n^*(M) - O$ has at most two components. We say that $M$ is orientable if $\Lambda_n^*(M) - O$ has two components; and if $M$ is orientable, an orientation on $M$ is a choice of one of the two components of $\Lambda_n^*(M) - O$.

A non-connected manifold $M$ is said to be orientable if each component of $M$ is orientable, and an orientation is a choice of orientation on each component. Let $M$ be oriented, and let $v_{1}, \ldots, v_{n}$ be a basis of $M_{m}$ with dual basis $\delta_{1}, \ldots, \delta_{n}$. We say that the (ordered) basis $v_{1}, \ldots, v_{n}$ is oriented if $\delta_{1} \wedge \cdots \wedge \delta_{n}$ belongs to the orientation.

Let $M$ and $N$ be orientable $n$-dimensional manifolds, and let $\psi: M \to N$ be a differentiable map. We say that $\psi$ preserves orientations if the induced map $\delta\psi: \Lambda_n^*(N) \to \Lambda_n^*(M)$ maps the component of $\Lambda_n^*(N) - O$ determining the orientation on $N$ into the component of $\Lambda_n^*(M) - O$ determining the orientation on $M$. Equivalently, $\psi$ is orientation-preserving if $d\psi$ sends oriented bases of the tangent spaces to $M$ into oriented bases of the tangent spaces to $N$.

4.2 Proposition Let M be a differentiable manifold of dimension n. Then the following are equivalent:

(a) M is orientable.

(b) There is a collection $\Phi = \{(V,\psi)\}$ of coordinate systems on $M$ such that

 $$ M=\bigcup_{(V,\psi)\in\Phi}V\qquad{a n d}\qquad\operatorname*{d e t}\left(\frac{\partial x_{i}}{\partial y_{j}}\right)>0\quad{o n}\quad U\cap V $$ 

whenever $(U, x_{1}, \ldots, x_{n})$ and $(V, y_{1}, \ldots, y_{n})$ belong to $\Phi$.

(c) There is a nowhere-vanishing n-form on M.

PROOF We can assume, without loss of generality, that $M$ is connected. We prove that (a) $\Rightarrow$ (b) $\Rightarrow$ (c) $\Rightarrow$ (a). Given (a), that $M$ is orientable, choose an orientation on $M$; that is, we choose one of the two components, call it $\Lambda$, of $\Lambda_n^*(M) - O$. Observe that for each $m \in M$, $\Lambda \cap \Lambda_n(M_m^*)$ is precisely one of the two components of $\Lambda_n(M_m^*) - \{0\}$. Now let $\Phi$ consist of all of those coordinate systems $(V, y_1, \ldots, y_n)$ on $M$ such that the map of $V$ into $\Lambda_n^*(M)$ defined by

 $$ m\mapsto(d y_{1}\land\cdots\land d y_{n})(m) $$ 

has range in $\Lambda$. Now, if $(U, x_1, \ldots, x_n)$ and $(V, y_1, \ldots, y_n)$ are any two coordinate systems on $M$, then for $m \in U \cap V$,

 $$ (d x_{1}\wedge\dotsm\wedge d x_{n})(m)=\mathsf{d e t}\biggl(\frac{\partial x_{i}}{\partial y_{j}}\bigg|_{m}\biggr)(d y_{1}\wedge\dotsm\wedge d y_{n})(m). $$ 

If these coordinate systems belong to $\Phi$, then necessarily

 $$ \det\left(\frac{\partial x_{i}}{\partial y_{j}}\bigg|_{m}\right)>0 $$ 

for each $m \in U \cap V$. Consequently, (1) is satisfied, and result (b) follows from (a).

Now assume (b). Let $\{\varphi_i\}$ be a partition of unity subordinate to the cover of $M$ given by the coordinate neighborhoods in the collection $\Phi$ with $\varphi_i$ subordinate to $(V_i, x_1^i, \ldots, x_n^i)$. Then

 $$ \omega=\sum_{i}\varphi_{i}d x_{1}{}^{i}\wedge\cdots\wedge d x_{n}{}^{i} $$ 

is a global $n$-form on $M$, where $\varphi_i \, dx_1^i \wedge \cdots \wedge dx_n^i$ is defined to be the $0$-form outside of $V_i$. That $\omega$ vanishes nowhere follows from the fact that for each $m$, $\omega(m)$ is a finite sum with positive coefficients of elements of one component of $\Lambda_n(M_m^*) - \{0\}$. Thus (c) follows from (b).

Finally, let  $ \omega $ be a nowhere-vanishing n-form on M, and let

 $$ \Lambda^{+}=\bigcup_{m\in\mathcal{M}}\{a\omega(m)\colon a\in\mathbb{R},a>0\}, $$ 

 $$ \Lambda^{-}=\bigcup_{m\in\mathcal{M}}\{a\omega(m)\colon a\in\mathbb{R},\;a<0\}. $$ 

Then  $ \Lambda_n^*(M) - O $ is the disjoint union of the two open subsets  $ \Lambda^+ $ and  $ \Lambda^- $, so  $ \Lambda_n^*(M) - O $ is disconnected, and  $ M $ is orientable.

### 4.3 Examples

(a) Every Lie group $G$ is orientable, for if $\omega_1, \ldots, \omega_n$ is a basis for the left invariant 1-forms on $G$, then $\omega_1 \wedge \cdots \wedge \omega_n$ is a global nowhere-vanishing $n$-form on $G$.

(b) The standard orientation on the Euclidean space  $ \mathbb{R}^d $ is the one determined by the  $ d $-form  $ dr_1 \wedge \cdots \wedge dr_d $.

(c) Let $X$ be a $d$-dimensional manifold, and suppose that there exists an immersion $f: X \to \mathbb{R}^{d+1}$. A normal vector field along $(X, f)$ is a smooth map $N: X \to T(\mathbb{R}^{d+1})$ such that for each $p \in X$, the vector $N(p)$ lies in $(\mathbb{R}^{d+1})_{f(p)}$ and is orthogonal to the subspace $df(X_p) \subset (\mathbb{R}^{d+1})_{f(p)}$. Such a manifold $X$ is orientable if and only if there is a smooth nowhere-vanishing normal vector field along $(X, f)$. (See Exercise 1.)

(d) As an immediate application of Example (c), the sphere  $ S^{*} $ is orientable for each  $ n \geq 1 $.

(e) The real projective space  $ P^n $ is orientable if and only if n is odd. (See Exercise 2.)

##### INTEGRATION ON MANIFOLDS

4.4 Integration in the Euclidean Space  $ \mathbb{R}^n $ We assume that the reader is familiar with some theory of integration in  $ \mathbb{R}^n $. Since we shall be integrating continuous (in fact usually  $ C^\infty $) functions over nice subsets of  $ \mathbb{R}^n $

(polyhedra for example), the theory of the Riemann integral will be quite sufficient. The principal theorem that we need to recall is the change of variables formula. Several versions of this formula and their proofs may be found in [6], [18], or [29]. A version sufficient for our purposes is the following. Let $\varphi$ be a diffeomorphism of a bounded open set $D$ in $\mathbb{R}^{n}$ with a bounded open set $\varphi(D)$. Let $J_{\varphi}$ denote the determinant of the Jacobian matrix of $\varphi$:

 $$ J_{\varphi}=\det\left(\frac{\partial\varphi_{i}}{\partial r_{j}}\right)\;. $$ 

Let $f$ be a bounded continuous function on $\varphi(D)$, and let $A$ be a nice subset of $D$. ($A$ will be polyhedral in most of our applications. Generally, for the Riemann theory, a nice subset would be one which has Jordan content.) Then

 $$ \int_{\varphi(A)}f=\int_{A}f\circ\varphi\mid J\varphi\mid. $$ 

4.5 Integration of $n$-forms in $\mathbb{R}^n$. As usual, we let $r_1, \ldots, r_n$ denote the canonical coordinate system on $\mathbb{R}^n$. The standard orientation is determined by the $n$-form $dr_1 \wedge \cdots \wedge dr_n$. Now let $\omega$ be an $n$-form on an open set $D \subset \mathbb{R}^n$. Then there is a uniquely determined function $f(D)$ such that $\omega = f dr_1 \wedge \cdots \wedge dr_n$. Let $A \subset D$. We define

 $$ \int_{A}\omega=\int_{A}f, $$ 

provided that the latter exists. We can restate the change of variables formula 4.4(1) in terms of differential forms. Let $\varphi$, $D$, and $A$ be as in 4.4, and let $\omega$ be an $n$-form on $\varphi(D)$. Then

 $$ \int_{\varphi(A)}\omega=\pm\int_{A}\delta\varphi(\omega), $$ 

where one uses “+” if φ is orientation preserving and “−” if φ is orientation reversing.

4.6 Integration over Chains The first type of integration that we shall consider on general manifolds involves integration of $p$-forms over differentiable singular $p$-chains in an $n$-manifold.

For each  $ p \geq 1 $ we let

 $$ \Delta^{p}=\Big\{(a_{1},\ldots,a_{p})\in\mathbb{R}^{p}\colon\sum_{i=1}^{p}a_{i}\leq1,\mathrm{a n d~e a c h}a_{i}\geq0\Big\}. $$ 

$\Delta^{\flat}$ is called the standard $p$-simplex in $\mathbb{R}^{p}$. For $p=0$, we set $\Delta^{\flat}$ equal to the $1$-point space $\{0\}$; $\Delta^{\flat}$ is the standard $0$-simplex. Let $M$ be a manifold. A differentiable singular $p$-simplex $\sigma$ in $M$ is a map $\sigma$ of $\Delta^{\flat}$ into $M$ which extends to be a differentiable $(C^{\infty})$ map of a neighborhood of $\Delta^{\flat}$ in $\mathbb{R}^{p}$ into $M$.

In this chapter we shall refer to such a $\sigma$ as simply a $p$-simplex $\sigma$ in $M$. (In Chapter 5 we shall deal, in addition, with continuous singular simplices, and so there we shall need to retain the term “differentiable” for distinction.) A $0$-simplex in $M$ consists of a map of the 1-point space $\{0\}$ into $M$. $\mathbf{A}p$-chain $c$ in $M$ (with real coefficients) is a finite linear combination $c=\sum a_i\sigma_i$ of $p$-simplices $\sigma_i$ in $M$ where the $a_i$ are real numbers.

For each $p \geq 0$ we define a collection of maps $k_i^{p}: \Delta^{p} \to \Delta^{p+1}$ for $0 \leq i \leq p + 1$ as follows:

 $$ \mathrm{f o r}\quad p=0,\quad k_{0}^{0}(0)=1\quad\mathrm{a n d}\quad k_{1}^{0}(0)=0;. $$ 

 $$ \begin{array}{l l}{\mathrm{f o r}\quad p\geq1,}&{\begin{cases}{k_{0}^{p}(a_{1},\ldots,a_{p})=\left(1-\sum_{i=1}^{p}a_{i},a_{1},\ldots,a_{p}\right)\quad\mathrm{a n d}}\\ {k_{i}^{p}(a_{1},\ldots,a_{p})=(a_{1},\ldots,a_{i-1},0,a_{i},\ldots,a_{p})}\\ {\quad(1\leq i\leq p+1).}\\ \end{cases}}\\ \end{array} $$ 

If  $ \sigma $ is a  $ p $-simplex in  $ M $ with  $ p \geq 1 $, we define its  $ ith $ face,  $ 0 \leq i \leq p $, to the  $ (p-1) $ simplex

 $$ \sigma^{i}=\sigma\circ k_{i}^{p-1}, $$ 

and we define the boundary of  $ \sigma $ to be the  $ (p - 1) $ chain

 $$ \partial\sigma=\sum_{i=0}^{p}(-1)^{i}\sigma^{i}. $$ 

We extend the boundary operator linearly to chains. Note carefully the use of the superscript to denote faces. Thus the boundary of the $p$-chain $\sum_{i=1}^{k}a_{i}\sigma_{i}$ is

 $$ \sum_{i=0}^{p}\sum_{j=1}^{k}(-1)^{i}a_{j}\sigma_{j}^{i}. $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//68eb7030-687c-46d6-ba6b-86d43af3e6c1/markdown_1/imgs/img_in_image_box_125_823_775_1072.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A14Z%2F-1%2F%2F31003b2ede52bcc3481773f1736e062336a58398a95a8cb1e9f90c4fa2de84f2" alt="Image" width="66%" /></div>


We claim that

 $$ k_{i}^{p+1}\circ k_{j}^{p}=k_{j+1}^{p+1}\circ k_{i}^{p}\qquad(p\geq0;i\leq j). $$ 

For $p=0$, check the three possible cases separately. For $p\geq1$, observe that both sides of (5) give the following maps:

 $$ \begin{aligned}{}&{{}\quad1\leq i<j\quad(a_{1},\ldots,a_{p})\mapsto(a_{1},\ldots,a_{i-1},0,a_{i},\ldots,a_{j-1},0,a_{j},\ldots,a_{p})}\\ {}&{{}\quad1\leq i=j\quad(a_{1},\ldots,a_{p})\mapsto(a_{1},\ldots,a_{i-1},0,0,a_{i},\ldots,a_{p})}\\ {}&{{}\quad0=i<j\quad(a_{1},\ldots,a_{p})\mapsto\bigg(1-\sum_{i=1}^{p}a_{i},a_{1},\ldots,a_{j-1},0,a_{j},\ldots,a_{p}\bigg)}\\ {}&{{}\quad0=i=j\quad(a_{1},\ldots,a_{p})\mapsto\bigg(0,1-\sum_{i=1}^{p}a_{i},a_{1},\ldots,a_{p}\bigg).}\\ \end{aligned} $$ 

It follows from (5), (3), and (4) that the boundary of the boundary of a chain is always 0. That is,

 $$ \partial\circ\partial=0. $$ 

Now let $\sigma$ be a $p$-simplex in $M$, and let $\omega$ be a $p$-form defined on a neighborhood of the image of $\sigma$. In most of our applications we shall deal only with smooth forms, but for the purposes of the following definition it would be quite sufficient for $\omega$ to be a continuous $p$-form. First of all, if $p = 0$, then a 0-simplex consists simply of a point in $M$, and a 0-form is simply a function. In this case, we define the integral of the function $\omega$ over the 0-simplex $\sigma$ to be the value of $\omega$ at the point $\sigma(0) \in M$:

 $$ \int_{\sigma}\omega=\omega\left(\sigma(0)\right). $$ 

If $p \geq 1$, then since $\sigma$ extends to be a smooth map of a neighborhood of $\Delta^p$ in $\mathbb{R}^p$ into $M$, $\omega$ can be pulled back via $\sigma$ to a $p$-form $\delta\sigma(\omega)$ on a neighborhood of $\Delta^p$. In this case, we define the integral of the $p$-form $\omega$ over the $p$-simplex $\sigma$ by

 $$ \int_{\sigma}\omega=\int_{\Delta^{v}}\delta\sigma(\omega). $$ 

We extend these integrals linearly to chains, so that if  $ c = \sum a_i \sigma_i $, then

 $$ \int_{e}\omega=\sum a_{i}\int_{\sigma_{i}}\omega. $$ 

Perhaps the single most important theorem in integration theory on manifolds is Stokes' theorem. This is a generalization of the Fundamental Theorem of Calculus. Observe that in our context the Fundamental Theorem says that if $F$ is a smooth function on the real line, and if $\sigma$ is a smooth 1-simplex in the real line, then

 $$ \int_{\mathfrak{s g}}F=\int_{\sigma}d F. $$ 

We shall present two versions of Stokes' theorem. The first is in terms of integration of forms over chains.

4.7 Stokes' Theorem I Let $c$ be a $p$-chain ($p \geq 1$) in a differentiable manifold $M$, and let $\omega$ be a smooth ($p-1$) form defined on a neighborhood of the image of $c$. Then

 $$ \int_{\partial e}\omega=\int_{e}d\omega. $$ 

PROOF It is sufficient to consider the case in which the p-chain c consists of a single p-simplex  $ \sigma $. Thus we must prove that

 $$ \int_{\sigma}d\omega=\int_{\partial\sigma}\omega. $$ 

It follows immediately from our definitions that (2) is equivalent with

 $$ \int_{\Delta^{p}}d\left(\delta\sigma(\omega)\right)=\sum_{i=0}^{p}(-1)^{i}\int_{\Delta^{p-1}}\delta\sigma^{i}(\omega)=\sum_{i=0}^{p}(-1)^{i}\int_{\Delta^{p-1}}\delta k_{i}^{p-1}\circ\delta\sigma(\omega). $$ 

Observe first of all that the case p = 1 reduces directly to the Fundamental Theorem of Calculus:

 $$ \int_{\Delta^{1}}\frac{d}{d r}(\omega\circ\sigma)d r=\omega\big(\sigma(1)\big)-\omega\big(\sigma(0)\big), $$ 

so we now assume that  $ p \geq 2 $. Then the  $ (p - 1) $ form  $ \delta\sigma(\omega) $ can be expressed as

 $$ \delta\sigma(\omega)=\sum_{j=1}^{p}a_{j}\mathop{}{d}r_{1}\wedge\dots\wedge\widehat{{d r}_{j}}\wedge\dots\wedge\mathop{}{d}r_{p}, $$ 

where the circumflex over a term means that the term is to be omitted, and where the $a_i$ are $C^\infty$ functions on a neighborhood of $\Delta^p$ in $\mathbb{R}^p$. Since the integral is linear, we may consider the special case in which $\delta\sigma(\omega)$ consists of a single term of the form $a_i dr_1 \wedge \cdots \wedge \widehat{dr}_j \wedge \cdots \wedge dr_p$. In this case, the left-hand side of (3) becomes

 $$ (-1)^{t-1}\int_{\Delta^{p}}\frac{\partial a_{j}}{\partial r_{j}}d r_{1}\wedge\cdots\wedge d r_{p}. $$ 

To evaluate the right-hand side of (3), we observe that for  $ 1 \leq i \leq p $,

 $$ \delta k_{i}^{s-1}(r_{j})=\left\{\begin{matrix}{r_{j}}&{}&{(1\leq j\leq i-1)}\\ {0}&{}&{(j=i)}\\ {r_{j-1}}&{}&{(i+1\leq j\leq p),}\\ \end{matrix}\right. $$ 

and

 $$ \delta k_{0}^{p-1}(r_{j})=\left\{\begin{aligned}{}&{{}1-\sum_{i=1}^{p-1}r_{i}}&{(j=1)}\\ {}&{{}r_{j-1}}&{(1<j\leq p).}\\ \end{aligned}\right. $$ 

Applying (7) and (8) to the right-hand term of (3), we obtain

 $$ \begin{align*}\sum_{i=0}^{p}(-1)^{i}&\int_{\Delta^{p-1}}\delta k_{i}^{p-1}(a_{j} dr_{1}\wedge\cdots\wedge\widehat{dr}_{j}\wedge\cdots\wedge dr_{p})\\&=(-1)^{i-1}\int_{\Delta^{p-1}}a_{j}\bigg(1-\sum_{i=1}^{p-1}r_{i},r_{1},\ldots,r_{p-1}\bigg)dr_{1}\wedge\cdots\wedge dr_{p-1}\\&\quad+(-1)^{i}\int_{\Delta^{p-1}}a_{j}(r_{1},\ldots,r_{j-1},0,r_{j},\ldots,r_{p-1})dr_{1}\wedge\cdots\wedge dr_{p-1}.\end{align*} $$ 

We shall now apply a change of variables to the first term on the right-hand side of (9). Let  $ \varphi_{t} $ be the diffeomorphism of  $ R^{p-1} $ defined by

 $$ \varphi_{j}(r_{1},\ldots,r_{p-1})=\begin{cases}{(r_{1},\ldots,r_{p-1})}&{(j=1)}\\ {\left(1-\displaystyle\sum_{i=1}^{p-1}r_{i},r_{2},\ldots,r_{p-1}\right)}&{(j=2)}\\ {\left(r_{2},\ldots,r_{j-1},1-\displaystyle\sum_{i=1}^{p-1}r_{i},r_{j},\ldots,r_{p-1}\right)}&{}\\ {\quad(3\leq j\leq p).}\\ \end{cases} $$ 

Then  $ \varphi_j(\Delta^{s-1}) = \Delta^{s-1} $, and  $ |J\varphi_j| = 1 $, so that by 4.4(1), the first term on the right-hand side of (9) is equal to

 $$ (-1)^{i-1}\int_{\Delta^{p-1}}a_{j}\left(r_{1},\ldots,r_{j-1},1-\sum_{i=1}^{p-1}r_{i},r_{j},\ldots,r_{p-1}\right)d r_{1}\wedge\cdots\wedge d r_{p-1}. $$ 

From (3), (6), (9), and (11) we see that the proof has been reduced to showing that

 $$ \begin{aligned}{}&{{}\int_{\Delta^{p}}\frac{\partial a_{j}}{\partial r_{j}}d r_{1}\wedge\cdots\wedge d r_{p}}\\ {}&{{}\quad=\int_{\Delta^{p-1}}a_{j}\bigg(r_{1},\ldots,r_{j-1},1-\sum_{i=1}^{p-1}r_{i},r_{j},\ldots,r_{p-1}\bigg)d r_{1}\wedge\cdots\wedge d r_{p-1}}\\ {}&{{}\quad-\int_{\Delta^{p-1}}a_{j}(r_{1},\ldots,r_{j-1},0,r_{j},\ldots,r_{p-1})d r_{1}\wedge\cdots\wedge d r_{p-1}.}\\ \end{aligned} $$ 

But now (12) is simply the evaluation of the integral of $\partial a_{i}/\partial r_{i}$ over $\Delta^{p}$ by iterating first with respect to $r_{i}$ and applying again the Fundamental Theorem of Calculus.

4.8 Integration on an Oriented Manifold Let $M$ be an $n$-dimensional oriented manifold. We shall integrate $n$-forms over regular domains in $M$. A subset $D$ of $M$ will be called a regular domain if for each point $m \in M$ one of the following holds:

(a) There is an open neighborhood of m which is contained in M - D.

(b) There is an open neighborhood of m which is contained in D.

(c) There is a centered coordinate system $(U,\varphi)$ about $m$ such that $\varphi(U\cap D)=\varphi(U)\cap H^n$, where $H^n$ is the half-space of $\mathbb{R}^n$ defined by $r_n\geq0$.

Points of $D$ of type (b) are called interior points and comprise the interior, Int(D), of $D$. Points of type (c) are called boundary points and comprise the boundary, $\partial D$, of $D$. Coordinate systems of type (c) restricted to $\partial D$ overlap differentially and yield a manifold structure of dimension $n-1$ on $\partial D$, making $\partial D$ into an imbedded $(n-1)$ dimensional submanifold of $M$.

Let $m \in \partial D$, and let $v \in M_m$. We call $v$ an outer vector to $D$ if there is a smooth curve $\alpha(t)$ in $M$ with $\dot{\alpha}(0) = v$ and with $\alpha(t) \notin D$ for $0 < t < \varepsilon$, for some $\varepsilon > 0$. The orientation on $M$ induces an orientation on $\partial D$ as follows. Let $v$ be an outer vector to $\partial D$ at $m$, and let $v_1, \ldots, v_{n-1}$ be a basis of the tangent space $(\partial D)_m$. Then we define $v_1, \ldots, v_{n-1}$ to be an oriented basis of $(\partial D)_m$ if and only if $v, v_1, \ldots, v_{n-1}$ is an oriented basis of $M_m$. One can easily check that this definition is independent of the outer vector $v$ chosen, and that this defines a smooth orientation on $\partial D$ in the sense of 4.1.

Now let $\omega$ be an $n$-form ($n = \dim M$) with compact support, and let $D$ be a regular domain in $M$. As a particular case, $D$ could be all of $M$. We are going to define the integral of $\omega$ over $D$. As in 4.6, it will be sufficient for the purposes of this definition for $\omega$ to be a continuous $n$-form. We shall use a partition of unity to reduce the support of $\omega$ to certain $n$-simplices in $M$ over which we can integrate as in 4.6(9). First, we shall choose some $n$-simplices suitably related to $D$ and $\partial D$.

An $n$-simplex $\sigma$ in $M$ will be called regular if $\sigma$ extends to a diffeomorphism on a neighborhood of $\Delta^n$. When speaking of regular $n$-simplices, we shall always assume that they have been extended in this way to a neighborhood of $\Delta^n$. An oriented regular $n$-simplex is one in which the map $\sigma$ preserves orientations. (We always take the standard orientation on $\mathbb{R}^n$.)

Associated with a given regular domain $D$, we shall consider only oriented regular $n$-simplices of the following two types:

 $ (\alpha) $  $ \sigma(\Delta^n) \subset \operatorname{Int}(D) $.

 $ (\beta) $  $ \sigma(\Delta^n) \subset D $ and  $ \sigma(\Delta^n) \cap \partial D = \sigma^n (\Delta^{n-1}) $; that is, precisely the nth face of  $ \sigma $ lies in the boundary of  $ D $.

Now cover D by open sets U of the following types:

 $ (\alpha') \quad U $ lies in the interior of an oriented regular  $ n $-simplex  $ \sigma $ of type  $ (\alpha) $.

 $ (\beta') $ U is the image under a type  $ (\beta) $ oriented regular  $ n $-simplex  $ \sigma $ of an open set  $ V $ in  $ \mathbb{R}^n $ which is a neighborhood of a point in the  $ n $th face of  $ \Delta^* $, which intersects the boundary of  $ \Delta^* $ only in that  $ n $th face, and whose image under  $ \sigma $ is contained in  $ \sigma(\Delta^*) \cup (M - D) $.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//99b7a010-77a7-43c1-b445-62f9bbe330c7/markdown_2/imgs/img_in_image_box_158_107_769_388.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A15Z%2F-1%2F%2F497a564299c6cc0960c2e6e231d555e43f41b07c88d6616eb040f46531a1b1b3" alt="Image" width="64%" /></div>


Since supp $\omega \cap D$ is compact, it has a finite cover $U_1, \ldots, U_k$ by open sets of type $(\alpha')$ or $(\beta')$. Let the associated oriented regular $n$-simplices be $\sigma_1, \ldots, \sigma_k$. Let $U = M - (\text{supp} \omega \cap D)$, and let $\varphi, \varphi_1, \ldots, \varphi_k$ be a partition of unity subordinate to the cover $U, U_1, \ldots, U_k$ of $M$. We define the integral of $\omega$ over $D$ by

 $$ \int_{D}\omega=\sum_{i=1}^{k}\int_{\sigma_{i}}\varphi_{i}\omega. $$ 

We must check that the definition (1) is independent of the cover and the partition of unity chosen. Let $V, V_{1}, \ldots, V_{i}$ and $\psi, \psi_{1}, \ldots, \psi_{i}$ be another such cover and another such partition of unity respectively, with $V_{i}$ associated with the oriented regular $n$-simplex $\tau_{i}$. Since $\psi = 0$ on $\mathrm{supp} \omega \cap D$, it follows that $\sum_{j=1}^{i} \psi_{j} = 1$ there, so that

 $$ \sum_{i=1}^{k}\int_{\sigma_{i}}\varphi_{i}\omega=\sum_{i=1}^{k}\int_{\sigma_{i}}\sum_{j=1}^{l}\psi_{j}\varphi_{i}\omega=\sum_{i,j}\int_{\sigma_{i}}\psi_{j}\varphi_{i}\omega. $$ 

Similarly,

 $$ \sum_{j=1}^{i}\int_{\tau_{j}}\psi_{j}\omega=\sum_{i,j}\int_{\tau_{j}}\psi_{j}\varphi_{i}\omega. $$ 

Now, since $\sigma_i^{-1} \circ \tau_i$ is an orientation-preserving diffeomorphism on the open set (possibly empty) where it is defined, and since (supp $\psi_i \varphi_i \omega$) $\cap \sigma_i(\Delta^n) = (\text{supp } \psi_i \varphi_i \omega) \cap \tau_i(\Delta^n)$, it follows from the change of variables formula 4.5(2) that

 $$ \begin{aligned}{\int_{\sigma_{i}}\psi_{j}\varphi_{i}\omega=}&{{}\int_{\Delta^{n}}\delta\sigma_{i}(\psi_{j}\varphi_{i}\omega)=\int_{\Delta^{n}}\delta(\sigma_{i}^{-1}\circ\tau_{j})[\delta\sigma_{i}(\psi_{j}\varphi_{i}\omega)]}\\ {=}&{{}\int_{\Delta^{n}}\delta\tau_{j}(\psi_{j}\varphi_{i}\omega)=\int_{\tau_{j}}\psi_{j}\varphi_{i}\omega.}\\ \end{aligned} $$ 

It follows from (2), (3), and (4) that $\int_{D} \omega$ is well-defined, independent of the choice of cover and partition of unity.

Observe that if $\gamma$ is a diffeomorphism of $M$, then

 $$ \int_{\tau(D)}\omega=\pm\int_{D}\delta\gamma(\omega) $$ 

with “+” if and only if  $ \gamma $ is orientation-preserving.

We now are ready to state and prove our second version of Stokes' theorem.

4.9 Stokes' Theorem II Let $D$ be a regular domain in an oriented $n$-dimensional manifold $M$, and let $\omega$ be a smooth $(n-1)$ form of compact support. Then

 $$ \int_{D}d\omega=\int_{\partial D}\omega. $$ 

PROOF Let $\varphi_{1},\ldots,\varphi_{k}$ and $\sigma_{1},\ldots,\sigma_{k}$ be chosen as in 4.8(1) relative to (supp $\omega$) $\cap D$. Since $\sum_{i=1}^{k}\varphi_{i}=1$ on a neighborhood of (supp $\omega$) $\cap D$, $d(\sum\varphi_{i})=0$ there. Thus on a neighborhood of (supp $\omega$) $\cap D$ we have

 $$ \sum_{i=1}^{k}d(\varphi_{i}\omega)=\sum_{i=1}^{k}d\varphi_{i}\wedge\omega+\sum_{i=1}^{k}\varphi_{i}d\omega=d\omega. $$ 

Now, if  $ \sigma_{t} $ is an n-simplex of type 4.8( $ \alpha $), then

 $$ \int_{\partial\sigma_{i}}\varphi_{i}\omega=0=\int_{\partial D}\varphi_{i}\omega $$ 

since $\mathrm{supp} \ \varphi_i \omega \subset \mathrm{Int} \ \sigma_i(\Delta^n) \subset \mathrm{Int} \, D$. On the other hand, suppose that $\sigma_i$ is an $n$-simplex of type 4.8($\beta$). In this case, $\varphi_i \omega$ is zero on the boundary of $\sigma_i$ except possibly at points in the interior of the $n$th face $\sigma_i^n$. Now $\sigma_i^n$ is an orientation-preserving regular ($n-1$) simplex in $\partial D$ if $n$ is even, and is orientation-reversing if $n$ is odd. It follows that

 $$ \int_{\partial\sigma_{t}}\varphi_{t}\omega=(-1)^{n}\int_{\sigma_{t}}{}_{n}\varphi_{t}\omega=(-1)^{n}(-1)^{n}\int_{\partial D}\varphi_{t}\omega=\int_{\partial D}\varphi_{t}\omega. $$ 

From (2), (3), (4), and from our first version (4.7) of Stokes' theorem, we see that

 $$ \begin{aligned}{\int_{\mathcal{D}}d\omega}&{{}=\sum_{i}\int_{\mathcal{D}}d(\varphi_{i}\omega)=\sum_{i}\int_{\sigma_{i}}d(\varphi_{i}\omega)}\\ {}&{{}=\sum_{i}\int_{\mathfrak{s}\sigma_{i}}\varphi_{i}\omega=\sum_{i}\int_{\mathfrak{s}\mathcal{D}}\varphi_{i}\omega=\int_{\mathfrak{s}\mathcal{D}}\omega.}\\ \end{aligned} $$ 

Corollary Let $\omega$ be a smooth $(n-1)$ form on a compact oriented $n$-dimensional manifold $M$. Then

 $$ \int_{\mathcal{M}}d\omega=0. $$ 

4.10 Integration on a Riemannian Manifold Let $M$ be a Riemannian manifold of dimension $n$. That is, $M$ is an $n$-dimensional differentiable manifold with a positive definite inner product $\langle \ , \rangle_m$ on each tangent space $M_m$ such that $m \mapsto \langle X, Y \rangle_m$ is a smooth function on $M$ whenever $X$ and $Y$ are smooth vector fields. The existence of Riemannian metrics on differentiable manifolds was asserted in Exercise 23 of Chapter 1.

Given a point  $ m \in M $, one can find a neighborhood  $ U $ of  $ m $ and a collection  $ e_1, \ldots, e_n $ of  $ C^\infty $ vector fields on  $ U $ which are orthonormal in the sense that they form an orthonormal basis of the tangent space to  $ M $ at each point of  $ U $. Start with a coordinate neighborhood  $ (U, x_1, \ldots, x_n) $, apply the usual Gram-Schmidt procedure to orthonormalize the vector fields  $ \partial/\partial x_1, \ldots, \partial/\partial x_n $, and do it simultaneously at all points of  $ U $. Such a collection  $ e_1, \ldots, e_n $ is called a local orthonormal frame field.

Since the inner product  $ \langle \quad, \quad\rangle_{m} $ is, in particular, a non-singular pairing of  $ M_{m} $ with itself, it induces (see 2.7) a natural isomorphism of  $ M_{m} $ with  $ M_{m}^{*} $, namely,  $ v \mapsto \varphi_{v} $ where

 $$ \varphi_{v}(w)=\langle v,w\rangle_{m}. $$ 

Via this isomorphism,  $ M_{m}^{*} $ inherits an inner product. Observe that the dual basis to an orthonormal basis of  $ M_{m} $ is itself an orthonormal basis for  $ M_{m}^{*} $.

Now let  $ e_{1}, \ldots, e_{n} $ be a local orthonormal frame field on U, and let  $ \omega_{1}, \ldots, \omega_{n} $ be the dual 1-forms. That is,

 $$ \omega_{i}(e_{i})=\delta_{i j}\quad\mathrm{o n}~U. $$ 

Then $\omega_{1}, \ldots, \omega_{n}$ form a local orthonormal coframe field on $U$. Consider now two local orthonormal coframe fields $\omega_{1}, \ldots, \omega_{n}$ on $U$ and $\omega_{1}^{\prime}, \ldots, \omega_{n}^{\prime}$ on $U^{\prime}$. Then on $U \cap U^{\prime}$

 $$ \omega_{1}\wedge\cdot\cdot\cdot\wedge\omega_{n}=\operatorname*{d e t}(\sigma)\omega_{1}^{\prime}\wedge\cdot\cdot\cdot\wedge\omega_{n}^{\prime} $$ 

where  $ \sigma $ is an orthogonal matrix whose entries are  $ C^{\infty} $ functions on  $ U \cap U' $. Thus

 $$ \omega_{1}\wedge\cdots\wedge\omega_{n}=\pm\omega_{1}^{\prime}\wedge\cdots\wedge\omega_{n}^{\prime}. $$ 

Now assume that $M$ is oriented. A local coframe field $\omega_1, \ldots, \omega_n$ on $U$ will be called oriented if $\omega_1 \wedge \cdots \wedge \omega_n$ belongs to the orientation at each point of $U$. Choose a local oriented orthonormal coframe field about each point of $M$. Then the corresponding $n$-forms $\omega_1 \wedge \cdots \wedge \omega_n$ agree on overlaps, and therefore determine a globally defined nowhere-vanishing $n$-form $\omega$ on $M$. This form $\omega$ is called the volume form of the oriented Riemannian manifold $M$. Its integral over $M$ is the volume of $M$.

In Exercise 13 of Chapter 2, the star operator * was introduced on $\Lambda(V)$ for an oriented inner product space $V$. On an oriented Riemannian manifold $M$, we therefore have * defined on $\Lambda(M_{m}^{*})$ for each $m$. It is easy to see that * takes smooth forms to smooth forms, so we have a linear operator

 $$ *:E^{v}(M)\to E^{n-v}(M), $$ 

which, according to Exercise 13 of Chapter 2, satisfies

 $$ **=(-1)^{p(n-p)}. $$ 

We already know from 4.8 how to integrate $n$-forms over an oriented $n$-dimensional manifold. Now in the case of an oriented Riemannian manifold $M$, we define the integral over $M$ of a continuous function $f$ with compact support to be the integral of the (continuous) $n$-form $*f = f_\omega$. That is,

 $$ \int_{M}f=\int_{M}*f=\int_{M}f\omega. $$ 

Actually, the orientation was convenient but not necessary in the definition of $\int_{M} f$. If $M$ is a (not necessarily oriented) Riemannian manifold, we define the integral of continuous functions with compact support as follows. Let $\{U_e\}$ be a cover of $M$ by interiors of regular $n$-simplices $\sigma_e$, and let $\omega_1^e, \ldots, \omega_n^e$ be a local orthonormal coframe field defined on a neighborhood of $\sigma_e(\Delta^n)$. Then there exist $C^\infty$ functions $h_e$ on neighborhoods of $\Delta^n$ such that

 $$ \delta\sigma_{a}(\omega_{1}{}^{a}\wedge\cdot\cdot\cdot\wedge\omega_{n}{}^{a})=h_{a}d r_{1}\wedge\cdot\cdot\cdot\wedge d r_{n}. $$ 

Let $\{\varphi_{e}\}$ be a partition of unity subordinate to the cover $\{U_{e}\}$, and let $f$ be a continuous function with compact support on $M$. Then we define

 $$ \int_{\mathcal{M}}f=\sum_{\alpha}\int_{\Delta^{n}}(\varphi_{\alpha}f)\circ\sigma_{\alpha}\left|h_{\alpha}\right|d r_{1}\wedge\cdots\wedge d r_{n}. $$ 

That this definition is independent of the cover and partition of unity chosen follows from an argument similar to the one at the end of 4.8. In the case of an oriented Riemannian manifold, (8) and (7) agree.

In classical vector analysis the gradient of a function $f$ on $\mathbb{R}^n$ is defined to be the vector field $\sum_{i=1}^{n}(\partial f/\partial r_i)\partial/\partial r_i$, and the divergence of a vector field $V=\sum_{i=1}^{n}v_i\,\partial/\partial r_i$ is defined to be the function $\sum_{i=1}^{n}\partial v_i/\partial r_i$. We extend these notions to general Riemannian manifolds as follows. Recall that the metric gives us canonical isomorphisms $M_m\cong M_m^*$. We shall for convenience denote such isomorphisms by a tilde, so that if $v\in M_m$, then $\tilde{v}$ will be the corresponding dual element in $M_m^*$; and if $\omega\in M_m^*$, then $\tilde{\omega}$ will be the corresponding vector in $M_m$. Then if $f$ is a function on $M$, its gradient is the vector field

 $$ \mathrm{grad}f=\widetilde{df}. $$ 

If V is a vector field on an oriented Riemannian manifold, then its divergence is the function

 $$ \mathrm{d i v}~\boldsymbol{V}=\ast d\ast\tilde{\boldsymbol{V}}. $$ 

Stokes' theorem has an equivalent version on oriented Riemannian manifolds known as the divergence theorem. This theorem says that if $V$ is a smooth vector field on an oriented Riemannian manifold $M$, if $D$ is a regular domain in $M$, and if $\vec{n}$ is the unit outer normal vector field on $\partial D$, then

 $$ \int_{D}\mathsf{d i v}V=\int_{\partial D}\langle V,\vec{n}\rangle. $$ 

The proof is left to the reader as an exercise. (For a few additional remarks see Exercise 4.)

4.11 Integration on a Lie Group Let G be an n-dimensional Lie group. We observed in 4.3(a) that G is orientable. We now fix once and for all an orientation on G.

Consider the left invariant $n$-forms on $G$. Since such a form is uniquely determined by its value at one point, and since the $n$th exterior power of an $n$-dimensional vector space is one-dimensional, there is exactly a one-dimensional space of left invariant $n$-forms on $G$. Choose a non-zero left invariant $n$-form $\omega$ consistent with the fixed orientation on $G$.

Since $G$ is oriented, the integral of compactly supported $n$-forms is defined on $G$ as in 4.8. We now define, with respect to $\omega$, the integral of a compactly supported continuous function $f$ on $G$ by setting

 $$ \int_{G}f=\int_{G}f\omega. $$ 

The integral (1) depends, of course, on the choice of the non-zero left invariant n-form  $ \omega $ consistent with the orientation on G. But since such forms are uniquely determined up to a positive constant multiple, so is the integral (1). In the case of a compact group G, we can and always will fix the choice of  $ \omega $ by requiring the normalization

 $$ \int_{G}\omega=1. $$ 

Consider the diffeomorphism  $ I_{\sigma} $, which is left translation by the element  $ \sigma $ of G. Then since  $ \delta I_{\sigma}(\omega) = \omega $,  $ I_{\sigma} $ is orientation-preserving, so that, according to 4.8(5),

 $$ \int_{G}f=\int_{G}f\omega=\int_{G}\delta l_{\sigma}(f\omega)=\int_{G}(f\circ l_{\sigma}^{\dot{i}})\omega=\int_{G}f\circ l_{\sigma}. $$ 

In view of property (3)—that the integral of a function $f$ on $G$ is the same as the integral of any of its left translates $f\circ l_\sigma$—we call the integral (1) left invariant.

Now we ask to what extent the integral (1) is also right invariant. That is, when do we have

 $$ \int_{G}f=\int_{G}f\circ r_{e} $$ 

for each $\sigma \in G$? The form $\delta r_{\sigma}\omega$ is still left invariant, since

 $$ \delta l_{\tau}\delta r_{\sigma}\omega=\delta r_{\sigma}\delta l_{\tau}\omega=\delta r_{\sigma}\omega. $$ 

Thus $\delta r_{a}\omega$ is some constant multiple of $\omega$. Thus there is defined a function $\bar{\lambda}$ of $G$ into the non-zero real numbers such that

 $$ \delta r_{\sigma}(\omega)=\tilde{\lambda}(\sigma)\omega. $$ 

It is easily checked that  $ \bar{\lambda} $ is  $ C^{\infty} $. We let

 $$ \lambda(\sigma)=|\tilde{\lambda}(\sigma)|. $$ 

Observe that

 $$ \lambda(\sigma\tau)=\lambda(\sigma)\lambda(\tau), $$ 

so that $\lambda$ is a Lie group homomorphism of $G$ into the multiplicative group of positive real numbers. $\lambda$ is called the modular function. Now since, by 4.8(5), for each $\sigma$ in $G$

 $$ \int_{G}f\omega=\int_{G}(f\circ r_{e})\lambda(\sigma)\omega, $$ 

it follows that the integral (1) is right invariant if and only if $\lambda \equiv 1$ on $G$. A Lie group $G$ for which $\lambda \equiv 1$ is called unimodular. We observe that each compact Lie group $G$ is unimodular since for each $\sigma \in G$

 $$ 1=\int_{\mathcal{G}}\omega=\lambda(\sigma)\int_{\mathcal{G}}\omega=\lambda(\sigma). $$ 

Thus the integral on a compact Lie group is both left and right invariant.

4.12 Application of 4.11 A typical application of the integral on a compact Lie group is the following.

Let $G$ be a Lie group, and let $\alpha: G \to \text{Aut}(V)$ be a representation into the automorphisms of a real or complex inner product space $V$. The representation $\alpha$ is called unitary (respectively orthogonal) in the case in which $V$ is a complex (respectively real) inner product space if

 $$ \langle\alpha(\tau)v,\alpha(\tau)w\rangle=\langle v,w\rangle $$ 

for all v and w in V and for all  $ \tau \in G $.

Let $G$ be compact and $V$ complex (respectively real). Then there is an inner product on $V$ with respect to which $\alpha$ is unitary (respectively orthogonal). The proofs in the real case and in the complex cases are similar. Let {, } be any inner product on $V$. We set

 $$ \langle v,w\rangle=\int_{G}\{\alpha(\sigma)v,\alpha(\sigma)w\}d\sigma, $$ 

where we use $d\sigma$ to denote that we are considering the integrand as a function of $\sigma$ in $G$. It is immediate that $\langle\quad,\quad\rangle$ is again an inner product. That (1) holds follows from the right invariance of the integral on $G$:

 $$ \begin{align*}\langle\alpha(\tau)v,\alpha(\tau)w\rangle=&\int_{G}\left\{\alpha(\sigma)\alpha(\tau)v,\alpha(\sigma)\alpha(\tau)w\right\}d\sigma\\=&\int_{G}\left\{\alpha(\sigma\tau)v,\alpha(\sigma\tau)w\right\}d\sigma=\int_{G}\left\{\alpha(\sigma)v,\alpha(\sigma)w\right\}d\sigma=\langle v,w\rangle.\end{align*} $$ 

##### DE RHAM COHOMOLOGY

4.13 Definition A p-form $\alpha$ on a differentiable manifold $M$ is called closed if $d\alpha = 0$. It is called exact if there is a $(p - 1)$ form $\beta$ such that $\alpha = d\beta$. Since $d^{2} = 0$, every exact form is closed. The quotient space of the real vector space of closed $p$-forms modulo the subspace of exact $p$-forms is called the $p$th $de$ $Rham$ cohomology group of $M$.

 $$ H_{\tt d e r}^{v}(M)=\{\mathrm{c l o s e d~}p\mathrm{-f o r m s}\}/\{\mathrm{e x a c t~}p\mathrm{-f o r m s}\}. $$ 

4.14 Example Consider the case of the unit circle  $ S^1 $. Since there are no non-zero p-forms on  $ S^1 $ for  $ p > 1 $, all of the cohomology groups  $ H_{\mathfrak{d}, \mathbf{B}}^p(S^1) $ are zero except possibly for  $ p = 0, 1 $. There are no exact 0-forms, and a closed 0-form on a connected manifold is simply a constant function, so

 $$ H_{\mathtt{d e R}}^{0}(S^{1})\cong\mathbb{R}. $$ 

The “polar coordinate function” $\theta$ on $S^1$ is not well-defined globally since it is defined only up to integral multiples of $2\pi$. However, its differential $d\theta$ is a globally well-defined nowhere-vanishing 1-form on $S^1$. In fact, $d\theta$ is the volume form of the natural Riemannian metric which $S^1$ inherits from $\mathbb{R}^2$. Now, $d\theta$ is not exact, for if it were, its integral over $S^1$ would have to be 0 rather than $2\pi$. All 1-forms on $S^1$ are closed. We claim that if $\alpha$ is a 1-form, then there is a constant $c$ such that $\alpha - c\,d\theta$ is exact. For let $\alpha = f(\theta)\,d\theta$, let

 $$ c=\frac{1}{2\pi}\int_{S^{1}}\alpha, $$ 

and let

 $$ g(\theta)=\int_{0}^{\theta}\left(f(\theta)-c\right)d\theta. $$ 

Since  $ g(\theta + 2\pi n) = g(\theta) $ for every integer n, then g is a well-defined  $ C^\infty $ function on  $ S^1 $; and  $ dg = (f(\theta) - c) d\theta = \alpha - c d\theta $. Thus every 1-form on  $ S^1 $ differs from a real multiple of  $ d\theta $ by an exact form. Consequently,

 $$ H_{\mathbf{d e}{\mathbb{R}}}^{1}(S^{1})\cong\mathbb{R}. $$ 

4.15 Effect of Mappings Let $f: M \to N$ be a $C^\infty$ map. Then the algebra homomorphism $\delta f: E^*(N) \to E^*(M)$ commutes with $d$, according to 2.23, and hence maps closed forms to closed forms and exact forms to exact forms. Thus it induces a homomorphism

 $$ f^{*}\colon H_{\tt d e r}^{\circ}(N)\to H_{\tt d e r}^{\circ}(M) $$ 

for each integer  $ p \geq 0 $. If, in addition,  $ g: N \to X $ is  $ C^\infty $, then

 $$ (g\circ f)^{*}=f^{*}\circ g^{*}. $$ 

Clearly the identity map id: $M \to M$ induces the identity on de Rham cohomology:

 $$ (id)^{*}=id. $$ 

It follows from (2) and (3) that a diffeomorphism $f\colon M\to N$ induces isomorphism on de Rham cohomology. Thus the de Rham cohomology is a differentiable invariant of a differentiable manifold $M$. We shall prove in Chapter 5 that it is actually a topological invariant. That is, the de Rham cohomology groups depend only on the underlying topological structure of $M$ and do not depend on the differentiable structure. A key part in the proof of this fact is the de Rham theorem, a version of which we shall formulate now. First, we need to define the real differentiable singular homology groups of $M$.

4.16 Real Differentiable Singular Homology For each integer $p \geq 0$ we let $\infty S_p(M,\mathbb{R})$ denote the real vector space generated by the differentiable singular $p$-simplices in $M$. Hence the elements of $\infty S_p(M,\mathbb{R})$ are precisely the differentiable singular $p$-chains in $M$ with real coefficients. For $p < 0$, we let $\infty S_p(M,\mathbb{R})$ be the zero vector space. The boundary operator $\partial$ induces linear transformations

 $$ \partial_{p}\colon\infty S_{p}(M,\mathbb{R})\to\infty S_{p-1}(M,\mathbb{R}) $$ 

for each integer $p$, which for $p \leq 0$ are simply the zero transformation. According to 4.6(7), $\partial_{p} \circ \partial_{p+1} = 0$, so that the image of $\partial_{p+1}$ lies in the kernel of $\partial_{p}$. The $p$th differential singular homology group of $M$ with real coefficients is defined by

 $$ \scriptstyle{H_{p}(M;\mathbb{R})=\ker\partial_{p}/\mathrm{I m}\partial_{p+1},} $$ 

and is moreover a real vector space. Elements of $\mathbf{ker} \partial_{p}$ are called differentiable $p$-cycles, and elements of $\mathrm{Im} \partial_{p+1}$ are called differentiable $p$-boundaries.

4.17 The de Rham Theorem We shall define a linear mapping of the de Rham cohomology  $ H_{\mathrm{deR}}^{p}(M) $ into the dual space  $ \infty H_{p}(M;\mathbb{R})^{*} $ of the real differentiable singular homology:

 $$ H_{\mathbf{d e}\mathbb{R}}^{\mathfrak{p}}(M)\to{}_{\infty}H_{\mathfrak{p}}(M;\mathbb{R})^{*}. $$ 

Let $\alpha$ be a closed $p$-form representing the de Rham cohomology class $\{\alpha\}$, and let $z$ be a $p$-cycle representing the real differentiable singular homology class $\{z\}$. Then (1) is defined by

 $$ \{\alpha\}(\{z\})=\int_{z}\alpha. $$ 

That (2) is independent of the representatives  $ \alpha $ and z chosen follows immediately from Stokes' theorem I (4.7).

The de Rham theorem asserts that (1) is an isomorphism. This will be proved in 5.36 and 5.37. The real numbers determined by the integrals of a differential form over differentiable cycles are called the periods of the differential form. Now, Stokes' theorem I says that the periods of an exact form are all zero. The injectiveness of the isomorphism (1) gives a converse, namely, if a closed form has all of its periods zero, then it is an exact form. The surjectivity of (1) says that if a real number per(z) is assigned to each cycle z in such a way that

 $$ \operatorname{p e r}(a z_{1}+z_{2})=a\operatorname{p e r}(z_{1})+\operatorname{p e r}(z_{2}),\quad\operatorname{p e r}(\operatorname{b o u n d a r y})=0, $$ 

then there is a closed form  $ \alpha $ on M such that for all cycles z

 $$ \int_{z}\alpha=\operatorname{p e r}(z). $$ 

A key ingredient in the proof of the de Rham theorem (see 5.28) is the

4.18 Poincaré Lemma Let U be the open unit ball in Euclidean space  $ \mathbb{R}^n $, and let  $ E^k(U) $, as usual, be the space of differential k-forms on U. Then for each  $ k \geq 1 $ there is a linear transformation  $ h_k: E^k(U) \to E^{k-1}(U) $ such that

 $$ h_{k+1}\circ d+d\circ h_{k}=\operatorname{i d}. $$ 

PROOF We begin with formula 2.25(d), which expresses the Lie derivative in terms of exterior differentiation and interior multiplication:

 $$ L_{x}=i(X)\circ d+d\circ i(X). $$ 

We shall apply (2) to the radial vector field

 $$ X=\sum_{i=1}^{n}r_{i}\frac{\partial}{\partial r_{i}} $$ 

on $U$. We define a linear operator $\alpha_{k}$ on $E^{k}(U)$ by setting

 $$ \alpha_{k}(\overset{\underset{\cdot}{f}}{\underset{\cdot}{d}}r_{i_{1}}\wedge\cdots\wedge\overset{\underset{\cdot}{d}}{d}r_{i_{k}})(p)=\left(\int_{0}^{1}t^{k-1}f(t p)\;d t\right)\;d r_{i_{1}}\wedge\cdots\wedge d r_{i_{k}}(p) $$ 

and extending linearly to all of  $ E^{k}(U) $. Now with X defined by (3), we show that

 $$ \alpha_{k}\circ L_{X}=\operatorname{id}\quad\operatorname{on}\quad E^{k}(U). $$ 

For, using the fact that $L_{x}$ is a derivation which commutes with $d$, we have

(6)

 $$ \begin{aligned}{\alpha_{k}\circ L_{\overline{{x}}}(f}&{{}d r_{\varepsilon_{1}}\wedge\cdots\wedge d r_{\varepsilon_{k}})(p)}\\ {}&{{}=\alpha_{k}\bigg\{\left(k f+\sum r_{\varepsilon}\frac{\partial f}{\partial r_{\varepsilon}}\right)d r_{\varepsilon_{1}}\wedge\cdots\wedge d r_{\varepsilon_{k}}\bigg\}(p)}\\ {}&{{}=\left(\int_{0}^{1}t^{k-1}\bigg(k f(t p)+\sum r_{\varepsilon}(t p)\frac{\partial f}{\partial r_{\varepsilon}}\bigg|_{t p}\right)d t\bigg)d r_{\varepsilon_{1}}\wedge\cdots\wedge d r_{\varepsilon_{k}}(p)}\\ {}&{{}=\left(\int_{0}^{1}\frac{d}{d t}\left(t^{k}f(t p)\right)d t\right)d r_{\varepsilon_{1}}\wedge\cdots\wedge d r_{\varepsilon_{k}}(p)}\\ {}&{{}=f(p)d r_{\varepsilon_{1}}\wedge\cdots\wedge d r_{\varepsilon_{k}}(p).}\\ \end{aligned} $$ 

From (5) and (2) we obtain

 $$ \mathrm{i d}=\alpha_{k}\circ i(X)\circ d+\alpha_{k}\circ d\circ i(X) $$ 

on  $ E^{k}(U) $ with X given by (3). Now  $ \alpha $ commutes with  $ d $; that is,

(8)

 $$ \alpha_{k}\circ d=d\circ\alpha_{b-1}. $$ 

For

 $$ \begin{aligned}{\alpha_{k}\circ d(f d r_{\ell_{1}}\wedge\cdots\wedge d r_{\ell_{k-1}})(p)}\\ {=}&{{}\alpha_{k}\bigg(\sum\frac{\partial f}{\partial r_{\ell_{i}}}d r_{\ell_{i}}\wedge d r_{\ell_{1}}\wedge\cdots\wedge d r_{\ell_{k-1}}\bigg)(p)}\\ {=}&{{}\left(\int_{0}^{1}t^{k-1}\sum\frac{\partial f}{\partial r_{\ell_{i}}}\bigg|_{t p}d t\right)d r_{\ell_{i}}\wedge d r_{\ell_{1}}\wedge\cdots\wedge d r_{\ell_{k-1}}(p)}\\ {=}&{{}d\left(\int_{0}^{1}t^{k-2}f(t p)d t\right)d r_{\ell_{1}}\wedge\cdots\wedge d r_{\ell_{k-1}}(p)}\\ {=}&{{}d\circ\alpha_{k-1}(f d r_{\ell_{1}}\wedge\cdots\wedge d r_{\ell_{k-1}})(p).}\\ \end{aligned} $$ 

Thus from (8) and (7) we obtain

(9)

 $$ \mathrm{i d}=\alpha_{k}\circ i(X)\circ d+d\circ\alpha_{k-1}\circ i(X) $$ 

on  $ E^{k}(U) $. Thus the desired linear transformation  $ h_{k} $ which yields (1) is obtained by setting

(10)

 $$ h_{k}=\alpha_{k-1}\circ i\left(\sum r_{i}\frac{\partial}{\partial r_{i}}\right). $$ 

Corollary (a) If $\omega$ is a $k$-form, $k \geq 1$, on the open unit ball in $\mathbb{R}^n$ and $d\omega = 0$, then there exists $a$ ($k - 1$) form $\beta$ (namely $h_k(\omega)$) such that $d\beta = \omega$.

Corollary (b) The de Rham cohomology groups of the open unit ball in  $ \mathbb{R}^n $ are all zero for  $ p \geq 1 $.

4.19 Remark Let $f_{1}$ and $f_{2}$ be $C^{\infty}$ maps of $M$ into $N$. Then we have induced maps

 $$ \delta f_{i}\colon E^{k}(N)\to E^{k}(M)\quad\mathrm{f o r~e a c h~}k. $$ 

If we wish to prove that $\delta f_{1}$ and $\delta f_{2}$ both induce the same homomorphism on de Rham cohomology, then we need only find a collection of linear transformations

 $$ h_{k}\colon E^{k}(N)\to E^{k-1}(M) $$ 

such that

 $$ h_{k+1}\circ d+d\circ h_{k}=\delta f_{1}-\delta f_{2}. $$ 

For then, if $\alpha$ is a closed form on $N$, $\delta f_{1}(\alpha)$ and $\delta f_{2}(\alpha)$ differ by an exact form, and thus lie in the same cohomology class. Such a collection of linear transformations $\{h_{k}\}$ is called a homotopy operator for $f_{1}$ and $f_{2}$. In the Poincaré lemma we found a homotopy operator between the identity map of the open unit ball $U$ and any constant map (range 1 point) of $U$ into itself.

##### EXERCISES

1 Prove the assertion of 4.3(c) that a $d$-dimensional manifold $X$ for which there exists an immersion $f: X \to \mathbb{R}^{d+1}$ is orientable if and only if there is a smooth nowhere-vanishing normal vector field along $(X,f)$.

2 Prove that the real projective space $P^{n}$ is orientable if and only if $n$ is odd. (Hint: Observe that the antipodal map on the $n$-sphere $S^{n}$ is orientation-preserving if and only if $n$ is odd.)

3 Carry out in detail the proof of the existence of local orthonormal frame fields on a Riemannian manifold.

4 Prove the divergence theorem 4.10(11). This follows from Stokes' theorem together with the identity

 $$ \int_{\partial D}\ast\widetilde{V}=\int_{\partial D}\langle V,\vec{n}\rangle. $$ 

The easiest way to see (1) is to choose a local oriented orthonormal frame field  $ e_1, \ldots, e_n $ on a neighborhood of a point of  $ \partial D $, such that at points of  $ \partial D $,  $ e_1 $ is the outer unit normal vector and  $ e_2, \ldots, e_n $ form an oriented basis of the tangent space to  $ \partial D $. Then express  $ *\tilde{V} $ and  $ \langle V,\tilde{n} \rangle $ in terms of this local frame field and its dual coframe field  $ \omega_1, \ldots, \omega_n $.

5 Let $M$ be an oriented Riemannian manifold, let $f$ and $g$ be $C^{\infty}$ functions on $M$, and let $D$ be a regular domain in $M$. The Laplacian of $g$, denoted $\Delta g$, is defined by

 $$ \Delta g=-*d*d g. $$ 

(For more on the Laplacian, see Chapter 6. Observe that our choice of sign for the Laplacian yields $\Delta g = -\sum_{i=1}^{n} \partial^{2} g/\partial r_{i}^{2}$ for $g$ a $C^{\infty}$ function on Euclidean space $\mathbb{R}^{n}$ with its standard Riemannian structure in which $\{\partial/\partial r_{i}\}$ is an orthonormal basis of each tangent space.) If $\bar{n}$ is the unit outer normal vector field along $\partial D$, we let $\partial g/\partial n$ denote $\bar{n}(g)$. Prove the following two Green's identities:

Green's 1st:

 $$ \int_{\partial D}f\frac{\partial g}{\partial n}=\int_{D}\langle\mathrm{g r a d}f,\mathrm{g r a d}g\rangle-\int_{D}f\Delta g. $$ 

Green's 2nd:  $ \int_{\partial D}\left(f\frac{\partial g}{\partial n}-g\frac{\partial f}{\partial n}\right)=\int_{D}(g\Delta f-f\Delta g). $

6 Let $\omega$ be the volume form of an oriented Riemannian manifold of dimension $n$. Let $X_{1},\ldots,X_{n}$ and $Y_{1},\ldots,Y_{n}$ be vector fields on $M$. Prove that

 $$ \omega(X_{1},\ldots,X_{n})\cdot\omega(Y_{1},\ldots,Y_{n})=\operatorname*{d e t}\{\langle X_{i},Y_{j}\rangle\}. $$ 

Prove also that

 $$ \omega(X_{1},\ldots,X_{n})\omega=\widetilde{X}_{1}\wedge\cdots\wedge\widetilde{X}_{n}, $$ 

where  $ \tilde{X}_{i} $ is the 1-form dual (via the Riemannian structure) to the vector field  $ X_{i} $.

7 Prove the differentiability of the function  $ \bar{\lambda} $ of 4.11(5).

8 Let $G$ be a compact (oriented) Lie group, and let $\alpha(\sigma) = \sigma^{-1}$ for $\sigma \in G$. Prove that for every continuous function $f$ on $G$

 $$ \int_{a}f=\int_{a}f\circ\alpha. $$ 

9 Prove that a Lie group $G$ has a bi-invariant Riemannian metric (that is, a metric such that both $dl_\sigma$ and $dr_\sigma$ preserve the inner products for each $\sigma\in G$) if and only if the closure of $\mathrm{Ad}(G)$ in $\mathrm{Aut}(g)$ is compact.

10 (a) Prove that  $ H_{\mathrm{de}\,\,\mathrm{R}}^{p}(\mathbb{R}^{n})=0 $ for each  $ p \geq 1 $ and each  $ n \geq 1 $.

(b) Prove that  $ H_{\mathrm{de}\, \mathbb{R}}^{0}(M) \cong \mathbb{R} $ for a connected manifold  $ M $.

11 Determine the de Rham cohomology of the annular region

 $$ 1<(r_{1}{}^{2}+r_{2}{}^{2})^{1/2}<2\mathrm{i n}\mathbb{R}^{2}. $$ 

12 If  $ \alpha $ and  $ \beta $ are closed differential forms, prove that  $ \alpha \wedge \beta $ is closed. If, in addition,  $ \beta $ is exact, prove that  $ \alpha \wedge \beta $ is exact.

13 Consider the 1-form  $ \alpha = (x^2 + 7y)\,dx + (-x + y\sin y^2)\,dy $ on  $ \mathbb{R}^2 $. Compute its integral over the following 1-cycle z.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//d0650512-3bcc-42bc-8454-7b336b54e101/markdown_2/imgs/img_in_image_box_404_245_599_433.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A14Z%2F-1%2F%2Fb3803fed4e4aff44b96b655651dc2311fe45d43aa5df8661eef460208cb516f9" alt="Image" width="20%" /></div>


14 Let  $ \alpha = (2x + y \cos xy)dx + (x \cos xy)dy $ on  $ \mathbb{R}^2 $. Show that  $ \alpha $ is closed. Show that  $ \alpha $ is exact by finding a function  $ f $:  $ \mathbb{R}^2 \to \mathbb{R} $ with  $ \alpha = df $. What would the integral of  $ \alpha $ over the cycle of Exercise 13 be?

15 Let

 $$ \alpha=\frac{1}{2\pi}\frac{x\,dy-y\,dx}{x^{2}+y^{2}}. $$ 

Prove that $\alpha$ is a closed 1-form on $\mathbb{R}^8 - \{0\}$. Compute the integral of $\alpha$ over the unit circle $S^1$. How does this result show that $\alpha$ is not exact? How does this show that $\delta i(\alpha)$ is not exact, where $i: S^1 \to \mathbb{R}^8$ is the canonical imbedding?

16 (a) Prove that every closed 1-form on  $ S^{2} $ is exact.

(b) Let

 $$ \sigma=\frac{r_{1}\,d r_{2}\wedge d r_{3}-r_{2}\,d r_{1}\wedge d r_{3}+r_{3}\,d r_{1}\wedge d r_{2}}{(r_{1}^{2}+r_{2}^{2}+r_{3}^{2})^{3/2}} $$ 

in  $ \mathbb{R}^{3} - \{0\} $. Prove that  $ \sigma $ is closed.

(c) Evaluate  $ \int_{S^{2}}\sigma $. How does this show that  $ \sigma $ is not exact?

(d) Let

 $$ \alpha=\frac{r_{1}d r_{1}+r_{2}d r_{2}+\cdots+r_{n}d r_{n}}{(r^{2}+r_{2}^{2}+\cdots+r_{n}^{2})^{n/2}} $$ 

in  $ \mathbb{R}^n - \{0\} $. Find  $ *\alpha $, and prove that  $ *\alpha $ is closed.

(e) Evaluate  $ \int_{S^{n-1}} \ast \alpha $. Is  $ \ast \alpha $ exact?

17 Using de Rham cohomology, prove that the torus $T^{2}$ is not diffeomorphic with the 2-sphere $S^{2}$.

18 (a) Prove that every closed 1-form in the open shell

 $$ 1<\left(\sum_{i=1}^{3}r_{i}^{2}\right)^{1/3}<2 $$ 

in  $ R^{*} $ is exact.

(b) Find a 2-form in the above shell that is closed but not exact.

(c) Prove that the above shell is not diffeomorphic with the open unit ball in  $ \mathbb{R}^{3} $.

19 Let $f$ and $g$ be $C^\infty$ maps of $M$ into $N$ which are $C^\infty$ homotopic; that is, there exists a $C^\infty$ map $F$ of $M \times(-\varepsilon,1+\varepsilon)$ into $N$, for some $\varepsilon>0$, such that $F(m,0)=f(m)$ and $F(m,1)=g(m)$ for every $m\in M$. Prove that the induced homomorphisms $f^*$ and $g^*$ of $H_{\mathrm{de}}_{\mathrm{R}}(N)$ into $H_{\mathrm{de}}_{\mathrm{R}}(M)$ are equal for each integer $p$. (Hint: You will need to prove that the two injections $i_{\mathrm{e}}(m)=(m,0)$ and $i_{1}(m)=(m,1)$ of $M$ into $M\times(-\varepsilon,1+\varepsilon)$ induce the same homomorphisms on de Rham cohomology. To prove this, find suitable homotopy operators. The outline of the proof of the Poincaré lemma 4.18 should be helpful.)

20 (a) Let $f: M^n \to \mathbb{R}^{n+1}$ be an immersion, and let $M^n$ be given the induced Riemannian structure; that is, for $m \in M$ and $u, v \in M_m$,

 $$ \langle u,v\rangle_{m}=\langle d f(u),d f(v)\rangle_{f(m)}. $$ 

Suppose that $M$ is oriented, and that $\vec{n}$ is the oriented unit normal field along $f(M^n)$. (This means that $\vec{n}, df(v_1), \ldots, df(v_n)$ is to be an oriented orthonormal basis of the tangent space to Euclidean space at $f(m)$ whenever $v_1, \ldots, v_n$ is an oriented orthonormal basis of $M_m$.) Show that the volume form on $M$ is given by

 $$ \begin{array}{r}{\omega=\delta f\big(i(\vec{n})(d r_{1}\wedge\cdot\cdot\cdot\wedge d r_{n+1})\big).}\end{array} $$ 

(b) Let $D$ be an open set in the xy plane, and let $\varphi: D \to \mathbb{R}^3$ be a smooth map of the form

 $$ \varphi(x,y)=\bigl(x,y,f(x,y)\bigr). $$ 

Thus $\varphi$ determines an imbedded surface in $\mathbb{R}^{3}$. Give $D$ and $\mathbb{R}^{3}$ the standard orientations. Use part (a) to prove that the induced volume form on $D$ is given by

 $$ \omega=\left(\sqrt{\left(\frac{\partial f}{\partial x}\right)^{2}+\left(\frac{\partial f}{\partial y}\right)^{2}+1}\right)\,dx\wedge dy. $$ 

SHEAVES,

COHOMOLOGY,

and the DE RHAM THEOREM

The principal objective in this chapter is a proof of the de Rham theorem, one version of which we have stated in 4.17. In its most complete form it asserts that the homomorphism from the de Rham cohomology ring to the differentiable singular cohomology ring given by integration of closed forms over differentiable singular cycles is a ring isomorphism. The approach will be to exhibit both the de Rham cohomology and the differentiable singular cohomology as special cases of sheaf cohomology and to use a basic uniqueness theorem for homomorphisms of sheaf cohomology theories to prove that the natural homomorphism between the de Rham and differentiable singular theories is an isomorphism. As an added dividend of this approach we shall also obtain the existence of canonical isomorphisms of the de Rham and differentiable singular cohomology theories with the continuous singular theory, the Alexander-Spanier theory, and the Czech cohomology theory for differentiable manifolds. From these isomorphisms we shall conclude that the de Rham cohomology theory is a topological invariant of a differentiable manifold.

No previous knowledge of sheaf theory nor of any of these cohomology theories is assumed. We shall develop those aspects of the theories necessary for our applications. We begin with an introduction to the theory of sheaves and sheaf cohomology. Our approach is based largely on the development given by Cartan in [4]. The interested reader will find more general treatments of sheaf theory in Cartan [4], Godement [7], and Bredon [3]. Sheaves are a very powerful tool in the study of complex manifolds. For an excellent account of their use in the theory of Riemann surfaces, see Gunning [8].

Let M be a differentiable manifold. Recall that M is assumed to be second countable and is therefore paracompact. It should be pointed out that nearly all of the sheaf theory presented in this chapter depends only on M being a paracompact Hausdorff space. The differentiable structure on M will be invoked only in a few examples and in the discussions of the Rham cohomology (5.28) and the differentiable singular cohomology (5.31); and, in addition, the locally Euclidean structure will be invoked in the discussion of the singular cohomology (5.31). Otherwise, M need only be a paracompact Hausdorff space.

Throughout this chapter, K will be a fixed principal ideal domain. We shall treat sheaves of K-modules over M. The most important cases to keep in mind are these:

(i) K is the ring of integers Z, whence a K-module is simply an abelian group.

(ii) K is the field of real numbers  $ \mathbb{R} $, whence a K-module is simply a real vector space.

For the first few sections of this chapter, K could be any ring. The additional property that K is a principal ideal domain will be used first in 5.13.

##### SHEAVES AND PRESHEAVES

5.1 Definitions A sheaf S of K-modules over M consists of a topological space S together with a map  $ \pi\colon S \to M $ satisfying:

(a)  $ \pi $ is a local homeomorphism of S onto  $ M $.

(b)  $ \pi^{-1}(m) $ is a K-module for each  $ m \in M $.

(c) The composition laws are continuous in the topology on S.

We elaborate on (c). Let $\mathcal{S}\circ\mathcal{S}$ be the subspace of $\mathcal{S}\times\mathcal{S}$ consisting of all pairs $(s_1,s_2)$ such that $\pi(s_1)=\pi(s_2)$. Then (c) requires that the map $(s_1,s_2)\mapsto s_1-s_2$ of $\mathcal{S}\circ\mathcal{S}\to\mathcal{S}$ be continuous, and that each of the maps $s\mapsto k s$ of $\mathcal{S}\to\mathcal{S}$ for $k\in K$ be continuous. It follows easily that the maps $s\mapsto(-s)$ and $(s_1,s_2)\mapsto s_1+s_2$ also are continuous. Sheaves of $K$ algebras are defined similarly, with the additional requirement in (c) that the map $(s_1,s_2)\mapsto s_1\cdot s_2$ of $\mathcal{S}\circ\mathcal{S}\to\mathcal{S}$ be continuous.

The map $\pi$ is called the projection; and the $K$-module $\mathcal{S}_m = \pi^{-1}(m)$ is called the stalk over $m \in M$. Let $U \subset M$ be open. A continuous map $f: U \to \mathcal{S}$ such that $\pi \circ f = id$ is called a section of $\mathcal{S}$ over $U$. The 0-section is the section which associates with $m \in U$ the zero element of $\mathcal{S}_m$. We let $\Gamma(\mathcal{S}, U)$ denote the set of sections of $\mathcal{S}$ over $U$. We make $\Gamma(\mathcal{S}, U)$ into a $K$-module as follows. Let $f$ and $g$ belong to $\Gamma(\mathcal{S}, U)$, and let $k \in K$. We define the sum of $f$ and $g$ to be the section

 $$ (f+g)(m)=f(m)+g(m)\qquad(m\in U), $$ 

and we define a section $kf$ by setting

 $$ (k f)(m)=k\bigl(f(m)\bigr)\qquad(m\in U). $$ 

With these operations, $\Gamma(8,U)$ becomes a $K$-module. The module of sections of $\mathcal{S}$ over $M$ (global sections) will simply be denoted by $\Gamma(8)$. Observe that since $\pi$ is a local homeomorphism, sections are open maps; and if sections $f$ and $g$ agree at $m\in M$, then they must agree on a neighborhood of $m$.

5.2 Examples The most elementary example of a sheaf over $M$ is that of a so-called constant sheaf $\mathcal{G} = M \times G$, where $G$ is a $K$-module with the discrete topology and $\mathcal{G}$ is given the product topology. Here the projection is simply $\pi(m,g) = m$.

A less trivial example is the following. Let $F_{m}$ denote the set of germs of $C^{\infty}$ functions at $m\in M$ (as in 1.13), and let

 $$ \mathcal{C}^{\infty}(M)=\bigcup_{m\in M}\widetilde{F}_{m}. $$ 

When it will introduce no confusion, we shall denote $\mathcal{C}^{\infty}(M)$ simply by $\mathcal{C}^{\infty}$. We define the projection $\pi\colon \mathcal{C}^{\infty} \to M$ in the obvious fashion so that $\mathbf{f} \in \widetilde{F}_{\pi(f)}$. Associate with each open set $U$ in $M$ and each $C^{\infty}$ function $f$ on $U$ the set

 $$ \bigcup_{m\in U}\mathbf{f}_{m}\subset\mathcal{C}^{\infty}, $$ 

where  $ f_m $ is the germ of  $ f $ at  $ m $. The collection of these sets forms a basis for a topology on  $ \mathcal{C}^\infty $ which makes  $ \mathcal{C}^\infty $ into a sheaf of real vector spaces (in fact, a sheaf of algebras since each  $ F_m $ has an algebra structure).  $ \mathcal{C}^\infty(M) $ is called the sheaf of germs of  $ C^\infty $ functions on  $ M $. Similarly, one constructs the sheaf  $ \mathcal{C}^\flat(M) $ of germs of functions of class  $ C^\flat $ on  $ M $ for each integer  $ p \geq 0 $.

5.3 Remark One should be cautioned that sheaves are generally not Hausdorff spaces. A simple example is provided by the sheaf  $ \mathcal{C}^0(\mathbb{R}) $ of germs of continuous functions on the real line. Let  $ g(t) \equiv 0 $, let  $ f(t) = 0 $ for  $ t \leq 0 $, and let  $ f(t) = t $ for  $ t > 0 $. Then the germs of  $ f $ and  $ g $ at the origin are distinct elements of  $ \mathcal{C}^0(\mathbb{R}) $; however,  $ f $ and  $ g $ have the same germ for each  $ t < 0 $. It follows that the germs of  $ f $ and  $ g $ at the origin cannot be separated by disjoint open sets in  $ \mathcal{C}^0(\mathbb{R}) $.

5.4 Definitions Let S and S' be sheaves on M with projections  $ \pi $ and  $ \pi' $ respectively. A continuous map  $ \varphi\colon S \to S' $ such that  $ \pi' \circ \varphi = \pi $ is called a sheaf mapping. Observe that sheaf mappings are necessarily local homeomorphisms, and they map stalks into stalks. A sheaf mapping  $ \varphi $ which is a homomorphism (of K-modules) on each stalk is called a sheaf homomorphism. A sheaf isomorphism is a sheaf homomorphism with an inverse which is also a sheaf homomorphism.

An open set $\mathcal{R}$ in the sheaf $\mathcal{S}$ such that the subset $\mathcal{R}_m = \mathcal{R} \cap \mathcal{S}_m$ is a submodule of $\mathcal{S}_m$ for each $m \in M$ is called a subsheaf of $\mathcal{S}$. It is clear that a subsheaf of $\mathcal{S}$, with the natural topology and the projection map which it inherits from $\mathcal{S}$, is again a sheaf.

Let $\varphi: \mathcal{S} \to \mathcal{T}$ be a homomorphism of sheaves. The kernel of $\varphi$ (ker $\varphi$) is the subset of $\mathcal{S}$ which maps under $\varphi$ into the 0-section of $\mathcal{T}$, and is in fact a subsheaf of $\mathcal{S}$. The subsheaf $\varphi(\mathcal{S}) \subset \mathcal{T}$ is called the image of $\varphi$ (im $\varphi$). In the case in which $\varphi$ is one-to-one, we shall often identify $\mathcal{S}$ with $\varphi(\mathcal{S})$ and speak of the subsheaf $\mathcal{S}$ of $\mathcal{T}$.

Let $\mathcal{R}$ be a subsheaf of $\mathcal{S}$. For each $m\in M$, let $\mathcal{T}_{m}$ denote the quotient module $S_{m}/\mathcal{R}_{m}$, and let

 $$ \mathcal{T}=\bigcup_{m\in\mathcal{M}}\mathcal{T}_{m}. $$ 

Let $\tau: \mathcal{S} \to \mathcal{T}$ be the natural map which associates with each element of $\mathcal{S}_m$ its coset in $\mathcal{T}_m$, for each $m$, and give $\mathcal{T}$ the quotient topology. That is, a set $U$ in $\mathcal{T}$ will be open if and only if $\tau^{-1}(U)$ is open in $\mathcal{S}$. Then, with this topology and with the natural projection which maps each element of $\mathcal{T}_m$ to $m$, $\mathcal{T}$ is a sheaf over $M$ and $\tau: \mathcal{S} \to \mathcal{T}$ is a sheaf homomorphism. We leave the details as an exercise. $\mathcal{T}$ is called the quotient sheaf of $\mathcal{S}$ modulo $\mathcal{R}$.

If $\varphi: \mathcal{S} \to \mathcal{T}$ is a homomorphism of sheaves, then it is easily checked that the natural map $\mathcal{S}/\ker \varphi \to \mathrm{im} \varphi$ given by $(s + (\ker \varphi \mid \mathcal{S}_m)) \mapsto \varphi(s)$ for $s \in \mathcal{S}_m$ is a sheaf isomorphism.

A sequence of sheaves and homomorphisms

 $$ \cdots\to\mathcal{S}_{i}\to\mathcal{S}_{i+1}\to\mathcal{S}_{i+2}\to\cdots $$ 

is called exact if at each stage the image of a given homomorphism is the kernel of the next. Exact sequences of K-modules are defined similarly. Observe that (2) is exact if and only if for each $m\in M$ the induced sequence of homomorphisms of the stalks over $m$, namely,

 $$ \cdots\to(\mathcal{S}_{i})_{m}\to(\mathcal{S}_{i+1})_{m}\to(\mathcal{S}_{i+2})_{m}\to\cdots, $$ 

is exact. If $\mathcal{R}$ is a subsheaf of $\mathcal{S}$, and $\mathcal{T}$ is the quotient sheaf $\mathcal{S}/\mathcal{R}$, then the natural sequence of homomorphisms

 $$ 0\to\mathcal{R}\to\mathcal{S}\to\mathcal{T}\to0 $$ 

is exact, where 0 denotes the constant sheaf over M whose stalk over each point is the trivial K-module consisting of only one element. Exact sequences of the form (4) consisting of only five terms with the first and last being the 0 sheaf are called short exact sequences. Short exact sequences of K-modules are defined similarly.

5.5 Presheaves A presheaf $P = \{S_U; \rho_{U,V}\}$ of $K$-modules on $M$ consists of a $K$-module $S_U$ for each open set $U$ in $M$ and a homomorphism $\rho_{U,V}: S_V \to S_U$ for each inclusion $U \subset V$ of open sets in $M$, such that $\rho_{U,U} = \mathrm{id}$, and such that whenever $U \subset V \subset W$, the following diagram commutes:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//ddeb4196-c1d2-4123-a4d2-03d9ef101377/markdown_0/imgs/img_in_image_box_358_1002_571_1176.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A15Z%2F-1%2F%2F5f7533f6f81f050615931aa3d846cf2d16f45316a57c854a6a798d04deb389cf" alt="Image" width="22%" /></div>


A typical example of a presheaf is the following. Associate with each open set $U$ in $M$ the algebra $C^\infty(U)$ of $C^\infty$ functions on $U$, and let $\rho_{U,V}$ be the map which restricts a $C^\infty$ function on $V$ to a $C^\infty$ function on $U$. This yields a presheaf $\{C^\infty(U);\rho_{U,V}\}$ of real vector spaces (in fact algebras) on $M$. Similarly, one could associate with $U$ the vector space of $p$-forms on $U$ for some fixed $p$ and again let $\rho_{U,V}$ be the restriction mapping.

Let $P=\{S_{U};\rho_{U,V}\}$ and $P^{\prime}=\{S_{U}^{\prime};\rho_{U,V}^{\prime}\}$ be presheaves on $M$. By a presheaf homomorphism of $P$ to $P^{\prime}$ we mean a collection $\{\varphi_{U}\}$ of homomorphisms $\varphi_{U}\colon S_{U}\to S_{U}^{\prime}$ such that

 $$ \rho_{U,V}^{\prime}\circ\varphi_{V}=\varphi_{U}\circ\rho_{U,V} $$ 

whenever $U \subset V$. A presheaf isomorphism is a presheaf homomorphism $\{\varphi_{U}\}$ in which each $\varphi_{U}$ is an isomorphism of $K$-modules.

5.6 The Relationship between Sheaves and Presheaves Each sheaf  $ \mathcal{S} $ gives rise canonically to a presheaf  $ \{\Gamma(8,U);\rho_{U,V}\} $. Here we associate with each open set  $ U $ in  $ M $ the  $ K $-module  $ \Gamma(8,U) $ of sections of  $ \mathcal{S} $ over  $ U $, and to each inclusion  $ U \subset V $ of open sets in  $ M $ we associate the homomorphism

 $$ \rho_{U,V}\colon\Gamma(\mathcal{S},V)\to\Gamma(\mathcal{S},U) $$ 

which maps a section of S over V to its restriction to U. We shall denote this map of sheaves to presheaves by $\alpha$. We call $\alpha(\mathcal{S})$ the presheaf of sections of the sheaf $\mathcal{S}$.

Conversely, we shall now show that each presheaf canonically determines a sheaf, which we call its associated sheaf. In practice, many sheaves will in this manner arise naturally from presheaves. The best example to keep in mind during the following construction is the presheaf  $ \{C^\infty(U);\rho_{U,\mathcal{V}}\} $; its associated sheaf will be the sheaf of germs of  $ C^\infty $ functions on  $ M $.

Let $P = \{S_U; \rho_{U,V}\}$ be a presheaf of $K$-modules on $M$. Let $m \in M$, and let $S_m^*$ be the disjoint union of each of the modules $S_U$ for which $m \in U$. If we set $f \in S_U$ equivalent to $g \in S_V$ if and only if there is a neighborhood $W$ of $m$ with $W \subset U \cap V$ such that $\rho_{W,U}f = \rho_{W,V}g$, we obtain an equivalence relation on $S_m^*$. The set $S_m$ of equivalence classes of elements of $S_m^*$ will be the stalk of the associated sheaf over $m$. If $m \in U$, let $\rho_{m,U}: S_U \to S_m$ be the natural projection which assigns to each element of $S_U$ its equivalence class. Let $f \in S_U$ and $g \in S_V$ be representatives of classes $s_1$ and $s_2$ in $S_m$ respectively. There exists a neighborhood $W$ of $m$ such that $W \subset U \cap V$. Define addition in $S_m$ by setting

 $$ s_{1}+s_{2}=\rho_{m,w}(\rho_{W,U}f+\rho_{W,V}g), $$ 

and define multiplication by  $ k \in K $ by setting

 $$ k s_{1}=\rho_{m,U}(k f). $$ 

It is easy to check that the operations in (3) and (4) are well-defined and give $S_{m}$ the structure of a $K$-module such that the maps $\rho_{m,U}$ are all homomorphisms. $S_{m}$ is known as the direct limit of the modules $S_{U}$ for $U$ containing $m$. Now let

 $$ \mathcal{S}=\bigcup_{m\in M}\mathcal{S}_{m}, $$ 

and let $\pi: \mathcal{S} \to M$ be the obvious projection such that $\pi(\mathcal{S}_m) = m$. We topologize $\mathcal{S}$ by taking for a basis of the topology the collection of subsets of $\mathcal{S}$ of the form

 $$ O_{f}=\{\rho_{p,U}f\colon p\in\mathcal{U}\} $$ 

for the various $f\in S_U$ and the various open sets $U$ in $M$. This collection does indeed form a basis for a topology on $\mathcal{S}$, for if $s\in O_f\cap O_g$, say $s=\rho_{p,U}f=\rho_{p,v}g$, then there is a neighborhood $W$ of $p$ with $W\subset U\cap V$ for which $\rho_{W,U}f=\rho_{W,v}g$, from which it follows that $s\in O_{\rho_{W,U}f}\subset O_f\cap O_g$.

We claim that $\mathcal{S}$ is a sheaf over $M$ with projection $\pi$. Now $\pi$ is a local homeomorphism since it is a homeomorphism on each $O_f$. Each stalk $\mathcal{S}_m$ has been given the structure of a $K$-module, so finally we need only check that the composition operations are continuous. Consider first multiplication by $k \in K$. Let $s \in \mathcal{S}$, and let $O$ be an open neighborhood of $ks$. Let $s = \rho_p, v f$. Then $O_{k f}$ is also an open neighborhood of $ks$. Let $V$ be a neighborhood of $p$ contained in $\pi(O_{k f} \cap O)$. Then $O_{p_v, v f}$ is an open neighborhood of $s$ which maps under multiplication by $k$ into the open neighborhood $O_{p_v, v f} \subset O$ of $ks$. Finally, we show that the map $(s_1, s_2) \mapsto s_1 - s_2$ of $\mathcal{S} \circ \mathcal{S} \to \mathcal{S}$ is continuous. For let $O_f$ be an open neighborhood of $s_1 - s_2$, say $s_1 - s_2 = \rho_p, v f$, and let $s_1 = \rho_p, v g$ and $s_2 = \rho_p, v h$. Then there exists an open neighborhood $Q$ of $p$ with $Q \subset U \cap V \cap W$ such that

 $$ \rho_{Q,\mathbf{v}}f=\rho_{Q,\mathbf{v}}g-\rho_{Q,\mathbf{w}}h. $$ 

It follows that the open neighborhood

 $$ O_{\rho_{\mathbf{Q},\mathbf{v}}\mathfrak{s}}\times\mathcal{O}_{\rho_{\mathbf{Q},\mathbf{w}}h}\cap\mathcal{S}\circ\mathcal{S} $$ 

of $(s_{1}, s_{2})$ maps into $O_{r}$. Thus the composition operations are continuous, and $\mathcal{S}$ is a sheaf over $M$ with projection $\pi$. $\mathcal{S}$ is called the sheaf associated with the presheaf $P$. We shall denote this map of presheaves to sheaves by $\beta$; thus $\mathcal{S} = \beta(P)$.

Clearly, each sheaf homomorphism $\varphi\colon\mathcal{S}\to\mathcal{T}$ gives rise to a presheaf homomorphism between the presheaves of sections $\alpha(\mathcal{S})$ and $\alpha(\mathcal{T})$ by composing elements of $\Gamma(\mathcal{S},U)$ with $\varphi$. Conversely, a presheaf homomorphism $\{\varphi_U\}$ from $P$ to $P'$ canonically induces a homomorphism $\varphi$ of the associated sheaves $\beta(P)$ and $\beta(P')$ such that

 $$ \rho_{\mathfrak{p},U}^{\prime}\circ\varphi_{U}=\varphi\circ\rho_{\mathfrak{p},U} $$ 

for each open set $U$ in $M$ and each $p \in U$. Moreover, in going in either direction, from homomorphisms of sheaves to homomorphisms of presheaves, or vice versa, the composition of two homomorphisms induces the composition of the corresponding homomorphisms.

Suppose now that we start with a sheaf $\mathcal{S}$, take its presheaf $\alpha(\mathcal{S})$ of sections, and then form the associated sheaf $\beta(\alpha(\mathcal{S}))$, thus obtaining the sheaf of germs of sections of $\mathcal{S}$. Then the sheaves $\mathcal{S}$ and $\beta(\alpha(\mathcal{S}))$ are canonically isomorphic. Indeed, let $\xi \in \beta(\alpha(\mathcal{S}))$ be the germ at $p$ of some section $f$ of $\mathcal{S}$ over an open set $U$ containing $p$; that is, $\xi = \rho_{p,U}f$ for $f \in \Gamma(\mathcal{S}, U)$. Then $\xi \mapsto f(p)$ determines a well-defined map $\beta(\alpha(\mathcal{S})) \to \mathcal{S}$ which is a sheaf isomorphism. We leave the details as an exercise.

Generally, however, if we start with a presheaf $P$ and take the presheaf $\alpha(\beta(P))$ of sections of the sheaf associated with $P$, we may get a presheaf quite distinct from $P$. For example, let $P = \{S_U; \rho_{U,V}\}$ where $S_U$ is the principal ideal domain $K$ for each $U$, and all restrictions $\rho_{U,V}$ for $U \subsetneq V$ are identically 0. Then the presheaf $\alpha(\beta(P))$ assigns to each open set $U$ in $M$ the zero $K$-module. The conditions of the following definition are clearly necessary if $P$ is to be isomorphic with $\alpha(\beta(P))$, and it will be shown in §5.8 that they are also sufficient.

5.7 Definition A presheaf $\{S_{U};\rho_{U,V}\}$ on $M$ is said to be complete if whenever the open set $U$ is expressed as a union $\bigcup U_{*}$ of open sets in $M$, the following two conditions are satisfied:

 $ (C_{1})' $ Whenever f and g in  $ S_{U} $ are such that  $ \rho_{U_{a},U}f = \rho_{U_{a},U}g $ for all  $ \alpha $, then f = g.

$(C_{2})$ Whenever there is an element $f_{\alpha}\in S_{U_{\alpha}}$ for each $\alpha$ such that $\rho_{U_{\alpha}\cap U_{\beta},U_{\alpha}}f_{\alpha}=\rho_{U_{\alpha}\cap U_{\beta},U_{\beta}}f_{\beta}$ for all $\alpha$ and $\beta$, then there exists $f\in S_{U}$ such that $f_{\alpha}=\rho_{U_{\alpha},U}$ for each $\alpha$.

5.8 Proposition If $P$ is a complete presheaf, then $\alpha(\beta(P))$ is canonically isomorphic with $P$.

PROOF Let $P=\{S_{U};\rho_{U,V}\}$. We define a presheaf homomorphism from $P$ to $\alpha(\beta(P))$ as follows. For each open set $U$ in $M$ we map

 $$ S_{U}\to\Gamma\bigl(\beta(P),U\bigr) $$ 

by sending the element f of  $ S_{U} $ to the section

 $$ p\mapsto\rho_{p,U}f $$ 

of $\beta(P)$ over $U$. To prove that this presheaf homomorphism is an isomorphism, we need to prove that each of the homomorphisms (1) are isomorphisms. Injectivity follows from $5.7(C_{1})$, for if $f$ in $S_{U}$ maps to the 0-section, then there exists a cover $\{U_{a}\}$ of $U$ such that $\rho_{U_{a},U}f=\rho_{U_{a},V}(0)$. Therefore $f=0\in S_{U}$ by $(C_{1})$. To prove surjectivity, let $c$

be a section of $\beta(P)$ over $U$. Then for each $p \in U$, there is a neighborhood $U_p$ of $p$ and an element $f_p \in S_{U_p}$ such that

 $$ \rho_{a,U_{p}}f_{p}=c(q) $$ 

for all $q\in U_{p}$. It follows from (3) and $5.7(C_{1})$ that for each $p$ and $q$ in $U$,

 $$ \rho_{U_{g}\cap U_{q},U_{p}}f_{g}=\rho_{U_{g}\cap U_{q},U_{e}}f_{e}. $$ 

Thus, according to 5.7( $ C_{2} $), there exists  $ f \in S_{U} $ such that

 $$ f_{o}=\rho_{U_{o},U}f $$ 

for each $p \in U$. It follows from (5), (3), and (2) that $f$ maps to $c$ under the homomorphism (1).

5.9 Tensor Products Before we define the tensor products of sheaves and presheaves, we need a few preliminary remarks. The definition of the tensor product  $ S \otimes T $ of K-modules S and T is completely analogous to that for the special case 2.1 of tensor products of  $ \mathbb{R} $-modules. If  $ f: S \to S' $ and  $ h: T \to T' $ are homomorphisms of K-modules, then their tensor product  $ f \otimes h $ is the homomorphism of  $ S \otimes T $ into  $ S' \otimes T' $ uniquely associated by the universal mapping property 2.2(a) with the bilinear map

 $$ (s,t)\mapsto f(s)\otimes h(t) $$ 

of  $ S \times T $ into  $ S' \otimes T' $.

Observe that if S is a K-module, then there is a canonical isomorphism

 $$ S\otimes K\cong S. $$ 

Indeed, let $f: S \otimes K \to S$ be the homomorphism determined by the bilinear map $(s, k) \mapsto ks$ of $S \times K \to S$. Then $f$ is clearly surjective, and is also injective since $\sum_{i}(s_{i} \otimes k_{i}) = \left(\sum_{i} k_{i} s_{i}\right) \otimes 1$, so if $f\left(\sum_{i}(s_{i} \otimes k_{i})\right) = 0$, then $\sum_{i} k_{i} s_{i} = 0$, which implies $\sum_{i}(s_{i} \otimes k_{i}) = 0$.

Now let $P=\{S_{U};\rho_{U,V}\}$ and $P^{\prime}=\{S_{U}^{\prime};\rho_{U,V}^{\prime}\}$ be presheaves on $M$. Then their tensor product is the presheaf

 $$ \begin{array}{r}{P\otimes P^{\prime}=\{S_{U}\otimes S_{U}^{\prime};\rho_{U,V}\otimes\rho_{U,V}^{\prime}\}.}\end{array} $$ 

If $\{\varphi_U\}$: $P \to Q$ and $\{\varphi'_U\}$: $P' \to Q'$ are homomorphisms of presheaves (5.5(2)), then their tensor product $\{\varphi_U\} \otimes \{\varphi'_U\}$ is by definition the homomorphism $\{\varphi_U \otimes \varphi'_U\}$ of $P \otimes P'$ into $Q \otimes Q'$.

If S and T are sheaves over M, we define their tensor product S ⊗ T to be the sheaf associated with the tensor product of the presheaves of sections of S and T. That is,

 $$ \mathcal{S}\otimes\mathcal{T}=\beta\big(\alpha(\mathcal{S})\otimes\alpha(\mathcal{T})\big). $$ 

Moreover, if $\varphi: \mathcal{S} \to \mathcal{T}$ and $\gamma: \mathcal{S}' \to \mathcal{T}'$ are sheaf homomorphisms, and if $\{\varphi_U\}: \alpha(\mathcal{S}) \to \alpha(\mathcal{T})$ and $\{\varphi_U\}: \alpha(\mathcal{S}') \to \alpha(\mathcal{T}')$ are the corresponding homomorphisms on the presheaves of sections, then we define the tensor product $\varphi \otimes \gamma$ to be the homomorphism $\mathcal{S} \otimes \mathcal{S}' \to \mathcal{T} \otimes \mathcal{T}'$ associated with the presheaf homomorphism

 $$ \{\varphi_{U}\}\otimes\{\gamma_{U}\}\colon\alpha(\mathcal{S})\otimes\alpha(\mathcal{S}^{\prime})\to\alpha(\mathcal{T})\otimes\alpha(\mathcal{T}^{\prime}). $$ 

The reader should check that there is a canonical isomorphism

 $$ (\mathcal{S}\otimes\mathcal{T})_{m}\cong\mathcal{S}_{m}\otimes\mathcal{T}_{m}, $$ 

so in particular if $\mathcal{H}$ is the constant sheaf $M\times K$, then in view of (2) there is a canonical isomorphism

 $$ \mathcal{S}\otimes\mathcal{H}\cong\mathcal{S}. $$ 

Moreover, if $\varphi$ and $\gamma$ are sheaf homomorphisms as above, then the reader should check that

 $$ (\varphi\otimes\gamma)\left|(\mathcal{S}\otimes\mathcal{S}^{\prime})_{m}=\varphi\right|\mathcal{S}_{m}\otimes\gamma\left|\mathcal{S}_{m}^{\prime}.\right. $$ 

One might ask, “Why not define $8\otimes\mathcal{F}$ and $\varphi\otimes\gamma$ by (6) and (8) rather than going to presheaves and back?” We could indeed proceed in this way, but it would involve a considerable duplication of previous work. The reason is that if we define the tensor products by (6) and (8), then we would also have to define the topology on $8\otimes\mathcal{F}$ and check that the properties $5.1(a)$ and (c) are satisfied, and would also have to prove that $\varphi\otimes\gamma$ is continuous. In defining $8\otimes\mathcal{F}$ and $\varphi\otimes\gamma$ by going to presheaves and back, the work of showing that $8\otimes\mathcal{F}$ is really a sheaf and that $\varphi\otimes\gamma$ is a sheaf homomorphism has already been carried out in the analysis of the maps $\alpha$ and $\beta$ of 5.6.

5.10 Fine Sheaves A sheaf 8 over M is said to be fine if for each locally finite cover  $ \{U_{i}\} $ of M by open sets there exists for each i an endomorphism  $ l_{i} $ of S such that:

(a)  $ \mathrm{supp}(I_i) \subset U_i $.

(b)  $ \sum_{i} l_{i} = id $.

Here, by $\operatorname{supp}(l_{i})$ (the support of $l_{i}$) we mean the closure of the set of points in $M$ for which $l_{i} \bigm| \mathcal{S}_{m}$ is not zero. We shall call $\{l_{i}\}$ a partition of unity for 8 subordinate to the cover $\{U_{i}\}$ of $M$.

An example of a fine sheaf is the sheaf  $ \mathcal{C}^{\infty}(M) $ of germs of  $ C^{\infty} $ functions on  $ M $. If  $ \{U_i\} $ is a locally finite open cover of  $ M $, let  $ \{\varphi_i\} $ be a partition of unity on  $ M $ subordinate to this cover (Theorem 1.11). We obtain endomorphisms  $ \widetilde{I}_i $ of the presheaf  $ \{C^{\infty}(U);\rho_{U,V}\} $ by setting

 $$ \tilde{l}_{i}(f)=(\varphi_{i}\bigm|U)\cdot f\quad\mathsf{f o r}f\in C^{\infty}(U). $$ 

The associated sheaf endomorphisms $l_{i}$ of $\mathcal{C}^{\infty}(M)$ form a partition of unity subordinate to the cover $\{U_{i}\}$ of $M$.

Let $\mathcal{S}$ and $\mathcal{T}$ be sheaves over $M$, with $\mathcal{S}$ fine. Then $\mathcal{S} \otimes \mathcal{T}$ is itself a fine sheaf. Indeed, if $\{l_i\}$ is a partition of unity for $\mathcal{S}$ subordinate to the cover $\{U_i\}$ of $M$, then $\{l_i \otimes \mathrm{id}\}$ is a partition of unity for $\mathcal{S} \otimes \mathcal{T}$.

5.11 A sheaf homomorphism $\varphi: \mathcal{S} \to \mathcal{T}$ gives rise to a homomorphism $\Gamma(\mathcal{S}) \to \Gamma(\mathcal{T})$ of the modules of global sections by composing sections of $\mathcal{S}$ with $\varphi$. We leave as an exercise the fact that a short exact sequence

 $$ 0\to\mathcal{S}^{\prime}\to\mathcal{S}\to\mathcal{S}^{\prime \prime}\to0 $$ 

gives rise to an exact sequence

 $$ 0\to\Gamma(\mathcal{S}^{\prime})\to\Gamma(\mathcal{S})\to\Gamma(\mathcal{S}^{\prime \prime}). $$ 

However, the homomorphism  $ \Gamma(\mathcal{S}) \to \Gamma(\mathcal{S}') $ is generally not surjective. Consider the following example.

Let  $ \mathcal{S}_{p_1, p_2} $ be the “skyscraper” sheaf over a connected  $ M $ whose stalk is the zero  $ K $-module over each point except over the distinct points  $ p_1 $ and  $ p_2 $ where the stalk is  $ K $. (Note that the topology on  $ \mathcal{S}_{p_1, p_2} $ is uniquely determined by the requirement that  $ \mathcal{S}_{p_1, p_2} $ be a sheaf.) Let  $ \mathcal{H} $ as usual be the constant sheaf with stalk  $ K $. There is an obvious homomorphism of  $ \mathcal{H} $ onto  $ \mathcal{S}_{p_1, p_2} $, namely, the homomorphism is zero on all stalks of  $ \mathcal{H} $ except on those over  $ p_1 $ and  $ p_2 $ where it is the identity map. However, the associated map  $ \Gamma(\mathcal{H}) \to \Gamma(\mathcal{S}_{p_1, p_2}) $ cannot be surjective for  $ \Gamma(\mathcal{H}) \cong K $, whereas  $ \Gamma(\mathcal{S}_{p_1, p_2}) \cong K \oplus K $.

Exactness of (1) is a purely local property, whereas exactness of (2) is a global property. We will see that certain sheaf cohomology modules will provide an extension of the exact sequence (2) and thus will provide a measure of the extent to which $\Gamma(\mathcal{S}) \to \Gamma(\mathcal{S}^*)$ fails to be surjective.

5.12 Theorem Let $\boldsymbol{\varphi}:\mathcal{S}\to\mathcal{T}$ be a surjective sheaf homomorphism with kernel $\mathcal{R}$. Suppose that $\mathcal{R}$ is a fine sheaf. Then the homomorphism $\Gamma(\mathcal{S})\to\Gamma(\mathcal{T})$ is surjective.

PROOF Let $t$ be a global section of $\mathcal{T}$. We must construct a section $s$ of $\mathcal{S}$ such that $\varphi \circ s = t$. By the continuity of $\varphi$ and $t$ and by the property 5.1(a) of $\mathcal{S}$ and $\mathcal{T}$ there is a covering $\{U_i\}$ of $M$ by open sets and, for each $i$, a section $s_i$ of $\mathcal{S}$ over $U_i$ such that

 $$ \varphi\circ s_{i}=t\mid U_{i}. $$ 

Since $M$ is paracompact, we can assume that the cover $\{U_{i}\}$ is locally finite. The difference

 $$ S_{i j}=S_{i}-S_{j} $$ 

is a section of the kernel  $ \mathcal{R} $ over  $ U_i \cap U_j $, and on  $ U_i \cap U_j \cap U_k $ the differences satisfy

 $$ s_{i j}+s_{j k}=s_{i k}. $$ 

Now, let $\{l_i\}$ be a partition of unity for $\mathcal{R}$ subordinate to the cover $\{U_i\}$ of $M$. Consider the section $l_i \circ s_{ij}$ of $\mathcal{R}$ over $U_i \cap U_i$. Since the support of $l_i$ lies in $U_i$, we can extend the section $l_i \circ s_{ij}$ to be a continuous section of $\mathcal{R}$ over $U_i$ by defining it to be zero on points of $U_i - U_j$. Let

 $$ s_{i}^{\prime}=\sum_{j}l_{j}\circ s_{i j}. $$ 

Then $s_{i}^{\prime}$ is a section of $\mathcal{R}$ over $U_{i}$, and by (3) and (4) the difference

 $$ s_{i}^{\prime}-s_{j}^{\prime}=\sum_{k}l_{k}\circ s_{i k}-\sum_{k}l_{k}\circ s_{j k}=\sum_{k}l_{k}\circ s_{i j}=s_{i j} $$ 

over  $ U_{i} \cap U_{j} $. Thus

 $$ s_{i}-s_{i}^{\prime}=s_{j}-s_{j}^{\prime} $$ 

on $U_i \cap U_s$. It follows that if we set $s(m) = (s_i - s'_i)(m)$ for $m \in U_i$, then $s$ is a well-defined global section of $\mathcal{S}$ such that $\varphi \circ s = t$.

5.13 Definitions A K-module X is torsionless if there is no non-zero element  $ x \in X $ for which there exists a non-zero element  $ k \in K $ such that  $ kx = 0 $. A sheaf of K-modules is said to be torsionless if each stalk is a torsionless K-module.

We shall need the following basic lemma concerning tensor products and exact sequences. This is the first of two fundamental algebraic propositions which we shall need in this chapter for which we shall not provide proofs. (The second proposition is the Kunneth formula, which we shall need in 5.42.) The proofs are rather long, are not of particular interest for our purposes, and would tend to obscure the main goals of the chapter. The interested reader can find a proof of the following lemma in Spanier [28, pp. 215, 221].

### 5.14 Lemma Let

 $$ 0\to A^{\prime}\to A\to A^{\prime \prime}\to0 $$ 

be an exact sequence of K-modules, and let B be a K-module. Then the induced sequence

 $$ A^{\prime}\otimes B\to A\otimes B\to A^{\prime \prime}\otimes B\to0 $$ 

(whose homomorphisms are the homomorphisms of (1) tensored with the identity�homomorphism of $B$) is exact, but $A'\otimes B\to A\otimes B$ is not necessarily injective. If, however, either $A'$ or $B$ is torsionless, then the full sequence

 $$ 0\to A^{\prime}\otimes B\to A\otimes B\to A^{\prime \prime}\otimes B\to0 $$ 

is exact.

(We should point out that (3) is the first place in this chapter where the fact that the ring K is actually a principal ideal domain is used.)

### 5.15 Theorem Let

 $$ 0\to\mathcal{S}^{\prime}\to\mathcal{S}\to\mathcal{S}^{\prime \prime}\to0 $$ 

be an exact sequence of sheaves over M, and let  $ \mathcal{T} $ be also a sheaf over M. Then if either  $ \mathcal{T} $ or  $ 8'' $ is torsionless, then the sequence

 $$ 0\to\mathcal{S}^{\prime}\otimes\mathcal{T}\to\mathcal{S}\otimes\mathcal{T}\to\mathcal{S}^{\prime \prime}\otimes\mathcal{T}\to0 $$ 

is exact. If, in addition, either  $ \mathcal{T} $ or  $ \mathcal{S}' $ is a fine sheaf, then the sequence

 $$ 0\to\Gamma(\mathcal{S}^{\prime}\otimes\mathcal{T})\to\Gamma(\mathcal{S}\otimes\mathcal{T})\to\Gamma(\mathcal{S}^{\prime \prime}\otimes\mathcal{T})\to0 $$ 

is exact.

PROOF The exactness of (2) follows from 5.14. If either $\mathcal{F}$ or $S'$ is fine, then, according to 5.10, $S' \otimes \mathcal{F}$ is fine; and this together with (2) above, 5.11(2), and 5.12 proves that (3) is exact.

##### COCHAIN COMPLEXES

5.16 Definitions A cochain complex  $ C^{*} $ consists of a sequence of K-modules and homomorphisms

 $$ \cdots\to C a^{-1}\to C a\to C a^{+1}\to\cdots $$ 

defined for all integers $q$ such that at each stage the image of a given homomorphism is contained in the kernel of the next. The homomorphism $C^{q} \to C^{q+1}$ (which we shall refer to as $d^{q}$, or simply $d$ if the index $q$ is not needed for clarification) is called the $q$th cobondary operator. The kernel $Z^{q}(C^{*})$ of $d^{q}$ is the module of $q$th degree cocytes of the cochain complex $C^{*}$, and the image $B^{q}(C^{*})$ of $d^{q-1}$ is the module of $q$th degree coboundaries. The $q$th cohomology module $H^{q}(C^{*})$ is defined to be the quotient module

 $$ H^{a}(C^{*})=Z^{a}(C^{*})/B^{a}(C^{*}). $$ 

Let  $ C^* $ and  $ D^* $ be cochain complexes. A cochain map  $ C^* \to D^* $ consists of a collection of homomorphisms  $ C^q \to D^q $ such that for each  $ q $, the diagram

 $$ \begin{array}{c}C^{a+1}\longrightarrow D^{a+1}\\\uparrow\quad\uparrow\\C^{a}\longrightarrow D^{a}\end{array} $$ 

commutes. It follows from (3) that a cochain map sends the module of q-cocyles of  $ C^* $ into the module of q-cocycles of  $ D^* $ and maps the module of q-coboundaries of  $ C^* $ into the module of q-coboundaries of  $ D^* $, and thus induces a homomorphism of the cohomology modules

 $$ H^{a}(C^{*})\to H^{a}(D^{*}). $$ 

The composition $C^{*}\to E^{*}$ of two cochain maps $C^{*}\to D^{*}$ and $D^{*}\to E^{*}$ induces on the cohomology modules the homomorphism $H^{q}(C^{*})\to H^{q}(E^{*})$, which is the composition of $H^{q}(C^{*})\to H^{q}(D^{*})$ and $H^{q}(D^{*})\to H^{q}(E^{*})$.

A sequence of cochain maps

 $$ 0\longrightarrow C^{*}\longrightarrow D^{*}\longrightarrow E^{*}\longrightarrow0 $$ 

forms a short exact sequence if for each $q$,

 $$ 0\longrightarrow C^{a}\longrightarrow D^{a}\longrightarrow E^{a}\longrightarrow0 $$ 

is a short exact sequence of K-modules. A homomorphism between short exact sequences $0 \to C^{*} \to D^{*} \to E^{*} \to 0$ and $0 \to \bar{C}^{*} \to \bar{D}^{*} \to \bar{E}^{*} \to 0$ of cochain complexes consists of cochain maps $C^{*} \to \bar{C}^{*}$, $D^{*} \to \bar{D}^{*}$, and $E^{*} \to \bar{E}^{*}$ such that we have a commutative diagram:

 $$ \begin{aligned}{0\to C^{*}}&{{}\to D^{*}\to E^{*}\to0}\\ {\downarrow}&{{}\quad\downarrow\quad\downarrow}\\ {0\to\tilde{C}^{*}}&{{}\to\tilde{D}^{*}\to\tilde{E}^{*}\to0.}\\ \end{aligned} $$ 

5.17 Proposition Given the short exact sequence 5.16(5) of cochain maps, there are homomorphisms

 $$ H^{q}(E^{*})\xrightarrow{\partial}H^{q+1}(C^{*}) $$ 

for each q such that the sequence

 $$ \cdots\to H^{q-1}(E^{*})\xrightarrow{\partial}H^{q}(C^{*})\to H^{q}(D^{*})\to H^{q}(E^{*})\xrightarrow{\partial}H^{q+1}(C^{*})\to\cdots $$ 

is exact, and such that given the homomorphism 5.16(7) of short exact sequences of cochain complexes, the diagram

 $$ \begin{array}{c}H^{e}(E^{*})\xrightarrow{\partial}H^{e+1}(C^{*})\\\downarrow\quad\downarrow\\H^{e}(\bar{E}^{*})\xrightarrow{\partial}H^{e+1}(\bar{C}^{*})\end{array} $$ 

commutes.

PROOF To define $\partial$, we consider the commutative diagram (4), where for convenience we have labeled particular homomorphisms. Let $\sigma$ be a cocycle in $E^q$. Since $\alpha$ is surjective, there is an element $\tilde{\sigma} \in D^q$ such that $\alpha(\tilde{\sigma}) = \sigma$. Since the square ① is commutative, and since $\sigma$ is a cocycle, it follows that $d(\tilde{\sigma})$ maps to zero in $E^{q+1}$; therefore.

<div style="text-align: center;"><div style="text-align: center;">(4)</div> </div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//dc498b61-2d7e-423e-ab90-cb990529f1dd/markdown_2/imgs/img_in_image_box_298_107_682_543.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A17Z%2F-1%2F%2Fda5bfba1215cf252159adb0c72b6948708961ac28a48eef430a4bc47321f106a" alt="Image" width="40%" /></div>


by the exactness of the horizontal sequences, $d(\tilde{\sigma})$ must be in the image of $\beta$. Thus there is an element $\sigma'\in C^{q+1}$ such that $\beta(\sigma')=d(\tilde{\sigma})$. It follows from the commutativity of the square $\textcircled{2}$, the injectivity of $\gamma$, and the fact that $d\circ d=0$ that $\sigma'$ is a cocycle. Now, $\sigma'$ is not uniquely determined by $\sigma$ because of the choice involved in the selection of $\tilde{\sigma}\in D^{q}$ such that $\alpha(\tilde{\sigma})=\sigma$. However, it is easily seen by a quick chase around the square $\textcircled{3}$ that $\sigma'$ is uniquely determined by $\sigma$ up to a cobondary. Thus we have a well-defined map

 $$ Z^{\mathfrak{q}}(E^{*})\to H^{\mathfrak{q}+1}(C^{*}), $$ 

which is easily seen to be a homomorphism. It is also readily seen that  $ B^{q}(E^{*}) $ is in the kernel of (5); hence (5) yields a homomorphism defined on the quotient  $ Z^{q}(E^{*})/B^{q}(E^{*}) $. This by definition is the desired homomorphism (1).

Checking the exactness of (2) involves checking exactness at  $ H^{q}(C^{*}) $, at  $ H^{q}(D^{*}) $, and at  $ H^{q}(E^{*}) $—and at each of these three stages we have to check two inclusion relations. These six steps in the proof of the exactness of (2) can be verified by simple chases around the diagram (4). We leave the details to the reader.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//dc498b61-2d7e-423e-ab90-cb990529f1dd/markdown_3/imgs/img_in_image_box_149_91_737_376.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A19Z%2F-1%2F%2Ff749877d446cb6d38372a9d51b199b3d8790de885d5bc1caf04403fbbb436b04" alt="Image" width="59%" /></div>


To prove (3), we have to follow some elements around the above commutative lattice.

We start with a cycicle $\sigma\in E^{q}$ and lift it back to $\tilde{\sigma}\in D^{q}$, which we map to $d(\tilde{\sigma})\in D^{q+1}$, which we have seen in the image of an element $\sigma'\in C^{q+1}$, which in turn we map to $\tilde{\sigma}'\in C^{q+1}$. Then $\tilde{\sigma}'$ is a cycicle in $C^{q+1}$ and is a representative of the cohomology class in $H^{q+1}(\tilde{C}^{*})$ into which the cohomology class of $\sigma$ in $H^{q}(E^{*})$ is mapped under the composition $H^{q}(E^{*})\xrightarrow{\partial}H^{q+1}(C^{*})\to H^{q+1}(\tilde{C}^{*})$. On the other hand, we can first map $\sigma$ to $\tilde{\sigma}\in E^{q}$, then lift back to $\tilde{\sigma}\in D^{q}$, map to $d(\tilde{\sigma})\in D^{q+1}$, and lift back to $\tilde{\sigma}'\in C^{q+1}$. Then $\tilde{\sigma}'$ is a cycicle in $C^{q+1}$ which represents the cohomology class in $H^{q+1}(\tilde{C}^{*})$ into which the cohomology class of $\sigma$ is mapped under the composition $H^{q}(E^{*})\to H^{q}(\tilde{E}^{*})\xrightarrow{\partial}H^{q+1}(\tilde{C}^{*})$. To prove (3), we need only check that $\tilde{\sigma}'-\tilde{\sigma}'$ is a cobondary. Now $\tilde{\sigma}\in D^{q}$ maps to an element $\tilde{\sigma}\in D^{q}$, and elements $\tilde{\sigma}$ and $\tilde{\sigma}$ of $D^{q}$ both map to $\tilde{\sigma}\in E^{q}$; hence there is an element $y\in C^{q}$ which maps to $(\tilde{\sigma}-\tilde{\sigma})$. One can easily check that $d\gamma=\tilde{\sigma}'-\tilde{\sigma}'$, which completes the proof of Proposition 5.17.

After a few trials the reader should find that these proofs by “diagram chase” become quite routine, albeit tedious. In the future we shall leave all such proofs as exercises.

##### AXIOMATIC SHEAF COHOMOLOGY

5.18 Definition A sheaf cohomology theory  $ \mathcal{H} $ for M with coefficients in sheaves of K-modules over M consists of

(I) a K-module  $ H^v(M,S) $ for each sheaf S and for each integer q,

(II) a homomorphism  $ H^q(M,\mathcal{S}) \to H^q(M,\mathcal{S}') $ for each homomorphism  $ \mathcal{S} \to \mathcal{S}' $ and for each integer  $ q $, and

(III) a homomorphism $H^{q}(M,\mathcal{S}^{\prime \prime}) \to H^{q+1}(M,\mathcal{S}^{\prime})$ for each short exact sequence $0 \to \mathcal{S}^{\prime} \to \mathcal{S} \to \mathcal{S}^{\prime \prime} \to 0$ and for each integer $q$,

such that the properties (a)–(f) hold:

(a)  $ H^{q}(M,S) = 0 $ for q < 0, and there is an isomorphism  $ H^{q}(M,S) \cong \Gamma(S) $ such that for each homomorphism  $ S \to S' $ the diagram

 $$ \begin{array}{c}H^{a}(M,\mathcal{S})\cong\Gamma(\mathcal{S})\\\downarrow\quad\downarrow\\H^{0}(M,\mathcal{S}^{\prime})\cong\Gamma(\mathcal{S}^{\prime})\end{array} $$ 

commutes.

(b)  $ H^{q}(M,\mathcal{S}) = 0 $ for all q > 0 if  $ \mathcal{S} $ is a fine sheaf.

(c) If  $ 0 \to S' \to S \to S'' \to 0 $ is exact, then the following is exact:

 $$ \cdots\to H^{q}(M,\mathcal{S}^{\prime})\to H^{q}(M,\mathcal{S})\to H^{q}(M,\mathcal{S}^{\prime \prime})\to H^{q+1}(M,\mathcal{S}^{\prime})\to\cdots. $$ 

(d) The identity homomorphism id: $\mathcal{S} \to \mathcal{S}$ induces the identity homomorphism id: $H^{q}(M,\mathcal{S}) \to H^{q}(M,\mathcal{S})$.

(e) If the diagram

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//71ded3ce-5c12-4e33-bb28-7ddb7c86f435/markdown_0/imgs/img_in_image_box_402_562_590_681.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A15Z%2F-1%2F%2F9e9b85e9aaf0906366a0b3814fd92156498e167f241a1f68479d91e604cc3789" alt="Image" width="19%" /></div>


commutes, then for each $q$ so does the diagram

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//71ded3ce-5c12-4e33-bb28-7ddb7c86f435/markdown_0/imgs/img_in_image_box_331_726_654_853.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A15Z%2F-1%2F%2Fec589a84b46d1d8428ce7c8f126d05cea92783acebc49c1538804a4d7749f090" alt="Image" width="33%" /></div>


(f) For each homomorphism of short exact sequences of sheaves

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//71ded3ce-5c12-4e33-bb28-7ddb7c86f435/markdown_0/imgs/img_in_image_box_318_892_667_991.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A15Z%2F-1%2F%2F40929dd777c4d5572b3fed2e56899e4120a584b651183cbfceb23a72a0e5a01d" alt="Image" width="36%" /></div>


the following diagram commutes:

 $$ \begin{matrix}{H^{q}(M,\mathcal{S}^{\prime\prime})\to H^{q+1}(M,\mathcal{S}^{\prime})}\\ {\downarrow\quad\downarrow}\\ {H^{q}(M,\mathcal{T}^{\prime\prime})\to H^{q+1}(M,\mathcal{T}^{\prime}).}\\ \end{matrix} $$ 

The module $H^{q}(M,S)$ is called the $q$th cohomology module of $M$ with coefficients in the sheaf $S$ relative to the cohomology theory $\mathcal{H}$.

### 5.19 Definition An exact sheaf sequence

 $$ 0\to\mathcal{A}\to\mathcal{C}_{0}\to\mathcal{C}_{1}\to\mathcal{C}_{2}\to\cdots $$ 

is called a resolution of the sheaf A. The resolution (1) is called fine (respectively torsionless) if each of the sheaves  $ C_{t} $ is fine (respectively torsionless).

With each resolution (1) of  $ \mathcal{S} $ and each sheaf  $ \mathcal{S} $ we associate a cochain complex

 $$ \cdots\to0\to\Gamma(\mathcal{C}_{0}\otimes\mathcal{S})\to\Gamma(\mathcal{C}_{1}\otimes\mathcal{S})\to\Gamma(\mathcal{C}_{2}\otimes\mathcal{S})\to\cdots $$ 

which we shall denote by $\Gamma(\mathcal{C}^*\otimes\mathcal{S})$. For $q\geq0$ the module of $q$-cochains is $\Gamma(\mathcal{C}_q\otimes\mathcal{S})$, whereas for $q<0$ the module of $q$-cochains is the zero module. Note carefully that this cochain complex does not contain the module $\Gamma(\mathcal{A}\otimes\mathcal{S})$. The homomorphisms in (2) are those induced by the homomorphisms $\mathcal{C}_i\otimes\mathcal{S}\to\mathcal{C}_{i+1}\otimes\mathcal{S}$ which are the tensor product of the homomorphisms of (1) with id: $\mathcal{S}\to\mathcal{S}$. The exactness of (1) implies that in

 $$ \cdots\to0\to\mathcal{C}_{0}\otimes\mathcal{S}\to\mathcal{C}_{1}\otimes\mathcal{S}\to\mathcal{C}_{2}\otimes\mathcal{S}\to\cdots $$ 

the image of each homomorphism is contained in the kernel of the next, and this in turn implies that (2) is indeed a cochain complex.

A homomorphism $\mathcal{S} \to \mathcal{S}'$ when tensored with the identity homomorphisms of the sheaves $\mathcal{C}_i$ yields homomorphisms $\mathcal{C}_i \otimes \mathcal{S} \to \mathcal{C}_i \otimes \mathcal{S}'$. These, in turn, induce homomorphisms $\Gamma(\mathcal{C}_i \otimes \mathcal{S}) \to \Gamma(\mathcal{C}_i \otimes \mathcal{S}')$, which commute with the coboundary homomorphisms of the respective cochain complexes and thus determine a cochain map

 $$ \Gamma(\mathcal{C}^{*}\otimes\mathcal{S})\to\Gamma(\mathcal{C}^{*}\otimes\mathcal{S}^{\prime}). $$ 

5.20 Existence of Cohomology Theories We shall now show that each fine torsionless resolution of the constant sheaf  $ \mathscr{K} = M \times K $,

 $$ 0\to\mathcal{H}\to\mathcal{C}_{0}\to\mathcal{C}_{1}\to\mathcal{C}_{2}\to\cdots, $$ 

canonically determines a cohomology theory for $M$ with coefficients in sheaves of $K$-modules over $M$. The existence of such resolutions will be amply demonstrated in the later sections in which the classical cohomology theories are discussed. In particular, see 5.26(7) and (11). We therefore assume that we are given a fine torsionless resolution (1). Then we obtain a cohomology theory as follows:

(I) With a sheaf S and each integer q we associate the qth cohomology module of the cochain complex  $ \Gamma(\mathcal{C}^* \otimes \mathcal{S}) $; that is, we set

 $$ H^{q}(M,\mathcal{S})=H^{q}\big(\Gamma(\mathcal{C}^{\ast}\otimes\mathcal{S})\big). $$ 

(II) With each homomorphism $\mathcal{S}\to\mathcal{S}^{\prime}$ and each integer $q$ we associate the homomorphism $H^{q}(M,\mathcal{S})\to H^{q}(M,\mathcal{S}^{\prime})$ induced, according to 5.16(4), by the cochain map $\Gamma(\mathcal{C}^{*}\otimes\mathcal{S})\to\Gamma(\mathcal{C}^{*}\otimes\mathcal{S}^{\prime})$ of 5.19(4).

(III) Each short exact sheaf sequence

 $$ 0\to\mathcal{S}^{\prime}\to\mathcal{S}\to\mathcal{S}^{\prime \prime}\to0 $$ 

induces, in view of Theorem 5.15 and the fact that the  $ \mathcal{C}_{t} $ are fine torsionless sheaves, a short exact sequence of cochain maps

 $$ 0\to\Gamma(\mathcal{C}^{*}\otimes\mathcal{S}^{\prime})\to\Gamma(\mathcal{C}^{*}\otimes\mathcal{S})\to\Gamma(\mathcal{C}^{*}\otimes\mathcal{S}^{\prime\prime})\to0 $$ 

with which, according to 5.17(1), there is associated a homomorphism  $ H^{q}(\Gamma(\mathcal{C}^*\otimes\mathcal{S}^*))\to H^{q+1}(\Gamma(\mathcal{C}^*\otimes\mathcal{S}^*)) $. This, by definition, is the homomorphism  $ H^{q}(M,\mathcal{S}^*) \to H^{q+1}(M,\mathcal{S}^*) $ that we associate with the short exact sequence  $ 0\to\mathcal{S}^*\to\mathcal{S}\to\mathcal{S}^*\to0 $ and the integer  $ q $.

The fact that axiom 5.18(d) for a cohomology theory is satisfied is immediately apparent. The remark immediately following 5.16(4) implies that axiom (e) is satisfied. Axioms (c) and (f) are consequences of 5.17.

Now let $\mathcal{L}_{q}$ be the kernel of $\mathcal{C}_{q}\to\mathcal{C}_{e+1}$. Then it follows from the exactness of (1) that

 $$ 0\to\mathcal{L}_{a}\to\mathcal{C}_{a}\to\mathcal{L}_{a+1}\to0 $$ 

is exact; and since $\mathcal{L}_{q}$ is a subsheaf of the torsionless sheaf $\mathcal{C}_{q}$, then $\mathcal{L}_{q}$ is also torsionless. It follows from Theorem 5.15 that for any sheaf $S$ the sequence

 $$ 0\to\mathcal{X}_{q}\otimes\mathcal{S}\to\mathcal{C}_{q}\otimes\mathcal{S}\to\mathcal{X}_{q+1}\otimes\mathcal{S}\to0 $$ 

is exact; and from (3) and 5.11(2) we obtain the exact sequence

 $$ 0\to\Gamma(\mathcal{L}_{q}\otimes\mathcal{S})\to\Gamma(\mathcal{C}_{q}\otimes\mathcal{S})\to\Gamma(\mathcal{L}_{q+1}\otimes\mathcal{S}). $$ 

In particular,  $ \Gamma(\mathcal{L}_q \otimes \mathcal{S}) \to \Gamma(\mathcal{C}_q \otimes \mathcal{S}) $ is an injection, so since the homomorphism

 $$ \Gamma(\mathcal{C}_{q}\otimes\mathcal{S})\to\Gamma(\mathcal{C}_{q+1}\otimes\mathcal{S}) $$ 

is the composition

 $$ \Gamma(\mathcal{C}_{q}\otimes\mathcal{S})\to\Gamma(\mathcal{Z}_{q+1}\otimes\mathcal{S})\to\Gamma(\mathcal{C}_{q+1}\otimes\mathcal{S}), $$ 

it follows from (4) that the kernel of (5) is simply the submodule  $ \Gamma(\mathcal{L}_q \otimes S) $ of  $ \Gamma(\mathcal{L}_q \otimes S) $. Thus for  $ q \geq 0 $,

 $$ H^{q}(M,\mathcal{S})=H^{q}\big(\Gamma(\mathcal{C}*\otimes\mathcal{S})\big)=\Gamma(\mathcal{Z}_{q}\otimes\mathcal{S})/\operatorname{I m}\big(\Gamma(\mathcal{C}_{q-1}\otimes\mathcal{S})\big). $$ 

Now, if § happens to be a fine sheaf, then according to Theorem 5.15 the full sequence

 $$ 0\to\Gamma(\mathcal{L}_{q-1}\otimes\mathcal{S})\to\Gamma(\mathcal{C}_{q-1}\otimes\mathcal{S})\to\Gamma(\mathcal{L}_{q}\otimes\mathcal{S})\to0 $$ 

is exact; and (8) together with (7) implies that

 $$ H^{q}(M,\mathcal{S})=0\quad\mathrm{f o r}\;q>0. $$ 

Thus axiom (b) is satisfied.

Finally, it is evident that  $ H^{v}(M,S) = 0 $ for q < 0, and for q = 0 the isomorphism

 $$ \mathcal{N}\to\mathcal{L}_{0}\subset\mathcal{C}_{0} $$ 

induces, for an arbitrary sheaf S, an isomorphism

 $$ \mathcal{S}\cong\mathcal{H}\otimes\mathcal{S}\xrightarrow{\cong}\mathcal{D}_{0}\otimes\mathcal{S} $$ 

and thus an isomorphism

 $$ \Gamma(\mathcal{S})\xrightarrow{\simeq}\Gamma(\mathcal{D}_{\mathfrak{g}}\otimes\mathcal{S})=H^{\mathfrak{g}}(M,\mathcal{S}), $$ 

which clearly satisfies

 $$ \begin{array}{c}\Gamma(\mathcal{S})\cong H^{0}(M,\mathcal{S})\\\downarrow\quad\downarrow\\\Gamma(\mathcal{S}^{\prime})\cong H^{0}(M,\mathcal{S}^{\prime})\end{array} $$ 

for each homomorphism  $ \mathcal{S} \to \mathcal{S}' $. Thus axiom (a) is satisfied.

5.21 Definition Let $\mathcal{H}$ and $\mathcal{H}$ be two sheaf cohomology theories on $M$ with coefficients in sheaves of $K$-modules over $M$. A homomorphism of the cohomology theory $\mathcal{H}$ to the theory $\tilde{\mathcal{H}}$ consists of a homomorphism

 $$ H^{a}(M,\mathcal{S})\to\tilde{H}^{a}(M,\mathcal{S}) $$ 

for each sheaf S and for each integer q, such that the following conditions hold:

(a) For q = 0, the diagram

 $$ \begin{array}{c}H^{0}(M,\mathbb{S})\cong\Gamma(\mathbb{S})\\\downarrow\quad\downarrow\\\tilde{H}^{0}(M,\mathbb{S})\cong\Gamma(\mathbb{S})\end{array} $$ 

commutes.

(b) For each homomorphism  $ \mathcal{S} \to \mathcal{T} $ and each integer  $ q $ the diagram

 $$ \begin{matrix}{H^{q}(M,\mathcal{S})\to H^{q}(M,\mathcal{T})}\\ {\downarrow\quad\downarrow}\\ {\tilde{H}^{q}(M,\mathcal{S})\to\tilde{H}^{q}(M,\mathcal{T})}\\ \end{matrix} $$ 

commutes.

(c) For each short exact sequence of sheaves

 $$ 0\to\mathcal{R}\to\mathcal{S}\to\mathcal{T}\to0 $$ 

the following diagram commutes for each integer $q$:

 $$ \begin{array}{c}H^{a}(M_{r}\mathcal{T})\xrightarrow{\partial}H^{a+1}(M,\mathcal{R})\\\downarrow\quad\downarrow\\\tilde{H}^{a}(M_{r}\mathcal{T})\xrightarrow{\partial}\tilde{H}^{a+1}(M,\mathcal{R}).\end{array} $$ 

An isomorphism $\mathcal{H}\to\tilde{\mathcal{H}}$ is a homomorphism in which each of the homomorphisms $H^{q}(M,\mathcal{S})\to\tilde{H}^{q}(M,\mathcal{S})$ are isomorphismisms. The identity $\operatorname{homomorphism of}\mathcal{H}$ with itself is the $\operatorname{homomorphism}\mathcal{H}\to\mathcal{H}$ which assigns the identity $\operatorname{homomorphism}H^{q}(M,\mathcal{S})\to H^{q}(M,\mathcal{S})$ to each sheaf $\mathcal{S}$ and each integer $q$.

We are now going to prove that there is a unique homomorphism between any two sheaf cohomology theories on $M$. However, first we need to introduce the notion of the sheaf of germs of discontinuous sections of a sheaf $S$.

5.22 The Sheaf of Germs of Discontinuous Sections of 8 Let 8 be a sheaf on $M$. By a discontinuous section of 8 over the open set $U \subset M$ we mean any map $f: U \to 8$, continuous or not, such that $\pi \circ f = \mathrm{id}$. The assignment to each open set $U \subset M$ of the module of all discontinuous sections of 8 over $U$ yields a presheaf whose associated sheaf $8_0$ is called the sheaf of germs of discontinuous sections of 8.

The important property of $\delta_{0}$ that we shall need is that $\delta_{0}$ is always a fine sheaf. For let $\{U_{i}\}$ be a locally finite open cover of $M$. Choose a refinement $\{V_{i}\}$ such that $\overline{V}_{i} \subset U_{i}$ for each $i$ (Exercise 3, Chapter 1). (For such a refinement on a general paracompact Hausdorff space, see [13, Ch. 5, Problem V(a)].) Associate with each point of $M$ a set $V_{i}$ containing it, and then for each $i$ define a function $\varphi_{i}$ on $M$ to have the value 1 at all points associated with $V_{i}$ and to have the value 0 elsewhere. It follows that $\operatorname{supp} \varphi_{i} \subset U_{i}$ and $\sum \varphi_{i} \equiv 1$. We associate with $\varphi_{i}$ an endomorphism $\widetilde{I}_{i}$ of the presheaf of discontinuous sections of 8 by defining

 $$ \tilde{l}_{i}(s)(m)=\varphi_{i}(m)s(m) $$ 

for each discontinuous section $s$ of $\mathcal{S}$ over an open set $U \subset M$ and each $m \in U$. The presheaf endomorphisms $\widetilde{I}_{i}$ induce endomorphisms $I_{i}$ of the sheaf $\mathcal{S}_{0}$ of germs of discontinuous sections of $\mathcal{S}$. It is immediate that the $\{I_{i}\}$ forms a partition of unity of $\mathcal{S}_{0}$ subordinate to the locally finite cover $\{U_{i}\}$ of $M$. Thus $\mathcal{S}_{0}$ is a fine sheaf, as claimed.

There is a natural injection of $\mathcal{S}$ into $\mathcal{S}_0$; namely, each element of the stalk $\mathcal{S}_m$ is the value at $m$ of a (continuous) section $s$ of $\mathcal{S}$ defined on some neighborhood of $m$, and we map $s(m)$ to the germ of $s$ at $m$ in $\mathcal{S}_0$. If we let $\overline{\mathcal{S}}$ denote the quotient sheaf $\mathcal{S}_0/\mathcal{S}$, then for each sheaf $\mathcal{S}$ we have constructed a short exact sequence

 $$ 0\to\mathcal{S}\to\mathcal{S}_{0}\to\overline{{\mathcal{S}}}\to0 $$ 

in which the middle sheaf is fine.

5.23 Theorem Let $\mathcal{H}$ and $\tilde{\mathcal{H}}$ be cohomologytheories on $M$ with coefficients in sheaves of $K$-modules over $M$. Then there exists a unique homomorphism of $\mathcal{H}$ to $\tilde{\mathcal{H}}$.

PROOF We first prove uniqueness. Suppose that we have a homomorphism of $\mathcal{H}$ to $\tilde{\mathcal{H}}$, and let a sheaf $\delta$ be given. Then it follows from the axioms 5.18 and 5.21 applied to the exact sequence 5.22(2), in which, you recall, the sheaf $\delta_{0}$ is fine, that we have a commutative diagram

 $$ \begin{array}{c}\Gamma(\mathcal{S}_{0})\rightarrow\Gamma(\overline{\mathcal{S}})\rightarrow H^{1}(M,\mathcal{S})\rightarrow0\\\downarrow\mathrm{id}\quad\downarrow\mathrm{id}\quad\downarrow\\\Gamma(\mathcal{S}_{0})\rightarrow\Gamma(\overline{\mathcal{S}})\rightarrow\tilde{H}^{1}(M,\mathcal{S})\rightarrow0;\end{array} $$ 

and for each $q \geq 2$ we have a commutative diagram

 $$ \begin{array}{c}0\to H^{q-1}(M,\overline{\delta})\to H^{q}(M,\mathcal{S})\to0\\\downarrow\quad\downarrow\\0\to\widetilde{H}^{q-1}(M,\overline{\mathcal{S}})\to\widetilde{H}^{q}(M,\mathcal{S})\to0.\end{array} $$ 

Note that in both (1) and (2) the rows are exact. Now uniqueness of the homomorphisms 5.21(1) follows for $q=0$ from 5.21(a), follows for $q=1$ from (1), and follows inductively for $q>1$ from (2).

We now show the existence of a homomorphism of the theory $\mathcal{H}$ to the theory $\widetilde{\mathcal{H}}$. We define the homomorphisms for $q=0$ by $5.21(a)$, and it follows immediately that $5.21(b)$ is satisfied for the case $q=0$. We define the homomorphisms $5.21(1)$ for $q=1$ by (1), and inductively for $q>1$ by (2). To prove that this indeed defines a homomorphism of $\mathcal{H}$ to $\widetilde{\mathcal{H}}$, it remains to show that $5.21(b)$ holds for $q>0$ and that $5.21(c)$ holds for all $q$.

Now, 5.21(b) follows for $q = 1$ from the following lattice constructed from two copies of (1):

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//30eac8e9-d4a5-4702-ba3c-6089ed089fb7/markdown_1/imgs/img_in_image_box_275_806_659_1038.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A15Z%2F-1%2F%2Ffdbcc3e7f428dbcec0b9fb5e52ae3d4b37bdf86d65e3135de4b7dda645bb518e" alt="Image" width="39%" /></div>


In the lattice, the commutativity of the right-hand face ① is forced by the apriori commutativity of all the other faces, and 5.21(b) follows inductively for $q>1$ from the analogous lattice constructed from (2).

As for 5.21(c), suppose that a short exact sequence

(4)

 $$ 0\to\mathcal{R}\to\mathcal{S}\to\mathcal{T}\to0 $$ 

is given. Let $\mathcal{R}_{0}$ and $\mathcal{S}_{0}$ be the sheaves of germs of discontinuous sections of $\mathcal{R}$ and $\mathcal{S}$ respectively. The composition $\mathcal{R}\to\mathcal{S}\to\mathcal{S}_{0}$ is an injection of $\mathcal{R}$ into $\mathcal{S}_{0}$; let $\mathcal{G}$ be the quotient sheaf $\mathcal{S}_{0}/\mathcal{R}$. As in 5.22, let $\overline{\mathcal{R}}=\mathcal{R}_{0}/\mathcal{R}$. Then there are uniquely determined homomorphisms $\mathcal{T}\to\mathcal{G}$ and $\overline{\mathcal{R}}\to\mathcal{G}$ such that the following diagram, in which the rows are exact, commutes:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//30eac8e9-d4a5-4702-ba3c-6089ed089fb7/markdown_2/imgs/img_in_image_box_334_348_672_518.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A15Z%2F-1%2F%2Fdf14e75b3a3b611a9b5f337939d2c819f75c38e80d9fe1765c376afd9eb2add5" alt="Image" width="35%" /></div>


It follows from the cohomology axioms 5.18 applied to (5) that there are commutative diagrams

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//30eac8e9-d4a5-4702-ba3c-6089ed089fb7/markdown_2/imgs/img_in_image_box_256_584_747_756.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A15Z%2F-1%2F%2Fd9a1359f88a120b4515aa00b07e85fbabcf769ef78eb73cbe7b3b548b89970f8" alt="Image" width="51%" /></div>


and (for  $ q \geq 1 $)

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//30eac8e9-d4a5-4702-ba3c-6089ed089fb7/markdown_2/imgs/img_in_image_box_210_796_773_983.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A15Z%2F-1%2F%2Fede52ed29f631db4dd0d224c9508c9d3c72ba190035f06db2434106040759005" alt="Image" width="59%" /></div>


It follows from (6) that the homomorphism  $ H^{0}(M,\mathcal{T}) \to H^{1}(M,\mathcal{R}) $ is the composition

(8)  $ H^0(M,\mathcal{T}) \xrightarrow{\cong} \Gamma(\mathcal{T}) \to \Gamma(\mathcal{G})/\mathrm{Im}\Gamma(\mathcal{S}_0) \xleftarrow{\cong} \Gamma(\overline{\mathcal{R}})/\mathrm{Im}\Gamma(\mathcal{R}_0) \xrightarrow{\cong} H^1(M,\mathcal{R}) $ and it follows from (7) that the homomorphism  $ H^0(M,\mathcal{T}) \to H^{\mathbb{V}+1}(M,\mathcal{R}) $ for  $ q \geq 1 $ is the composition

 $$ H^{q}(M,\mathcal{T})\to H^{q}(M,\mathcal{G})\xleftarrow{\cong}H^{q}(M,\bar{\mathcal{R}})\xrightarrow{\cong}H^{q+1}(M,\mathcal{R}). $$ 

From (8) and the corresponding sequence for the $\tilde{\mathcal{H}}$ theory we obtain the diagram

 $$ \begin{array}{c c}{H^{0}(M,\mathcal{T})\xrightarrow{\cong}\Gamma(\mathcal{T})\to\Gamma(\mathcal{G})/\operatorname{I m}\Gamma(\mathcal{S}_{0})\xleftarrow{\cong}\Gamma(\bar{\mathcal{R}})/\operatorname{I m}\Gamma(\mathcal{R}_{0})\xrightarrow{\cong}H^{1}(M,\mathcal{R})}\\ {(10)\Big\downarrow\Big\downarrow\big\downarrow\operatorname{i d}\Big\downarrow\big\downarrow\operatorname{i d}\Big\downarrow\big\downarrow\operatorname{i d}\Big\downarrow\big\downarrow}\\ {\tilde{H}^{0}(M,\mathcal{T})\xrightarrow{\cong}\Gamma(\mathcal{T})\to\Gamma(\mathcal{G})/\operatorname{I m}\Gamma(\mathcal{S}_{0})\xleftarrow{\cong}\Gamma(\bar{\mathcal{R}})/\operatorname{I m}\Gamma(\mathcal{R}_{0})\xrightarrow{\cong}\tilde{H}^{1}(M,\mathcal{R})}\\ \end{array} $$ 

in which the first and last squares commute by the definitions of the homomorphisms $H^{0}(M,\mathcal{T})\to\tilde{H}^{0}(M,\mathcal{T})$ and $H^{1}(M,\mathcal{R})\to\tilde{H}^{1}(M,\mathcal{R})$, and the middle two squares trivially commute. Thus 5.21(c) is proved for $q=0$. From (9) and the corresponding sequence for the $\tilde{\mathcal{H}}$ theory we obtain the diagram

 $$ \begin{array}{c}\boldsymbol{H}^{q}(\boldsymbol{M},\mathcal{T})\rightarrow\boldsymbol{H}^{q}(\boldsymbol{M},\mathcal{G})\xleftarrow{\cong}\boldsymbol{H}^{q}(\boldsymbol{M},\widetilde{\mathcal{R}})\xrightarrow{\cong}\boldsymbol{H}^{q+1}(\boldsymbol{M},\mathcal{R})\\\downarrow\quad\downarrow\quad\downarrow\quad\downarrow\quad\downarrow\\\widetilde{\boldsymbol{H}}^{q}(\boldsymbol{M},\mathcal{T})\rightarrow\widetilde{\boldsymbol{H}}^{q}(\boldsymbol{M},\mathcal{G})\xleftarrow{\cong}\widetilde{\boldsymbol{H}}^{q}(\boldsymbol{M},\widetilde{\mathcal{R}})\xrightarrow{\cong}\widetilde{\boldsymbol{H}}^{q+1}(\boldsymbol{M},\mathcal{R})\end{array} $$ 

in which the last square commutes by definition of the homomorphism  $ H^{q+1}(M,\mathcal{R}) \to \tilde{H}^{q+1}(M,\mathcal{R}) $, and the first two squares commute by 5.21(b). Thus 5.21(c) follows for  $ q \geq 1 $, and the proof of Theorem 5.23 is complete.

Corollary A homomorphism of the cohomology theory $\mathcal{H}$ to the theory $\tilde{\mathcal{H}}$ must necessarily be an isomorphism. Consequently, any two cohomology theories on $M$ with coefficients in sheaves of $K$-modules over $M$ are uniquely isomorphic.

PROOF Assume that a homomorphism $\mathcal{H}\to\tilde{\mathcal{H}}$ is given. By Theorem 5.23 there must also exist a homomorphism $\tilde{\mathcal{H}}\to\mathcal{H}$. The composition $\mathcal{H}\to\tilde{\mathcal{H}}\to\mathcal{H}$ must necessarily, by uniqueness, be the identity homomorphism of $\mathcal{H}$, and similarly the composition $\tilde{\mathcal{H}}\to\mathcal{H}\to\tilde{\mathcal{H}}$ must be the identity homomorphism of $\tilde{\mathcal{H}}$. It follows that the homomorphisms $\mathcal{H}\to\tilde{\mathcal{H}}$ and $\tilde{\mathcal{H}}\to\mathcal{H}$ are both isomorphisms.

### 5.24 Assume that

 $$ \begin{array}{c}0\to\mathcal{H}\to\mathcal{C}_{0}\to\mathcal{C}_{1}\to\mathcal{C}_{\mathfrak{z}}\to\cdots\\\downarrow\downarrow\downarrow\downarrow\downarrow\downarrow\\\downarrow\downarrow\downarrow\downarrow\downarrow\downarrow\\0\to\mathcal{H}\to\widetilde{\mathcal{C}}_{0}\to\widetilde{\mathcal{C}}_{1}\to\widetilde{\mathcal{C}}_{\mathfrak{z}}\to\cdots\end{array} $$ 

is a commutative diagram in which the rows are fine torsionless resolutions of the constant sheaf $\mathcal{H}$. We have seen in 5.20 that each of these resolutions determines a cohomology theory. Denote the cohomology theory obtained from the top resolution by $\mathcal{H}$ and that obtained from the second resolution by $\tilde{\mathcal{H}}$. We claim that the “homomorphism” (1) between these two fine torsionless resolutions canonically induces a homomorphism, and therefore,

by the corollary of 5.23, induces an isomorphism, $\mathcal{H} \to \tilde{\mathcal{H}}$. For each sheaf $\delta$, (1) induces a cochain map $\Gamma(\mathcal{C}^* \otimes \delta) \to \Gamma(\mathcal{C}^* \otimes \delta)$ from which we obtain a homomorphism $H^q(M,\delta) \to \tilde{H}^q(M,\delta)$ for each integer $q$. That the axioms 5.21(a), (b), and (c) for a homomorphism of cohomology theories are satisfied is easily demonstrated and will be left to the reader as an exercise. This procedure for obtaining a homomorphism of cohomology theories will be used in 5.36 to obtain an explicit isomorphism of the de Rham and differentiable singular cohomology theories for a differentiable manifold $M$.

5.25 Theorem Assume that $\mathcal{H}$ is a cohomology theory for $M$ with coefficients in sheaves of $K$-modules over $M$. Let

 $$ 0\to\mathcal{S}\to\mathcal{C}_{0}\to\mathcal{C}_{1}\to\mathcal{C}_{2}\to\cdots $$ 

be a fine resolution of the sheaf 8. Then there are canonical isomorphisms

 $$ H^{\mathfrak{q}}(M,\mathcal{S})\cong H^{\mathfrak{q}}\bigl(\Gamma(\mathcal{C}^{*})\bigr)\quad{f o r\quad a l l}\;q. $$ 

PROOF From the exactness of (1) it follows that $0 \to \Gamma(\mathcal{S}) \to \Gamma(\mathcal{C}_0) \to \Gamma(\mathcal{C}_1)$ is exact, whence $H^0(M,\mathcal{S}) \cong \Gamma(\mathcal{S}) \cong H^0\left(\Gamma(\mathcal{C}^*)\right)$. Now let $\mathcal{H}_e$ be the kernel of $\mathcal{C}_e \to \mathcal{C}_{e+1}$ for $q \geq 1$. Then the exactness of (1) implies that

 $$ 0\to\mathcal{H}_{a}\to\mathcal{C}_{a}\to\mathcal{H}_{a+1}\to0 $$ 

is exact for  $ q \geq 1 $, and that

 $$ 0\to\mathcal{S}\to\mathcal{C}_{0}\to\mathcal{H}_{1}\to0 $$ 

is exact. It follows from the long exact cohomology sequence for (4) and from the fact that  $ \mathcal{C}_{0} $ is a fine sheaf that

 $$ H^{q}(M,\mathcal{S})\cong H^{q-1}(M,\mathcal{H}_{1})\quad\mathrm{f o r}\;q>1 $$ 

and

 $$ H^{\mathrm{1}}(M,\mathcal{S})\cong\Gamma(\mathcal{H}_{1})/\operatorname{I m}\Gamma(\mathcal{C}_{0})\cong H^{\mathrm{1}}\big(\Gamma(\mathcal{C}^{*})\big). $$ 

By repeated application of the long exact sequence associated with (3) and of the fact that the sheaves  $ \mathcal{C}_i $ are fine, we obtain for  $ q > 1 $

 $$ \begin{aligned}{H^{q}(M,\mathcal{S})}&{{}\cong H^{q-1}(M,\mathcal{H}_{1})\cong H^{q-2}(M,\mathcal{H}_{2})\cong\cdots\cong H^{1}(M,\mathcal{H}_{q-1})}\\ {}&{{}\cong\Gamma(\mathcal{H}_{q})/\operatorname{I m}\Gamma(\mathcal{C}_{q-1})\cong H^{q}\bigl(\Gamma(\mathcal{C}^{*})\bigr).}\\ \end{aligned} $$ 

This completes our development of axiomatic sheaf cohomology except for the multiplicative structure, which is discussed in 5.42. We shall now consider four sheaf cohomology theories for a differentiable manifold $M$-the Alexander-Spanier, de Rham, singular, and Czech. In view of the corollary of 5.23, these theories will be uniquely isomorphic. We shall also define the classical versions of these theories, and prove that they are canonically isomorphic with sheaf cohomology with coefficients in constant sheaves.

##### THE CLASSICAL COHOMOLOGY THEORIES

##### Alexander-Spanier Cohomology

5.26 For the Alexander-Spanier theory, $M$ need only be a paracompact Hausdorff space. Let $U \subset M$ be open, and as usual let $K$ be a fixed principal ideal domain. We use $U^{p+1}$ to denote the $(p+1)$ fold cartesian product of $U$ with itself. Let $A^p(U,K)$ denote the $K$-module of functions $U^{p+1} \to K$ under pointwise addition. For each $p \geq 0$ we define a homomorphism

 $$ d\colon A^{\mathfrak{g}}(U,K)\to A^{\mathfrak{g}+1}(U,K) $$ 

by setting

 $$ df(m_{0},\ldots,m_{p+1})=\sum_{i=0}^{p+1}(-1)^{i}f(m_{0},\ldots,\widehat{m_{i}},\ldots,m_{p+1}) $$ 

for each $f \in A^p(U,K)$ and $(m_0, \ldots, m_{p+1}) \in U^{p+1}$, where $\neg$ over an entry means that entry is to be omitted. It is a straightforward exercise to check that $d \circ d = 0$, so for each $U \subset M$ we have a cochain complex

 $$ \cdots\to0\to A^{0}(U,K)\xrightarrow{d}A^{1}(U,K)\xrightarrow{d}A^{\sharp}(U,K)\xrightarrow{d}\cdots $$ 

which we shall denote by $A^{*}(U,K)$, and in which the modules of $q$-cochains for $q<0$ are all assumed to be zero modules. If $V\subset U$, then $V^{p+1}\subset U^{p+1}$, and there is a corresponding restriction homomorphism

 $$ \rho_{V,U}\colon A^{\mathfrak{p}}(U,K)\to A^{\mathfrak{p}}(V,K). $$ 

The collection

 $$ \left\{A^{p}(U,K);\rho_{U,V}\right\} $$ 

forms a presheaf of K-modules on $M$ called the presheaf of Alexander-Spanier $p$-cochains. Observe that these presheaves satisfy $5.7(C_{2})$, but for $p\geq1$ do not satisfy $5.7(C_{1})$.

The associated sheaf of germs of Alexander-Spanier $p$-cochains we denote by $\mathcal{A}^{p}(M,K)$. The homomorphisms $d$ give presheaf homomorphisms $\{A^{p}(U,K);\rho_{U,V}\}\to\{A^{p+1}(U,K);\rho_{U,V}\}$ for each $p\geq0$, and induce sheaf homomorphisms (which we shall denote by the same symbol $d$):

 $$ d\colon\mathcal{A}^{\mathfrak{p}}(M,K)\to\mathcal{A}^{\mathfrak{p}+1}(M,K)\qquad(p\geq0). $$ 

These homomorphisms, together with the natural injection of the constant sheaf $\mathcal{H} \to \mathcal{A}^0(M,K)$ which sends $k \in \mathcal{H}_m$ to the germ of the constant function $k$ at $m$, give us a sequence

 $$ 0\to\mathcal{H}\to\mathcal{A}^{0}(M,K)\xrightarrow{d}\mathcal{A}^{1}(M,K)\xrightarrow{d}\mathcal{A}^{2}(M,K)\xrightarrow{d}\cdots. $$ 

We claim that (7) is a fine torsionless resolution of the constant sheaf  $ \mathcal{X} $. The elements of  $ \mathcal{A}^{\varphi}(M,K) $ are equivalence classes of functions with values in  $ K $, and  $ K $ is an integral domain; hence  $ \mathcal{A}^{\varphi}(M,K) $ is torsionless. To prove that  $ \mathcal{A}^{\varphi}(M,K) $ is a fine sheaf, let  $ \{U_t\} $ be a locally finite open cover of  $ M $, and take (as in 5.22) a partition of unity  $ \{\varphi_t\} $ subordinate to the cover  $ \{U_t\} $ in which the functions  $ \varphi_t $ take values 0 or 1 only. For each  $ t $ we define an endomorphism  $ \tilde{l}_t $ of  $ A^{\varphi}(U,K) $ by setting

 $$ \tilde{I}_{i}(f)(m_{0},\ldots,m_{p})=\varphi_{i}(m_{0})f(m_{0},\ldots,m_{p}). $$ 

The endomorphisms  $ \widetilde{l}_t $ commute with restrictions and thus determine presheaf endomorphisms of  $ \{A^p(U,K): \rho_{U,V}\} $. Let  $ l_t: \mathcal{A}^p(M,K) \to \mathcal{A}^p(M,K) $ be the sheaf endomorphism associated with  $ \widetilde{l}_t $. Then it follows readily that  $ \supset p l_t \subset U_t $ and that  $ \sum l_t \equiv 1 $. Thus the sheaves  $ \mathcal{A}^p(M,K) $ are fine. The exactness of (7) follows directly from the fact that we have exactness on the presheaf level. That is, if  $ U \subset M $ is open, then

 $$ 0\to K\to A^{0}(U,K)\xrightarrow{d}A^{1}(U,K)\xrightarrow{d}A^{2}(U,K)\xrightarrow{d}\cdots $$ 

is exact. Here $K$ is injected into $A^0(U,K)$ by sending $k \in K$ to the function that has the constant value $k$ on $U$. That (9) is exact is apparent at $K$ and at $A^0(U,K)$, and follows elsewhere from the fact that $d \circ d = 0$ and that if $f \in A^p(U,K)$ with $p \geq 1$ and $df = 0$, then $f = dg$, where $g \in A^{p-1}(U,K)$ is defined by.

 $$ g(m_{0},\ldots,m_{p-1})=f(m,m_{0},\ldots,m_{p-1}) $$ 

for some arbitrary but fixed  $ m \in U $. Thus (7) is a fine torsionless resolution of  $ \mathcal{H} $.

The explicit exhibition of the fine torsionless resolution (7) of the constant sheaf $\mathcal{H}$ completes the proof in 5.20 of the existence of a cohomology theory for $M$ with coefficients in sheaves of $K$-modules. Thus by setting (as in 5.20(1))

 $$ H^{q}(M,\mathbb{S})=H^{q}\big(\Gamma\big(\mathcal{A}^{*}(M,K)\otimes\mathbb{S}\big)\big), $$ 

we obtain a cohomology theory with which, according to the corollary of 5.23, any other sheaf cohomology theory for $M$ with coefficients in sheaves of $K$-modules is uniquely isomorphic.

We shall now define the classical Alexander-Spanier cohomology modules of $M$ with coefficients in a $K$-module $G$, and show that they are canonically isomorphic with the cohomology modules $H^p(M,\mathcal{G})$ with coefficients in the constant sheaf $\mathcal{G}=M\times G$. We let $A^p(U,G)$ denote the $K$-module of functions $U^{p+1}\to G$, and similarly replace $K$ by $G$ and $\mathcal{H}$ by $\mathcal{G}$ in the constructions (1) through (7). Let

 $$ A_{0}^{p}(M,G)=\{f\in A^{p}(M,G)\colon\rho_{m,M}(f)=0\mathrm{f o r~a l l}m\in M\}. $$ 

Recall that  $ \rho_{m,M} $ is the homomorphism which assigns to each element of  $ A^{\mathfrak{p}}(M,G) $ its equivalence class in the stalk over  $ m $ of the associated sheaf  $ \mathcal{A}^{\mathfrak{p}}(M,G) $.  $ A^{\mathfrak{p}}(M,G) $ is a submodule of  $ A^{\mathfrak{p}}(M,G) $, and the extent to which  $ A^{\mathfrak{p}}(M,G) $ is not zero measures the extent to which the presheaf  $ \{A^{\mathfrak{p}}(U,G);\rho_{U,V}\} $ fails to satisfy  $ 5.7(C_1) $. The homomorphism (1) restricted to  $ A^{\mathfrak{p}}(M,G) $ has range in  $ A^{\mathfrak{p}+1}(M,G) $ and thus yields homomorphisms on quotients

 $$ A^{p}(M,G)/A_{0}^{p}(M,G)\to A^{p+1}(M,G)/A_{0}^{p+1}(M,G). $$ 

The sequence of modules and homomorphisms given by (13) for $p \geq 0$ form a cochain complex which we shall denote by $A^*(M,G)/A_0^*(M,G)$, and in which the modules of $q$ cochains for $q < 0$ are as usual all assumed to be zero. The classical Alexander-Spanier cohomology modules for $M$ with coefficients in the $K$-module $G$ are given by definition by

 $$ H_{A-S}^{a}(M;G)=H^{a}\big(A^{*}(M,G)/A_{0}^{*}(M,G)\big). $$ 

Since the sequence (7) with $K$ replaced by $G$ and $\mathcal{H}$ by $\mathcal{G}$ is a fine resolution of $\mathcal{G}$, it follows from 5.25 that there are canonical isomorphisms

 $$ H^{q}(M,\mathcal{G})\cong H^{q}\big(\Gamma\big(\mathcal{A}^{*}(M,G)\big)\big). $$ 

That there are canonical isomorphisms

 $$ H_{A-S}^{a}(M;G)\cong H^{a}(M,\mathcal{G}) $$ 

follows from (14) and (15) and from the fact that the natural cochain map

 $$ A^{*}(M,G)/A_{0}^{*}(M,G)\to\Gamma\bigl(\mathcal{A}^{*}(M,G)\bigr) $$ 

is an isomorphism. This in turn is an immediate consequence of the following proposition.

5.27 Proposition Let $\{S_U; \rho_{U,V}\}$ be a presheaf on $M$ satisfying $5.7(C_3)$, and let $S$ be the associated sheaf. As in 5.26(12), let

 $$ (S_{M})_{0}=\{s\in S_{M}\colon\;\rho_{m,M}(s)=0\mathrm{f o r~a l l~}m\in M\}. $$ 

Then the sequence

 $$ 0\to(S_{M})_{0}\to S_{M}\xrightarrow{7}\Gamma(\mathcal{S})\to0 $$ 

is exact.

PROOF Since $\gamma$ is the homomorphism which sends $s \in S_M$ to the global section $m \mapsto \rho_{m,M}(s)$ of $\delta$, the exactness of the sequence (2) at $S_M$ is the result of the definition of $(S_M)_0$. Thus we need only prove that $\gamma$ is surjective. Let $t \in \Gamma(8)$. Then there is a locally finite open cover $\{U_a\}$ of $M$, and there are elements $s_a \in S_{U_a}$ such that

 $$ \gamma(s_{a})=t\mid U_{a}. $$ 

Let $\{V_{\alpha}\}$ be a refinement such that $\overline{V_{\alpha}} \subset U_{\alpha}$. Let $I_{m}$ be the (finite) collection of all those indices $\alpha$ for which $m \in \overline{V_{\alpha}}$. Choose a neighborhood $W_{m}$ of $m$ such that

 $$ W_{m}\cap\overline{{V_{\beta}}}=\varnothing\quad\mathrm{i f}\quad\beta\notin I_{m}, $$ 

 $$ W_{m}\subset\bigcap_{a\in I_{m}}U_{a}, $$ 

 $$ \rho_{W_{m},U_{\alpha}}(s_{\alpha})=\rho_{W_{m},U_{\alpha}}(s_{\alpha^{\prime}})\quad\mathrm{i f}\quad\alpha,\alpha^{\prime}\in I_{m}. $$ 

Let $s_{m} \in S_{W_{m}}$ be the common image of the elements in (c). Then for all $n$ and $m$ in $M$,

 $$ \rho_{W_{m}\cap W_{n},W_{m}}(s_{m})=\rho_{W_{m}\cap W_{n},W_{n}}(s_{n}). $$ 

For let $p \in W_m \cap W_n$. Then it follows from (a) that $I_p \subset I_m \cap I_n$. So let $\alpha \in I_p$. Then according to (c),

 $$ s_{m}=\rho_{W_{m},U_{\alpha}}(s_{\alpha})\qquad\mathrm{a n d}\qquad s_{n}=\rho_{W_{n},U_{\alpha}}(s_{\alpha}), $$ 

so that

 $$ \rho_{W_{m}\cap W_{n},W_{m}}(s_{m})=\rho_{W_{m}\cap W_{n},U_{\alpha}}(s_{\alpha})=\rho_{W_{m}\cap W_{n},W_{n}}(s_{n}), $$ 

which proves (4). It follows from (4) and the property $5.7(C_{2})$ that there is an element $s \in S_{M}$ such that

 $$ \rho_{W_{m},M}(s)=s_{m}; $$ 

and it follows from (7), (5), and (3) that  $ \gamma(s) = t $.

##### de Rham Cohomology

5.28 In this section we shall take the principal ideal domain $K$ to be the real number field $\mathbb{R}$. Let $U \subset M$ be open. The set of differential $p$-forms on $U$ forms a real vector space, which we have denoted by $E^p(U)$. These real vector spaces together with ordinary restriction homomorphisms $\rho_{U,V}$ form a presheaf

 $$ \{E^{p}(U);\rho_{U,V}\} $$ 

which satisfies both  $ 5.7(C_{1}) $ and  $ (C_{2}) $ and thus is complete. From the exterior derivative operator d we obtain presheaf homomorphisms

 $$ \{E^{v}(U);\rho_{U,V}\}\xrightarrow{d}\{E^{v+1}(U);\rho_{U,V}\}\qquad(p\geq0). $$ 

We shall denote the associated sheaf of germs of differential $p$-forms by $\mathcal{E}^{p}(M)$, and we shall retain the symbol $d$ for the sheaf homomorphisms induced by (2). The constant sheaf $\mathcal{R}=M\times\mathbb{R}$ can be naturally injected into $\mathcal{E}^{0}(M)$ by sending $a\in\mathcal{R}_{m}$ to the germ at $m$ of the function with constant value $a$. Thus we have a sequence

 $$ 0\to\mathcal{R}\to\mathcal{E}^{0}(M)\xrightarrow{d}\mathcal{E}^{1}(M)\xrightarrow{d}\mathcal{E}^{2}(M)\xrightarrow{d}\cdots. $$ 

We claim that (3) is a fine torsionless resolution of the constant sheaf  $ \mathscr{R} $. Partitions of unity can be constructed for the sheaves  $ \mathscr{E}^{\circ}(M) $ exactly as they were constructed in 5.10 for  $ \mathscr{C}^{\infty}(M) = \mathscr{E}^{\circ}(M) $. Thus the sheaves  $ \mathscr{E}^{\circ}(M) $ are all fine. They are certainly torsionless since they are sheaves of real vector spaces. The sequence (3) is clearly exact at  $ \mathscr{R} $ and at  $ \mathscr{E}^{\circ}(M) $. Since the exterior derivative operator satisfies  $ d \circ d = 0 $, the same is true of the sheaf homomorphisms in (3); hence the image of each homomorphism is contained in the kernel of the next. That the sequence is actually exact, and therefore a resolution, is a consequence of the corollaries of the Poincaré lemma 4.18. We shall return to the resolution (3) in a moment. First, we comment about the structure of the Poincaré lemma.

5.29 Remark The collection of operators $h_k$ in the Poincaré lemma 4.18 is an example of a very useful tool in the cohomology theory of cochain complexes called a homotopy operator. We shall have further occasion to make use of such operators. They arise generally in the following situation. Suppose that we have two cochain maps, call them $f$ and $g$, between cochain complexes $C^*$ and $D^*$, and suppose that we want to show that $f$ and $g$ both induce the same homomorphisms of the cohomology modules. This will follow if we can find homotopy operators for $f$ and $g$, namely, homomorphisms $h_k: C^k \to D^{k-1}$ such that

 $$ h_{k+1}\circ d+d\circ h_{k}=f_{k}-g_{k} $$ 

on $C^k$ (where $d$ indicates the coboundary operators in both $C^*$ and $D^*$). For then if $\sigma \in C^k$ is a cocycle, then $f_k(\sigma) = g_k(\sigma)$ up to a coboundary, so $f_k(\sigma)$ and $g_k(\sigma)$ lie in the same cohomology class. In the Poincaré lemma, we found homotopy operators (for $k \geq 1$) between the identity cochain map of the cochain complex

 $$ \cdots\to0\to E^{0}(U)\xrightarrow{\dot{d}}E^{1}(U)\xrightarrow{\dot{d}}E^{2}(U)\xrightarrow{\dot{d}}\cdots $$ 

and the zero cochain map, with $U$ the open unit ball in Euclidean space. Consequently, all of the cohomology groups of this cochain complex vanish for $k \geq 1$.

5.30 Since 5.28(3) is exact, it is therefore a fine torsionless resolution of the constant sheaf R. According to 5.20, the resolution 5.28(3) gives rise to a cohomology theory for M with coefficients in sheaves of real vector spaces by setting

 $$ H^{\mathfrak{q}}(M,\mathcal{T})=H^{\mathfrak{q}}\big(\Gamma\big(\mathcal{E}^{*}(M)\otimes\mathcal{T}\big)\big) $$ 

for $q \geq 0$ and for $\mathcal{T}$ a sheaf of real vector spaces over $M$. In view of the corollary of 5.23, this theory is uniquely isomorphic with the theory we constructed in 5.26(11).

If we take  $ \mathcal{T} $ to be the constant sheaf  $ \mathcal{R} $, then

 $$ H^{q}(M,\mathcal{R})=H^{q}\big(\Gamma\big(\mathcal{E}^{*}(M)\otimes\mathcal{R}\big)\big)\cong H^{q}\big(\Gamma\big(\mathcal{E}^{*}(M)\big)\big). $$ 

Consider now the cochain complex  $ \Gamma(\mathcal{E}^{*}(M)) $:

 $$ \cdots\to0\to\Gamma\bigl(\mathcal{E}^{\mathfrak{e}}(M)\bigr)\to\Gamma\bigl(\mathcal{E}^{1}(M)\bigr)\to\Gamma\bigl(\mathcal{E}^{2}(M)\bigr)\to\cdots $$ 

and the cochain complex  $ E^{*}(M) $:

 $$ \cdots\to0\to E^{0}(M)\stackrel{d}{\longrightarrow}E^{1}(M)\stackrel{d}{\longrightarrow}E^{2}(M)\stackrel{d}{\longrightarrow}\cdots. $$ 

In view of the fact that the presheaves  $ \{E^{p}(U);\rho_{U,V}\} $ are complete, it follows from 5.8 (or is easily seen directly in this special case) that the natural homomorphisms

 $$ E^{\mathfrak{p}}(M)\to\Gamma\bigl(\mathcal{E}^{\mathfrak{p}}(M)\bigr) $$ 

are isomorphisms. Since the homomorphisms (5) commute with the co-boundaries of the respective cochain complexes (3) and (4), they induce a cochain map  $ E^*(M) \to \Gamma(\mathcal{E}^*(M)) $ which is an isomorphism of cochain complexes. Thus there are canonical isomorphisms

 $$ H^{q}\bigl(\Gamma\bigl(\mathcal{E}^{*}(M)\bigr)\bigr)\cong H^{q}\bigl(E^{*}(M)\bigr). $$ 

But  $ H^{\varphi}(E^{*}(M)) $ is the classical qth de Rham cohomology group  $ H_{\mathrm{deR}}^{q}(M) $ for M which we introduced in 4.13(1), namely, the quotient of the vector space of closed q-forms (those annihilated by d) modulo the vector space of exact q-forms (those in the image of d). Thus from (2) and (6) we obtain canonical isomorphism

 $$ H^{q}(M,\mathcal{R})\cong H_{\operatorname{d e}\mathbb{R}}^{q}(M). $$ 

##### Singular Cohomology

5.31 In this section we again take $K$ to be an arbitrary principal ideal domain, and we let $U \subset M$ be open. In 4.6 we introduced differentiable singular simplices for the theory of integration on manifolds. Now we need continuous singular simplices. We review the definitions. Recall that for each integer $p \geq 1$ we let

 $$ \Delta^{p}=\Big\{(a_{1},\ldots,a_{p})\in\mathbb{R}^{p}\colon\sum_{i=1}^{p}a_{i}\leq1\quad\mathrm{a n d}\quad\mathrm{e a c h}\quad a_{i}\geq0\Big\}. $$ 

$\Delta^{\flat}$ is called the standard $p$-simplex in $\mathbb{R}^{\flat}$. For $p = 0$ we set $\Delta^{\flat}$ equal to the 1-point space $\{0\}$; and $\Delta^{\flat}$ is the standard $0$-simplex. A (continuous) singular $p$-simplex $\sigma$ in $U$ is a continuous map $\sigma: \Delta^{\flat} \to U$. If $p \geq 1$, we define a differentiable singular $p$-simplex in $U$ to be a singular $p$-simplex $\sigma$ which can be extended to be a differentiable $(C^{\infty})$ map of a neighborhood of $\Delta^{\flat}$ in $\mathbb{R}^{\flat}$ into $U$.

We shall let $S_{p}(U)$ denote the free abelian group generated by the singular $p$-simplices in $U$. Elements of $S_{p}(U)$ are called singular $p$-chains with integer coefficients. If $\sigma$ is a singular $p$-simplex in $U$, with $p \geq 1$, then its boundary is defined as in 4.6(4) to be the singular $(p-1)$ chain

 $$ \partial\sigma=\sum_{i=0}^{n}(-1)^{i}\sigma^{i} $$ 

where  $ \sigma^{i} $ is the  $ i $th face of  $ \sigma $ (see 4.6(3)). The boundary operator extends to a homomorphism of  $ S_{p}(U) $ into  $ S_{p-1}(U) $ for each  $ p \geq 1 $, and satisfies (as in 4.6(7))

 $$ \partial\circ\partial=0. $$ 

Let $S^{\#}(U,K)$ denote the $K$-module consisting of functions $f$ which assign to each singular $p$-simplex in $U$ an element of $K$. Such an $f$ is called a singular $p$-cochain on $U$. Scalar multiplication and addition in the module $S^{\#}(U,K)$ are defined by

 $$ (k f)(\sigma)=k\big(f(\sigma)\big), $$ 

 $$ (f+g)(\sigma)=f(\sigma)+g(\sigma). $$ 

Each cochain in $S^{p}(U,K)$ canonically extends to a homomorphism of $S_{p}(U)$ into $K$. In fact, this determines an isomorphism of $S^{p}(U,K)$ with the $K$-module of homomorphisms of $S_{p}(U)$ into $K$. For convenience we shall at times regard elements of $S^{p}(U,K)$ as such homomorphisms. If $V\subset U$, we let

 $$ \rho_{V,U}\colon S^{\mathfrak{d}}(U,K)\to S^{\mathfrak{d}}(V,K) $$ 

be the homomorphism which assigns to each $f \in S^p(U,K)$ its restriction to singular $p$-simplices which lie in $V$. Then

 $$ \{S^{p}(U,K);\rho_{U,V}\} $$ 

forms a presheaf on $M$ called the presheaf of singular $p$-cochains. Observe that these presheaves, for $p \geq 1$, satisfy $5.7(C_2)$ but not $(C_1)$, and that the presheaf $\{S^0(U,K);\rho_{U,V}\}$ (which can be canonically identified with the presheaf $\{A^0(U,K);\rho_{U,V}\}$ of 5.26 since each singular 0-simplex in $U$ can be identified with a point of $U$) is complete.

For $p \geq 1$, we let $S_\infty^\circ(U,K)$ denote the $K$-module consisting of functions $f$ which assign to each differentiable singular $p$-simplex in $U$ an element of $K$. Such an $f$ is called a differentiable singular $p$-cochain on $U$. With restriction homomorphisms defined as in (5), we obtain the presheaf $\{S_\infty^\circ(U,K); \rho_{U,V}\}$ of differentiable singular $p$-cochains on $M$. Since the developments of the differentiable and the continuous singular cohomology theories are nearly word-for-word the same, we shall primarily discuss the continuous case. Just keep in mind that analogous constructions apply if $S_\infty^\circ(U,K)$, for $p \geq 1$, is substituted for $S^\circ(U,K)$. When substantial differences arise they will be discussed.

A coboundary homomorphism

 $$ d\colon S^{p}(U,K)\to S^{p+1}(U,K) $$ 

is defined by setting

 $$ d f(\sigma)=f(\partial\sigma) $$ 

for $f \in S^p(U, K)$ and for $\sigma$ a singular $(p+1)$ simplex in $U$. It follows from item (3) that

 $$ d\circ d=0. $$ 

Since $d$ commutes with restriction homomorphisms, $d$ yields a presheaf homomorphism

 $$ \{{S}^{\mathfrak{p}}(U,K);\rho_{U,V}\}\to\{{S}^{\mathfrak{p}+1}(U,K);\rho_{U,V}\}; $$ 

and at the same time, in view of (9), d makes

 $$ \cdots\to0\to S^{0}(U,K)\stackrel{d}{\longrightarrow}S^{1}(U,K)\stackrel{d}{\longrightarrow}S^{2}(U,K)\stackrel{d}{\longrightarrow}\cdots $$ 

into a cochain complex (where the modules of q-cochains are zero for q < 0) which we denote by  $ S^{*}(U,K) $.

We denote the associated sheaf of germs of singular $p$-cochains by $\mathcal{S}^{p}(M,K)$ (and by $\mathcal{S}_{\infty}^{p}(M,K)$ in the differentiable case) and retain $d$ to denote the induced sheaf homomorphisms

 $$ \mathbb{S}^{\mathfrak{p}}(M,K)\xrightarrow{d}\mathbb{S}^{\mathfrak{p}+1}(M,K). $$ 

Observe that $S^{0}(M,K)$ is simply the sheaf of germs of functions on $M$ with values in $K$. The constant sheaf $\mathcal{H}$ can be canonically injected into $S^{0}(M,K)$ by sending $k\in\mathcal{H}_{m}$ to the germ at $m$ of the function on $M$ with constant value $k$. Thus we have a sequence

 $$ 0\to\mathcal{K}\to\mathcal{S}^{0}(M,K)\xrightarrow{d}\mathcal{S}^{1}(M,K)\xrightarrow{d}\mathcal{S}^{2}(M,K)\xrightarrow{d}\cdots $$ 

and an analogous sequence with $\mathcal{S}^{p}(M,K)$ replaced by $\mathcal{S}_{\infty}^{p}(M,K)$ for $p\geq1$. We claim that in both the continuous and the differentiable cases, the sequence (13) is a fine torsionless resolution of the constant sheaf $\mathcal{H}$. That the sheaves $\mathcal{S}^{p}(M,K)$ (and $\mathcal{S}_{\infty}^{p}(M,K)$ for $p\geq1$) are all torsionless is a consequence of the fact that they are all sheaves of germs of certain types of functions with values in $K$, and $K$ is an integral domain. To see that the sheaves $\mathcal{S}^{p}(M,K)$ (and $\mathcal{S}_{\infty}^{p}(M,K)$ for $p\geq1$) are all fine sheaves, let a locally finite open cover $\{U_{i}\}$ of $M$ be given, and take (as in 5.22) a partition of unity $\{\varphi_{i}\}$ subordinate to the cover $\{U_{i}\}$ in which the functions $\varphi_{i}$ take values 0 or 1 only. For each $i$, we define an endomorphism $\widetilde{I}_{i}$ of $S^{p}(U,K)$ by setting

 $$ \tilde{l}_{i}(f)(\sigma)=\varphi_{i}\big(\sigma(0)\big)f(\sigma), $$ 

where if  $ p \geq 1 $, then 0 denotes the origin in  $ \mathbb{R}^p $. The endomorphisms  $ \tilde{I}_i $ commute with restrictions, and thus determine presheaf endomorphisms

of $\{S^p(U,K); \rho_{U,V}\}$. Let $l_i: \mathcal{S}^p(M,K) \to \mathcal{S}^p(M,K)$ be the sheaf endomorphism associated with $\tilde{l}_i$. Then it follows readily that $\text{supp} l_i \subset U_i$ and that $\sum l_i \equiv 1$. Thus the sheaves $\mathcal{S}^p(M,K)$ (similarly $\mathcal{S}^p(M,K)$ for $p \geq 1$). are fine sheaves. The exactness of (13) is apparent at $\mathcal{H}$ and $\mathcal{S}^p(M,K)$, and we know that $d \circ d = 0$. For the exactness of (13), it remains to be shown that at each stage $\mathcal{S}^p(M,K)$ for $p \geq 1$ the image of the preceding homomorphism contains the kernel of the next. This will follow if we can prove that for “sufficiently small” open sets $U$, if $f$ is a singular $p$-cochain on $U$ such that $df = 0$ and if $p \geq 1$, then there is a singular $(p-1)$ cochain $g$ on $U$ such that $f = dg$. Here we shall make use of the fact that $M$ is a manifold and is therefore locally Euclidean. It suffices to assume that $U$ is the open unit ball in $\mathbb{R}^{dim M}$. To prove that if $df = 0$ then there is a $g$ such that $dg = f$, we need only find a homotopy operator (see 5.29)

 $$ h_{p}\colon S^{p}(U,K)\to S^{p-1}(U,K)\qquad(p\geq1) $$ 

such that

 $$ d\circ h_{p}+h_{p+1}\circ d=\operatorname{i d}. $$ 

We define $h_p$ as follows. Let $f \in S^p(U,K)$, where $U$ is the open unit ball in $\mathbb{R}^{\dim M}$, and let $\sigma$ be a singular $(p-1)$ simplex in $U$. Define

 $$ h_{p}(f)(\sigma)=f\big(\tilde{h}_{p}(\sigma)\big) $$ 

where  $ \tilde{h}_{p}(\sigma) $ is the singular  $ p $-simplex in  $ U $ which maps the origin in  $ \Delta^{p} $ to the origin in  $ U $, and which is defined for  $ (a_{1}, \ldots, a_{p}) \neq 0 $ by

 $$ \tilde{h}_{p}(\sigma)(a_{1},\ldots,a_{p})=\left(\sum_{i=1}^{p}a_{i}\right)\cdot\sigma\left(a_{2}\bigg/\sum_{i=1}^{p}a_{i},\ldots,a_{p}\bigg/\sum_{i=1}^{p}a_{i}\right). $$ 

Geometrically,  $ \tilde{h}_{p}(\sigma) $ is the cone in U obtained by joining  $ \sigma $ radially to the origin:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//809c2fcf-9364-47c1-9360-5c5f8b97072b/markdown_1/imgs/img_in_image_box_188_809_438_1049.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A16Z%2F-1%2F%2F5d3f26e580467c5e74361e847a4c9ab225a3a328d8a4a3c8b0756b4e9add82d2" alt="Image" width="25%" /></div>


 $ \tilde{h}_{p} $ extends to a homomorphism  $ S_{p-1}(U) \to S_{p}(U) $. It follows from (18) and the definition 4.6(4) of the boundary operator  $ \partial $ that

 $$ \mathrm{i d}=\partial\circ\tilde{h}_{p+1}+\tilde{h}_{p}\circ\partial $$ 

on $S_{p}(U)$ for $p \geq 1$. Before checking (19) in general, try the case in which $p = 1$, where it turns out that

 $$ \sigma=(\tilde{h}_{2}(\sigma))^{2}-(\tilde{h}_{2}(\sigma))^{1}+(\tilde{h}_{2}(\sigma))^{0}+\tilde{h}_{1}(\sigma^{0})-\tilde{h}_{1}(\sigma^{1}), $$ 

and where the corresponding picture is

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//809c2fcf-9364-47c1-9360-5c5f8b97072b/markdown_2/imgs/img_in_image_box_206_267_814_500.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A17Z%2F-1%2F%2F5b1433194f026dbdac027b55f27bf07b3e21435766b6bb11030d848f0e43397d" alt="Image" width="63%" /></div>


<div style="text-align: center;"><div style="text-align: center;">Now, (16) follows from (19) and (17) and from the definition (8) of the co-boundary operator $d$. However, here is one point where the treatment of the continuous case does not quite suffice for the differentiable case. For if $\sigma$ is a differentiable singular $(p-1)$ simplex with $p\geq2$, and if $\tilde{h}_{p}(\sigma)$ is defined as in (18), then $\tilde{h}_{p}(\sigma)$ will be a continuous but generally not a differentiable singular $p$-simplex—there are differentiability problems at the origin. For example, if $\sigma$ were a differentiable singular 1-simplex in $U$, then for $\tilde{h}(\sigma)$ as defined in (18) to extend to be a smooth mapping on a neighborhood of the origin in $\mathbb{R}^{2}$, one would at least have to have the image of $\sigma$ contained in a 2-dimensional plane passing through the origin in $U$. This, of course, may not be the case. The defect is easily remedied by means of a “smoothing” function. Let $\varphi$ denote the real-valued $C^{\infty}$ function on the real line defined by 1.10(3). Then $\varphi(t)$ takes values between 0 and 1, and has the value 1 for $t\geq1$ and the value 0 for $t\leq0$. Then if $p\geq2$, and if $\sigma$ is a differentiable $(p-1)$ simplex, we define $\tilde{h}_{p}(\sigma)$ by</div> </div>


 $$ \tilde{h}_{p}(\sigma)(a_{1},\ldots,a_{p})=\varphi\left(\sum_{i=1}^{p}a_{i}\right)\cdot\sigma\left(a_{2}\bigg/\sum_{i=1}^{p}a_{i},\ldots,a_{p}\bigg/\sum_{i=1}^{p}a_{i}\right), $$ 

where, as in (18), we assume that  $ \tilde{h}_{p}(\sigma) $ maps the origin in  $ \Delta^{p} $ to the origin in U. Now extend  $ \sigma $ to be differentiable on all of  $ \mathbb{R}^{p-1} $ so that  $ \sigma $ and each of its derivatives is bounded. Then  $ \tilde{h}_{p}(\sigma) $ is defined on all of  $ \mathbb{R}^{p} $, providing that we agree that  $ \tilde{h}_{p}(\sigma) $ maps any point where  $ \sum_{i=1}^{p} a_{i} = 0 $ to the origin in U. Moreover,  $ \tilde{h}_{p}(\sigma) $ is differentiable of class  $ C^{\infty} $ on all of  $ \mathbb{R}^{p} $. The only points where problems arise are those for which  $ \sum_{i=1}^{p} a_{i} = 0 $; and since  $ \varphi(t) $ and all of its derivatives vanish faster than any polynomial in  $ t $ as  $ t \to 0 $, and since

$\sigma$ and each of its derivatives is bounded on $\mathbb{R}^{p-1}$, it follows that all derivatives of $\tilde{h}_{p}(\sigma)$ of all orders exist, and are continuous, and are zero at points where $\sum_{i=1}^{p} a_{i}=0$. This completes the proof that (13) is a fine torsionless resolution of the constant sheaf $\mathcal{H}$, both for the continuous and for the differentiable singular theories.

Thus both resolutions (13), for the continuous and the differentiable cases, give rise, as in 5.20, to cohomology theories if we set

 $$ \begin{aligned}{H^{q}(M,\mathbb{S})}&{{}=H^{q}\big(\Gamma\big(\mathbb{S}^{*}(M,K)\otimes\mathbb{S}\big)\big),}\\ {H^{q}(M,\mathbb{S})}&{{}=H^{q}\big(\Gamma\big(\mathbb{S}_{\infty}^{*}(M,K)\otimes\mathbb{S}\big)\big)}\\ \end{aligned} $$ 

for each integer $q$ and for $S$ any sheaf of $K$-modules over $M$. In view of the corollary of 5.23, these theories are uniquely isomorphic and, moreover, are uniquely isomorphic with the theories 5.26(11) and 5.30(1).

5.32 Let $G$ be a $K$-module. We let $S^p(U,G)$ denote the $K$-module consisting of functions which assign to each singular $p$-simplex in $U$ an element of $G$. Similarly, we may replace $K$ by $G$ and $\mathcal{H}$ by the constant sheaf $\mathcal{G}$ in the constructions 5.31(4)–(13).

The classical singular cohomology groups of M with coefficients in a K-module G are defined in the continuous and differentiable cases by:

 $$ \begin{aligned}{H_{\Delta}^{q}(M;G)}&{{}=H^{q}\big(S^{*}(M,G)\big),}\\ {H_{\Delta^{\infty}}^{q}(M;G)}&{{}=H^{q}\big(S_{\infty}^{*}(M,G)\big).}\\ \end{aligned} $$ 

We shall now show that the classical cohomology groups (actually K-modules) are canonically isomorphic with the sheaf cohomology modules  $ H^{e}(M,\mathcal{G}) $. It follows from Proposition 5.27 that

 $$ 0\to S_{0}^{*}(M,G)\to S^{*}(M,G)\to\Gamma\bigl(\mathcal{S}^{*}(M,G)\bigr)\to0 $$ 

is a short exact sequence of cochain complexes (with a similar sequence in the differentiable case). Thus if we prove that

 $$ H^{q}\bigl(S_{0}^{*}(M,G)\bigr)=0\quad\mathrm{f o r~a l l}\quad q $$ 

(also in the differentiable case), then it follows from the long exact sequence 5.17(2) that there are canonical isomorphisms

 $$ \begin{array}{r l}&{H^{q}\big(S^{*}(M,G)\big)\cong H^{q}\big(\Gamma\big(\mathcal{S}^{*}(M,G)\big)\big),}\\ &{H^{q}\big(S_{\infty}^{*}(M,G)\big)\cong H^{q}\big(\Gamma\big(\mathcal{S}_{\infty}^{*}(M,G)\big)\big).}\end{array} $$ 

Thus it follows from (1) and (4), and from 5.25 (applied to the fine resolutions of G obtained by replacing K by G and  $ \mathcal{H} $ by  $ \mathcal{G} $ in 5.31(13)) that we have canonical isomorphism

 $$ H_{\Delta}^{q}(M;G)\cong H^{q}(M,\mathcal{G})\cong H_{\Delta^{\infty}}^{q}(M;G). $$ 

The proof of (3) for the continuous singular theory goes as follows. (The differentiable case is identical.) It is trivially satisfied for $q<0$ since in this range the modules of the cochain complex $S_0^*(M,G)$ are all zero. The module $S_0^*(M,G)$ is also zero since the presheaf $\{S^0(U,G); p_{U,V}\}$ is complete. Thus $H^0(S_0^*(M,G))=0$. It remains to prove (3) for $q\geq1$. Let $U=\{U_i\}$ be an arbitrary open cover of $M$. Let $S_U^*(M,G)$ be the cochain complex consisting of modules $S_U^*(M,G)$ of singular cochains $f$, with values in $G$, defined only on “$\mathcal{U}$-small” singular $p$-simplices, that is, defined only on those singular $p$-simplices whose ranges lie in elements of $\mathcal{U}$. Each element of $S^p(M,G)$ determines an element of $S_U^*(M,G)$ by restriction to $\mathcal{U}$-small simplices. The restriction homomorphisms $f_U:S^p(M,G)\to S_U^*(M,G)$ yield a surjective cochain map

 $$ j_{\mathfrak{U}}\colon S^{*}(M,G)\to S_{\mathfrak{U}}^{*}(M,G). $$ 

The kernels of the homomorphisms  $ j_{u} $ form a cochain complex  $ K_{u}^{*} $ such that

 $$ 0\to K_{\mathfrak{U}}^{*}\to S^{*}(M,G)\to S_{\mathfrak{U}}^{*}(M,G)\to0 $$ 

is an exact sequence of cochain complexes. The key ingredient in the proof of (3) is the fact that the cochain map $j_{tt}$ induces isomorphismsincohomology. Let us assume this for the moment. It follows from the long exact cohomology sequence for (7) that

 $$ H^{q}(K_{\mathfrak{U}}^{*})=0\quad\mathrm{f o r~a l l~}q. $$ 

So now let $q \geq 1$, and let $f$ be a cocycle in $S_0^q(M,G)$; that is, $df = 0$. Then, by the definition of $S_0^q(M,G)$, there is an open cover $\mathcal{U}$ of $M$ consisting of sufficiently small open sets so that $f \in K_U^q$. It follows from (8) that there exists $g \in K_U^{q-1} \subset S_0^{q-1}(M,G)$ such that $dg = f$, which proves (3).

Now we return to the proof that the cochain map $j_{u}$ induces isomorphismsof the cohomology. Since we will work with a fixed cover $\mathcal{U}$ of $M$, we drop the subscript $\mathcal{U}$ from $j_{u}$. To prove that $j\colon S^{*}(M,G)\to S_{u}^{*}(M,G)$ induces isomorphismsof the cohomology modules, we shall construct a cochain map

 $$ k\colon S_{\mathfrak{U}}^{*}(M,G)\to S^{*}(M,G) $$ 

such that

 $$ j\circ k=\mathtt{i d}, $$ 

whence the cochain map $j$ must induce surjections of the cohomology modules, and such that there exist homotopy operators $h_{p}\colon S^{p}(M,G)\to S^{p-1}(M,G)$ for all $p$ such that

 $$ h_{p+1}\circ d+d\circ h_{p}=\operatorname{i d}-k_{p}\circ j_{p}, $$ 

whence  $ k \circ j $ induces the identity on cohomology, which implies that j must

induce injections. Hence it will follow from (10) and (11) that $j$ induces isomorphismshs on the cohomology modules. The definitions of $h$ and $k$ require a few preliminary constructions. The details become a little technical, but the general idea is this. Let $f \in S_l(M,G)$. Thus $f$ is defined only on $\mathbb{U}$-small singular $p$-simplices. We want to define $k(f)$ to be an element of $S^p(M,G)$; that is, $k(f)$ is to be defined on all singular $p$-simplices. We will define an operation “subdivision” to break large singular $p$-simplices into chains of smaller ones. By subdividing any singular $p$-simplex sufficiently many times, we will obtain a chain of $\mathbb{U}$-small singular $p$-simplices to which we can then apply $f$. So we will define $k(f)$ on the large singular simplex to be $f$ on the subdivided ones. Simplices which are already $\mathbb{U}$-small will not be subdivided at all. The technical difficulty which arises will be due to the fact that the number of times that a singular $p$-simplex $\sigma$ needs to be subdivided in order to obtain a chain of $\mathbb{U}$-small simplices depends on $\sigma$.

Let  $ q \geq 1 $. A linear  $ p $-simplex in  $ \Delta^q $ is a singular  $ p $-simplex of the form

 $$ (a_{1},\ldots,a_{p})\mapsto\left(1-\sum_{i=1}^{p}a_{i}\right)v_{0}+a_{1}v_{1}+\cdots+a_{p}v_{p} $$ 

$(0\mapsto v_0$ for $p=0)$, canonically determined by the ordered sequence of points $v_0,\ldots,v_p$ in $\Delta^q$. We shall denote such a linear simplex by $(v_0,\ldots,v_p)$. The identity map of $\Delta^q$ onto itself is a linear $q$-simplex in $\Delta^q$ which we shall denote simply by $\Delta^q$. The free abelian group generated by the linear $p$-simplices in $\Delta^q$ we shall denote by $L_p(\Delta^q)$. The barycenter of a linear $p$-simplicx $\sigma=(v_0,\ldots,v_p)$ in $\Delta^q$ is the point

 $$ b_{\sigma}=\frac{1}{p+1}v_{0}+\cdots+\frac{1}{p+1}v_{p}. $$ 

Given a linear $p$-simplex $\sigma = (v_0, \ldots, v_p)$ in $\Delta^q$ and a point $v \in \Delta^q$, we define the join $v\sigma$ of $v$ and $\sigma$ to be the linear $(p+1)$ simplex $(v, v_0, \ldots, v_p)$ in $\Delta^q$. The join operation extends by linearity to $L_p(\Delta^q)$. A direct calculation shows that if $p \geq 1$, then

 $$ \partial(v\sigma)=\sigma-v(\partial\sigma). $$ 

We define subdivision homomorphisms $\mathrm{Sd}: L_p(\Delta^q) \to L_p(\Delta^q)$ by setting $\mathrm{Sd} = \mathrm{id}$ for $p = 0$ and by setting

 $$ \mathsf{S d}(\sigma)=b_{\sigma}\mathsf{S d}(\partial\sigma) $$ 

for $\sigma$ a linear $p$-simplex in $\Delta^q$ with $p \geq 1$, and extending linearly to $L_p(\Delta^q)$. We define homomorphisms $R: L_p(\Delta^q) \to L_{p+1}(\Delta^q)$ by setting $R = 0$ for $p = 0$ and by setting

 $$ R(\sigma)=b_{\sigma}\big(\sigma-\mathsf{S d}(\sigma)-R(\partial\sigma)\big) $$ 

for $\sigma$ a linear $p$-simplex in $\Delta^{q}$ with $p \geq 1$, and extending linearly to $L_{p}(\Delta^{q})$. It follows from (13), (14), (15), and (16), using an elementary induction argument, that

 $$ \begin{aligned}{\partial\circ\operatorname{S d}=\operatorname{S d}\circ\partial,}\\ {\partial\circ R+R\circ\partial=\operatorname{i d}-\operatorname{S d}}\\ \end{aligned} $$ 

on $L_{p}(\Delta^{q})$ with $p\geq1$. (The collection of modules $L_{p}(\Delta^{q})$ and homomorphisms $\partial\colon L_{p}(\Delta^{q})\to L_{p-1}(\Delta^{q})$ form what is called a chain complex in contrast with a cochain complex 5.16(1) in which the homomorphisms go the other direction. The first formula in (17) says that subdivision $\mathsf{Sd}$ is a chain map of this chain complex with itself. The second formula in (17) shows that $R$ is a homotopy operator for the chain maps id and $\mathsf{Sd}$, from which it follows that $\mathsf{Sd}$ induces the identity map on the homology groups $(\ker\partial_{p}/\mathsf{Im}\partial_{p+1})$ of this chain complex.)

We define homomorphisms $\mathbf{Sd}\colon S_p(U)\to S_p(U)$ and $R\colon S_p(U)\to S_{p+1}(U)$ for $p\geq0$ by setting

 $$ \mathtt{S d}(\sigma)=\sigma\circ\mathtt{S d}(\Delta^{p}), $$ 

 $$ R(\sigma)=\sigma\circ R(\Delta^{\mathfrak{p}}) $$ 

for $\sigma$ a singular $p$-simplex in $U$, and then extending linearly to $S_{p}(U)$. It follows easily that formulas (17) hold on $S_{p}(U)$ for $p \geq 1$.

Now let  $ \sigma = (v_0, \ldots, v_p) $ be a linear  $ p $-simplex in  $ \Delta^q $. Then the diameter of each simplex of  $ \text{Sd}(\sigma) $ is at most  $ p/(p+1) $ times the diameter of  $ \sigma $, for the diameter of a linear simplex  $ \sigma $ is the maximum distance between any two of the vertices  $ v_i $. Of any two vertices in a simplex in  $ \text{Sd}(\sigma) $, at least one must be of the form  $ [1/(k+1)](v_{i_0} + \cdots + v_{i_k}) $ for  $ 1 \leq k \leq p $. The distance from this vertex to the other vertex is less than or equal to the distance to some  $ v_j $, and

 $$ \begin{aligned}\left|\frac{1}{k+1}(v_{i_{0}}+\cdots+v_{i_{k}})-v_{j}\right|\\ =\frac{1}{k+1}\left|\sum_{i=0}^{k}(v_{i_{1}}-v_{j})\right|\leq\frac{k}{k+1}\text{diam}\sigma\leq\frac{p}{p+1}\text{diam}\sigma.\end{aligned} $$ 

We are now ready to construct the maps $h_p$ and $k_p$. Let $\sigma$ be a singular $p$-simplex in $M$. The open cover $\sigma^{-1}(\Omega)$ of $\Delta^p$ has a Lebesgue number $\delta$ [27, p. 122]. It follows that for $s$ large enough, the diameter of each simplex in $(Sd)^s(\Delta^p)$ is less than $\delta$ where $(Sd)^s$ is the $s$-fold composition of $Sd$ with itself. Thus each singular $p$-simplex in the chain $(Sd)^s(\sigma)$ lies in an element of the cover $\Omega$. Now let $s(\sigma)$ be the smallest of those positive integers $s \geq 0$ for which each simplex of $(Sd)^s(\sigma)$ lies in an element of $\Omega$. Then we can define homomorphisms $k_p: S_l^p(M,G) \to S^p(M,G)$ by setting $k_p = id$ for $p \leq 0$, and for $p \geq 1$ by setting

 $$ k_{p}(f)(\sigma)=f\left((\mathbb{S d})^{s(\sigma)}(\sigma)+\sum_{j=0}^{p}(-1)^{j}R\left(\sum_{\substack{s(\sigma^{j})\leq i\leq s(\sigma)-1}}(\mathbb{S d})^{i}(\sigma^{j})\right)\right). $$ 

Note that Sd raised to a negative power is to be interpreted as the zero homomorphism, and (Sd)⁰ = id. We also define homomorphisms  $ h_p: S^p(M,G) \to S^{p-1}(M,G) $ by setting  $ h_p = 0 $ for  $ p \leq 1 $ and

 $$ h_{p}(f)(\sigma)=f\left(R\left(\sum_{0\leq i\leq s/{\sigma})-1}({\sf S d})^{i}(\sigma)\right)\right) $$ 

for $p \geq 2$. That (10) holds is obvious, and (11) follows immediately from a straightforward calculation. Finally, the fact that the homomorphisms $k$, yield a cochain map (9) follows from (11). For from (11) we obtain

 $$ \begin{array}{r}{d\circ k_{p}\circ j_{p}=k_{p+1}\circ j_{p+1}\circ d.}\end{array} $$ 

But $j$ is a cochain map. Thus $d\circ k_{p}\circ j_{p}=k_{p+1}\circ d\circ j_{p}$. Since $j$ is surjective, it follows that $d\circ k_{p}=k_{p+1}\circ d$. This completes the proof that $j$ induces isomorphism in cohomology.

##### Čech Cohomology

5.33 In the Alexander-Spanier, de Rham, and singular cases we obtained a sheaf cohomology theory by exhibiting explicit fine torsionless resolutions of a constant sheaf, and we then proved that there were canonical isomorphisms of the classical cohomology modules with the sheaf cohomology modules. The Czech theory, by contrast, arises from a direct construction that does not involve finding a fine torsionless resolution of $\mathcal{X}$. We will define modules $\widetilde{H}^{q}(M,S)$ for $S$ a sheaf of $K$-modules over $M$, and show that the axioms 5.18 for a cohomology theory are satisfied. We again direct your attention to the comment in the introduction to this chapter that for much of the chapter, $M$ need not be a differentiable manifold. In particular, $M$ in this section need only be a paracompact Hausdorff space.

Let $\mathcal{U} = \{U_a\}$ be an open cover of $M$. A collection $(U_0, \ldots, U_q)$ of members of the cover such that $U_0 \cap \cdots \cap U_q \neq \varnothing$ will be called a $q$-simplex. If $\sigma = (U_0, \ldots, U_q)$ is a $q$-simplex, its support $|\sigma|$ is by definition

 $$ |\sigma|=U_{0}\cap\cdots\cap U_{q}. $$ 

The $i$th face of a $q$-simplex $\sigma = (U_0, \ldots, U_e)$ is the $(q-1)$ simplex $\sigma^i = (U_0, \ldots, U_{i-1}, U_{i+1}, \ldots, U_e)$. Let $C^q(\mathfrak{U},\mathfrak{S})$, for $q \geq 0$, be the $K$-module consisting of functions which assign to each $q$-simplex $\sigma$ an element of $\Gamma(\mathcal{S},|\sigma|)$, and let $C^q(\mathfrak{U},\mathcal{S}) = 0$ for $q < 0$. Elements of $C^q(\mathfrak{U},\mathcal{S})$ are called $q$-cochains. With a coboundary homomorphism

 $$ d\colon C^{\mathfrak{s}}(\mathfrak{U},\mathbb{S})\to C^{\mathfrak{s}+1}(\mathfrak{U},\mathbb{S}) $$ 

defined by

 $$ d f(\sigma)=\sum_{i=0}^{a}(-1)^{i}\rho_{|\sigma|,|\sigma^{i}|}f(\sigma^{i}), $$ 

one obtains a cochain complex $C^{*}(U,S)$ whose $q$th cohomology module, which we denote by $\tilde{H}^{q}(U,S)$, is called the $q$th $\tilde{C}_{\mathrm{ech}}$ cohomology module of $(M,U)$ with coefficients in $S$. A homomorphism $S\to S'$ induces by composition a cochain map $C^{*}(U,S)\to C^{*}(U,S')$ and thus induces homomorphisms

 $$ \check{H}^{q}(\mathfrak{U},\mathcal{S})\to\check{H}^{q}(\mathfrak{U},\mathcal{S}^{\prime}) $$ 

for each q.

A cochain $f$ belongs to $C^0(\mathcal{U},\mathcal{S})$ if and only if $f$ assigns to each open set $U_\alpha\in\mathcal{U}$ a section of $\mathcal{S}$ over $U_\alpha$. $f$ is a 0-cocycle, that is $df=0$, if and only if

 $$ 0=d f(U_{\alpha_{0}},U_{\alpha_{1}})=\rho_{U_{\alpha_{0}}\cap U_{\alpha_{1}},U_{\alpha_{1}}}f(U_{\alpha_{1}})-\rho_{U_{\alpha_{0}}\cap U_{\alpha_{1}},U_{\alpha_{0}}}f(U_{\alpha_{0}}) $$ 

for every 1-simplex $(U_{\alpha_0}, U_{\alpha_1})$. Thus $f$ is a 0-cocycle if and only if $f$ defines a global section of $S$ over $M$. Thus

 $$ \check{H}^{0}(\mathfrak{U},\mathcal{S})=\Gamma(\mathcal{S}). $$ 

We now consider the effect of refining the cover U. If a cover B is a refinement of the cover U, then there exists a map $\mu: \mathfrak{B} \to U$ such that $V \subseteq \mu(V)$ for each $V \in \mathfrak{B}$. If $\sigma = (V_0, \ldots, V_q)$ is a $q$-simplex of the cover B, then we let $\mu(\sigma)$ denote the $q$-simplex $(\mu(V_0), \ldots, \mu(V_q))$ of the cover U. Now, $\mu$ induces a cochain map $\mu: C^*(\mathfrak{U}, \mathfrak{S}) \to C^*(\mathfrak{B}, \mathfrak{S})$ if we set

 $$ \mu_{a}(f)(\sigma)=\rho_{|\sigma|,|\mu(\sigma)|}f\big(\mu(\sigma)\big) $$ 

for $f\in C^{q}(\mathfrak{U},\mathcal{S})$ and for $\sigma$ a $q$-simplex of the cover $\mathfrak{V}$. This cochain map induces homomorphisms

 $$ \mu_{q}^{*}\colon\check{H}^{q}(\mathfrak{U},\mathcal{S})\to\check{H}^{q}(\mathfrak{B},\mathcal{S}) $$ 

of the cohomology modules. We claim that if $\mu$ and $\tau$ are both refining maps of $\mathfrak{B}$ into $\mathfrak{U}$, then $\mu_{q}^{*}=\tau_{q}^{*}$ for each $q$. As usual, we prove this by finding a homotopy operator. If $\sigma=(V_{0},\ldots,V_{q-1})$ is a $(q-1)$ simplex of the cover $\mathfrak{B}$, we let

 $$ \tilde{\sigma}_{j}=\big(\mu(V_{0}),\ldots,\mu(V_{j}),\tau(V_{j}),\ldots,\tau(V_{q-1})\big). $$ 

We then define homomorphisms  $ h_{q}\colon C^{q}(\mathfrak{U},\mathfrak{S})\to C^{q-1}(\mathfrak{B},\mathfrak{S}) $ by setting

 $$ h_{q}(f)(\sigma)=\sum_{j=0}^{q-1}(-1)^{j}\rho_{|\sigma|,|\widetilde{\sigma}_{j}|}f(\widetilde{\sigma}_{j}). $$ 

From a straightforward calculation, one obtains

 $$ h_{a+1}\circ d+d\circ h_{a}=\tau_{a}-\mu_{a}, $$ 

from which it follows that $\mu_{q}^{*}=\tau_{q}^{*}$ for each integer $q$. Thus if $\mathfrak{B}$ is a refinement of $\mathfrak{U}$, which we shall denote by $\mathfrak{B}<\mathfrak{U}$, then there are canonical homomorphisms $\widetilde{H}^{q}(\mathfrak{U},\mathfrak{S})\to\widetilde{H}^{q}(\mathfrak{B},\mathfrak{S})$. Since the set of coverings of $M$ forms a directed set under the relation $<\mathfrak{f}$ refinement, and since if $\mathfrak{S}<\mathfrak{B}<\mathfrak{U}$ then the homomorphism $\widetilde{H}^{q}(\mathfrak{U},\mathfrak{S})\to\widetilde{H}^{q}(\mathfrak{S},\mathfrak{S})$ is the composition of the $\widetilde{H}^{q}(\mathfrak{U},\mathfrak{S})\to\widetilde{H}^{q}(\mathfrak{B},\mathfrak{S})$ and $\widetilde{H}^{q}(\mathfrak{B},\mathfrak{S})\to\widetilde{H}^{q}(\mathfrak{S},\mathfrak{S})$—then the

collection of modules  $ \tilde{H}^{\circ}(U,S) $ and refinement homomorphisms forms a direct system. Thus one can form the direct limit module

 $$ \check{H}^{a}(M,\mathcal{S})=\operatorname{d i r}_{\mathrm{~u~}}\operatorname*{l i m}\check{H}^{e}(\mathcal{U},\mathcal{S}). $$ 

(Construction is completely analogous to the construction of the module $\delta_{m}$ from the modules $S_{U}$ in 5.6.) $\tilde{H}^{q}(M,\mathfrak{S})$ is the $q$th $\tilde{C}$ech cohomology module for $M$ with coefficients in the sheaf of $K$-modules 8. The classical $q$th $\tilde{C}$ech cohomology module $\tilde{H}^{q}(M;G)$ of $M$ with coefficients in a $K$-module $G$ is by definition $\tilde{H}^{q}(M,\mathcal{G})$, where $\mathcal{G}$ is the constant sheaf $M\times G$.

We shall now show that the Čech cohomology modules (12) give a sheaf cohomology theory in the sense of 5.18. It is apparent that  $ \tilde{H}^{e}(M,\mathcal{S})=0 $ for  $ q<0 $, and it follows from (6) that  $ \tilde{H}^{e}(M,\mathcal{S})=\Gamma(\mathcal{S}) $; thus 5.18(a) is satisfied. The homomorphisms (4) induced from a homomorphism  $ \mathcal{S}\to\mathcal{S}^{\prime} $ commute with the refinement homomorphisms (8) and thus induce homomorphisms

 $$ \check{H}^{a}(M,\mathcal{S})\to\check{H}^{a}(M,\mathcal{S}^{\prime}). $$ 

It is immediate that these homomorphisms satisfy 5.18(d) and (e).

Consider now a fine sheaf $8$ and an integer $q > 0$. Since every cover of $M$ has a locally finite refinement, in order to prove that $\tilde{H}^{q}(U,8) = 0$, it suffices to prove that $\tilde{H}^{q}(U,8) = 0$ for each locally finite open cover $U$. Let $\{I_{a}\}$ be a partition of unity for $8$ subordinate to the locally finite open cover $U = \{U_{a}\}$ of $M$. We shall define homomorphisms $h_{p}: C^{p}(U,8) \to C^{p-1}(U,8)$ for each $p \geq 1$. Let $f \in C^{p}(U,8)$, and let $\sigma = (U_{0}, \ldots, U_{p-1})$ be a $(p-1)$ simplex of the cover $U$. Then $l_{a} \circ (f(U_{0}, U_{0}, \ldots, U_{p-1}))$ has support in $U_{a} \cap U_{0} \cap \cdots \cap U_{p-1}$, so we can extend $l_{a} \circ (f(U_{a}, U_{0}, \ldots, U_{p-1}))$ to a continuous section of $8$ over $U_{0} \cap \cdots \cap U_{p-1}$ by extending it to be zero outside $U_{a} \cap U_{0} \cap \cdots \cap U_{p-1}$. We consider $I_{a} \circ (f(U_{a}, U_{0}, \ldots, U_{p-1}))$ as this section over $U_{0} \cap \cdots \cap U_{p-1}$. Now define

 $$ h_{p}(f)(\sigma)=\sum_{a}l_{a}\circ\big(f(U_{a},U_{0},\ldots,U_{p-1})\big). $$ 

It follows that

 $$ d\circ h_{p}+h_{p+1}\circ d=\operatorname{id}\qquad\mathrm{for}p\geq1. $$ 

So if $f$ is a $q$-cocycle with $q>0$, then there is a $(q-1)$ cochain $g$, namely $g=h_e(f)$, such that $dg=f$. It follows that $\tilde{H}^q(\mathfrak{U},\mathfrak{S})=0$. Thus axiom 5.18(b) is satisfied.

A short exact sheaf sequence  $ 0 \to \mathcal{S}' \to \mathcal{S} \to \mathcal{S}'' \to 0 $ induces exact sequences

 $$ 0\to C^{q}(\mathfrak{U},\mathcal{S}^{\prime})\to C^{q}(\mathfrak{U},\mathcal{S})\to C^{q}(\mathfrak{U},\mathcal{S}^{\prime\prime}). $$ 

Let  $ \tilde{C}^q(U,S^*) $ be the image of  $ C^q(U,S) $ in  $ C^q(U,S^*) $. Then the short exact sequences

 $$ 0\to C^{q}(\mathfrak{U},\mathcal{S}^{\prime})\to C^{q}(\mathfrak{U},\mathcal{S})\to\bar{C}^{q}(\mathfrak{U},\mathcal{S}^{\prime\prime})\to0 $$ 

yield a short exact sequence of cochain complexes

 $$ 0\to C^{*}(\mathfrak{U},\mathcal{S}^{\prime})\to C^{*}(\mathfrak{U},\mathcal{S})\to\bar{C}^{*}(\mathfrak{U},\mathcal{S}^{\prime})\to0. $$ 

A refining map $\mu\colon\mathfrak{B}\to\mathfrak{U}$ induces a homomorphism of short exact sequences of cochain complexes

 $$ \begin{aligned}{0\to C^{*}(\mathfrak{U},\mathfrak{S}^{\prime})}&{{}\to C^{*}(\mathfrak{U},\mathfrak{S})\to\bar{C}^{*}(\mathfrak{U},\mathfrak{S}^{\prime\prime})\to0}\\ {\downarrow^{\mu}}&{{}\quad\downarrow^{\mu}\quad\downarrow^{\mu}}\\ {0\to C^{*}(\mathfrak{B},\mathfrak{S}^{\prime})}&{{}\to C^{*}(\mathfrak{B},\mathfrak{S})\to\bar{C}^{*}(\mathfrak{B},\mathfrak{S}^{\prime\prime})\to0}\\ \end{aligned} $$ 

and thus by 5.17 induces a commutative diagram of the associated cohomology sequences

(20)

 $$ \begin{array}{c}\cdots\rightarrow\bar{H}^{q-1}(\mathfrak{U},\mathfrak{S}^{n})\xrightarrow{\partial}\check{H}^{q}(\mathfrak{U},\mathfrak{S}^{\prime})\rightarrow\check{H}^{q}(\mathfrak{U},\mathfrak{S})\rightarrow\bar{H}^{q}(\mathfrak{U},\mathfrak{S}^{n})\xrightarrow{\partial}\check{H}^{q+1}(\mathfrak{U},\mathfrak{S}^{\prime})\rightarrow\cdots\\\left\downarrow\right._{\mathfrak{q}-1}^{\mu_{q}^{*}}\left\downarrow\right._{\mathfrak{q}}\left\downarrow\right._{\mathfrak{q}^{*}}\left\downarrow\right._{\mathfrak{q}}\left\downarrow\right._{\mathfrak{q}^{*}}\left\downarrow\right._{\mathfrak{q}+1}^{\mu_{q}^{*}}\\\cdots\rightarrow\bar{H}^{q-1}(\mathfrak{B},\mathfrak{S}^{n})\xrightarrow{\partial}\check{H}^{q}(\mathfrak{B},\mathfrak{S}^{\prime})\rightarrow\check{H}^{q}(\mathfrak{B},\mathfrak{S})\rightarrow\bar{H}^{q}(\mathfrak{B},\mathfrak{S}^{n})\xrightarrow{\partial}\check{H}^{q+1}(\mathfrak{B},\mathfrak{S}^{\prime})\rightarrow\cdots\ .\\\end{array} $$ 

On passing to the direct limit, we obtain a long exact sequence

 $$ \begin{aligned}\cdots\longrightarrow\bar{H}^{q-1}(M,\mathcal{S}^{n})&\xrightarrow{\partial}\bar{H}^{q}(M,\mathcal{S}^{\prime})\\&\longrightarrow\check{H}^{q}(M,\mathcal{S})\longrightarrow\bar{H}^{q}(M,\mathcal{S}^{n})\xrightarrow{\partial}\check{H}^{q+1}(M,\mathcal{S}^{\prime})\longrightarrow\cdots.\end{aligned} $$ 

We shall now prove that the inclusion cochain map  $ \tilde{C}^*(\mathfrak{U},\mathfrak{S}^*) \to C^*(U,\mathfrak{S}^*) $ on passage to the direct limit in cohomology induces isomorphism

 $$ \tilde{H}^{q}(M,\mathcal{S}^{\prime\prime})\xrightarrow{\simeq}\check{H}^{q}(M,\mathcal{S}^{\prime\prime}). $$ 

These isomorphisms, together with (21), will then yield a long exact sequence

 $$ \begin{aligned}\cdots\longrightarrow\check{H}^{q-1}(M,\mathcal{S}^{n})&\xrightarrow{\partial}\check{H}^{q}(M,\mathcal{S}^{\prime})\\ \longrightarrow\check{H}^{q}(M,\mathcal{S})&\longrightarrow\check{H}^{q}(M,\mathcal{S}^{n})\xrightarrow{\partial}\check{H}^{q+1}(M,\mathcal{S}^{\prime})\longrightarrow\cdots,\end{aligned} $$ 

which proves axiom 5.18(c). The quotient modules

 $$ \tilde{C}^{\alpha}(\mathfrak{U})=C^{\alpha}(\mathfrak{U},\delta^{\prime\prime})/(\tilde{C}^{\alpha}(\mathfrak{U},\delta^{\prime\prime}) $$ 

together with the induced coboundary homomorphisms form a cochain complex  $ \tilde{C}^{*}(U) $ such that

 $$ 0\to\tilde{C}^{*}(\mathfrak{U},\mathfrak{S}^{\prime})\to C^{*}(\mathfrak{U},\mathfrak{S}^{\prime})\to\tilde{C}^{*}(\mathfrak{U})\to0 $$ 

is exact. It follows from the long exact cohomology sequence for (25), upon passage to the direct limit, that (22) will follow if we prove that the direct limit of the modules  $ H^q(\widetilde{C}^*(U)) $ is 0 for all q. So let U be a locally finite cover of M. That the direct limit of the modules  $ H^q(\widetilde{C}^*(U)) $ is 0 will certainly follow if we prove that for an arbitrary  $ f \in C^q(U, S^*) $ there is a refinement  $ \mu: \mathfrak{B} \to U $ such that  $ \mu_q(f) \in \widetilde{C}^q(\mathfrak{B}, S^*) $. Choose a refinement  $ \mathfrak{D} = \{O_q\} $ of  $ U = \{U_q\} $ such that  $ O_q \subset U_q $ for each  $ \alpha $. For each  $ p \in M $ choose a neighborhood  $ V_p $ such that

(a)  $ V_{p} \subset O_{a} $ for some a.

(b) If  $ V_{p} \cap O_{a} \neq \varnothing $, then  $ V_{p} \subset U_{a} $.

(c)  $ V_{p} $ lies in the intersection of the  $ U_{a} $ containing  $ p $.

(d) If $\sigma$ is a $q$-simplex of the cover $\mathfrak{U}$, and $p\in|\sigma|$ (so $V_{p}\subset|\sigma|$), then $\rho_{V_{p},|\sigma|}f(\sigma)$ is the image of a section of $\delta$ over $V_{p}$.

It is possible to satisfy (d) since there are only finitely many $q$-simplices of the cover $\mathfrak{U}$ which contain $p$. Now let $\mathfrak{B}$ be the cover $\{V_p\}$, and for every $p$ choose $O_p \in \mathfrak{U}$ and $U_p \in \mathfrak{U}$ such that $V_p \subset O_p \subset U_p$. Thus we have a refinement $\mu: \mathfrak{B} \to \mathfrak{U}$. Now let $\sigma = (V_{p_0}, \ldots, V_{p_q})$ be a $q$-simplex of the cover $\mathfrak{B}$. Then $V_{p_0} \cap O_{p_q} \neq \varnothing$, $0 \leq i \leq q$, so by (b), $V_{p_0} \subset U_{p_q}$. Thus $V_{p_0} \subset U_{p_q} \cap \cdots \cap U_{p_q} = |\mu(\sigma)|$. Therefore

 $$ \begin{aligned}{\mu_{q}(f)(\sigma)}&{{}=\rho_{|\sigma|,|\mu(\sigma)|}f(U_{y_{0}},\ldots,U_{y_{e}})}\\ {}&{{}=\rho_{|\sigma|,\mathcal{V}_{y_{0}}}\circ\rho_{\mathcal{V}_{y_{0}},|\mu(\sigma)|}f(U_{y_{0}},\ldots,U_{y_{e}});}\\ \end{aligned} $$ 

hence by condition (d),  $ \mu_{q}(f) \in \tilde{C}^{q}(\mathfrak{B},\mathfrak{S}^{n}) $.

Finally, axiom 5.18(f) follows readily from the above construction of (23) by making use of 5.17(3).

Thus the Čech cohomology satisfies the axioms 5.18 for a sheaf cohomology theory.

##### THE DE RHAM THEOREM

5.34 Convention Since according to the corollary of 5.23, any two sheaf cohomology theories on $M$ are uniquely isomorphic, we shall consider them as identified via their unique isomorphism, and shall henceforth use $H^{p}(M,8)$ to denote the $p$th cohomology module of $M$ with coefficients in the sheaf 8. With this convention,

 $$ H^{\flat}(M,\mathbb{s})=\check{H}^{\flat}(M,\mathbb{s}); $$ 

and given any fine torsionless resolution

 $$ 0\to\mathcal{H}\to\mathcal{C}_{0}\to\mathcal{C}_{1}\to\mathcal{C}_{3}\to\cdots, $$ 

we have

 $$ H^{\mathfrak{p}}(M,\mathbb{s})=H^{\mathfrak{p}}\big(\Gamma(\mathcal{C}^{\ast}\otimes\mathbb{s})\big). $$ 

5.35 In the preceding sections we have obtained canonical isomorphisms

 $$ H_{\pmb{A}-\pmb{S}}^{\mathfrak{p}}(M;\pmb{G})\cong H_{\Delta}^{\mathfrak{p}}(M;\pmb{G})\cong H_{\Delta}^{\mathfrak{p}}\infty(M;\pmb{G})\cong\check{H}^{\mathfrak{p}}(M;\pmb{G}) $$ 

of the classical Alexander-Spanier, singular, differentiable singular, and Czech cohomology modules of a differentiable manifold $M$ with coefficients in a $K$-module $G$ over a principal ideal domain $K$. We have seen that each of these is canonically isomorphic with the sheaf cohomology module $H^{p}(M,\mathcal{G})$ with coefficients in the constant sheaf $\mathcal{G}$. If we take $K$ to be the field of real numbers, we can add the de Rham cohomology group $H_{\mathrm{de}}^{p}(M)$ to the above list of isomorphisms. In particular, we have canonical isomorphisms

 $$ H_{\mathbf{d e}\mathbf{R}}^{{v}}(M)\cong H^{{v}}(M,\mathcal{R})\cong H_{\Delta}^{\mathbf{v}}\infty(M;\mathbb{R}). $$ 

We shall now prove, with the help of 5.24, that the explicit homomorphism from the de Rham to the differentiable singular cohomology theory obtained from integration of forms over differentiable singular simplices yields the canonical isomorphism (2).

We define homomorphisms

 $$ k_{p}\colon E^{p}(M)\to S_{\infty}^{p}(M,\mathbb{R}) $$ 

for each integer  $ p \geq 0 $ by setting

 $$ k_{p}(\omega)(\sigma)=\int_{\sigma}\omega $$ 

for each differentiable $p$-form $\omega$ on $M$ and differentiable singular $p$-simplex $\sigma$ in $M$. It is an immediate consequence of Stokes' theorem 4.7 that the homomorphisms $k_{p}$ induce a cochain map

 $$ k\colon E^{*}(M)\to S_{\infty}^{*}(M,\mathbb{R}). $$ 

Let

 $$ k_{\mathfrak{p}}^{*}\colon H_{\tt d e R}^{\mathfrak{p}}(M)\to H_{\Delta}^{\mathfrak{p}}\infty(M;\mathbb{R}) $$ 

denote the induced homomorphism of the cohomology modules (real vector spaces).  $ k_{p}^{*} $ is called the de Rham homomorphism.

5.36 The de Rham Theorem The de Rham homomorphism  $ k_{p}^{*} $ is the canonical isomorphism 5.35(2) for each integer p.

PROOF The homomorphisms 5.35(3) can be defined for arbitrary open sets in M, and yield presheaf homomorphisms

 $$ \{E^{v}(U);\rho_{U,V}\}\xrightarrow{k_{p}}\{S_{\infty}^{v}(U,\mathbb{R});\rho_{U,V}\} $$ 

which commute, by Stokes' theorem, with the coboundary homomorphisms 5.28(2) and 5.31(10). Thus the induced homomorphisms of the associated sheaves form a commutative diagram:

 $$ \begin{array}{c}0\to\mathcal{R}\longrightarrow\mathcal{E}^{0}(M)\longrightarrow\mathcal{E}^{1}(M)\longrightarrow\mathcal{E}^{2}(M)\quad\to\cdots\\\downarrow\downarrow\downarrow\downarrow\downarrow\downarrow k_{0}\downarrow k_{1}\downarrow k_{2}\\0\to\mathcal{R}\to\mathcal{S}^{0}_{\infty}(M,\mathbb{R})\to\mathcal{S}^{1}_{\infty}(M,\mathbb{R})\to\mathcal{S}^{2}_{\infty}(M,\mathbb{R})\to\cdots.\end{array} $$ 

Consider now the following commutative diagram of cochain complexes in which the rows, according to 5.30(5) and 5.32(2), are exact:

 $$ \begin{array}{r l r}&{}&{0\longrightarrow E^{*}(M)\stackrel{\textcircled{\scriptsize{I}}{\longmapsto}}{\longrightarrow}\Gamma\big(\mathcal{E}^{*}(M)\big)\longrightarrow0}\\ &{}&{0\to S_{\infty,0}^{*}(M,\mathbb{R})\to S_{\infty}^{*}(M,\mathbb{R})\stackrel{\downarrow\quad\kappa}{\to}\Gamma\big(\mathcal{S}_{\infty}^{*}(M,\mathbb{R})\big)\to0.}\end{array} $$ 

The cochain map ① induces the isomorphism $\mathcal{H}_{\mathfrak{d}\in\mathbf{R}}^{p}(M)\cong\mathcal{H}^{p}(M,\mathscr{R})$. We proved in 5.32(4) that ② induces the isomorphism $H_{\mathfrak{A}^{\infty}}^{p}(M;\mathbb{R})\cong H^{p}(M,\mathscr{R})$. That ③ induces isomorphism on cohomology follows from the corollary of 5.23 applied to the isomorphism of sheaf cohomology theories induced according to 5.24 by the isomorphism (1) of fine torsionless resolutions of $\mathscr{R}$. Thus from the uniqueness of the isomorphism between sheaf cohomology theories, ③ induces the identity isomorphism of $H^{p}(M,\mathscr{R})$. It follows that $k_{p}^{*}$ is the canonical isomorphism 5.35(2) for each integer $p$.

5.37 Earlier, in 4.17, we stated a slightly different version of the de Rham theorem in terms of singular homology instead of cohomology. We shall now see that there is a natural isomorphism

 $$ H_{\Delta}^{\mathfrak{p}}\propto(M;\mathbb{R})\to_{\infty}H_{\mathfrak{p}}(M;\mathbb{R})^{*} $$ 

which composed with $k_{p}^{*}$ yields the isomorphism 4.17(1). (For the definition of the real differentiable singular homology group $\infty H_{p}(M;\mathbb{R})$ and other relevant notation, the reader should review section 4.16.) The map (1) is defined as follows. If $f$ represents a cohomology class in $H_{A}^{\mathfrak{p}}(\mathfrak{M};\mathbb{R})$.

then $f$ can be considered as a linear function on the vector space $\omega S_p(M;\mathbb{R})$ of real differentiable singular $p$-chains in $M$. In particular, $f$ is a linear function on the subspace of $\omega S_p(M;\mathbb{R})$ consisting of the $p$-cycles, and $f$ vanishes on the $p$-boundaries in $\omega S_p(M;\mathbb{R})$ since $df=0$; hence $f$ determines a linear function on the homology group $\omega H_p(M;\mathbb{R})$. Since a real differentiable singular coboundary necessarily vanishes on all $p$-cycles, each cohomology class in $H_\infty^\infty(M;\mathbb{R})$ determines a well-defined element of $\omega H_p(M;\mathbb{R})^{*}$ independent of the representative $f$ chosen. This defines the map (1). We leave it to the reader as an exercise to establish that (1) is actually an isomorphism. Clearly the composition of (1) with $k_p^{*}$ is exactly the homology $\mathbb{R}^p$ (1.1). Thus $4.17(1)$ is an isomorphism.

5.38 Remark The singular cohomology groups $H_{\Delta}^{p}(M;\mathbb{R})$ are topological invariants; that is, homeomorphic spaces have isomorphic real singular cohomology (see Exercise 19). As a consequence of this and the isomorphism 5.35(1) and (2), the de Rham cohomology groups are also topological invariants of a differentiable manifold.

##### MULTIPLICATIVE STRUCTURE

In the case in which $\mathcal{S}$ is a sheaf of $K$-algebras over $M$, we shall make the direct sum of the cohomology modules $\sum H^{p}(M,\mathcal{S})$ into an associative algebra over $K$. But first we need a few preliminary constructions.

5.39 Definitions Let $C^*$ and $C^*$ be cochain complexes. Their tensor product $C^* \otimes C^*$ is the cochain complex whose $r$th module is the direct sum

 $$ \sum_{\mathfrak{p}+q=\tau}C_{\mathfrak{p}}\otimes{^{\prime}C}_{\mathfrak{q}}, $$ 

and whose rth coboundary homomorphism is the direct sum

 $$ \sum_{p+q=r}\big(d_{p}\otimes\mathbf{\Sigma}^{\prime}(\mathtt{i d})_{q}+(-1)^{p}(\mathtt{i d})_{p}\otimes\mathbf{\Sigma}^{\prime}d_{q}\big). $$ 

If $\sigma \in Z^p(C^*)$ and $\tau \in Z^q(^{\prime}C^*)$, then $\sigma \otimes \tau \in Z^{p+q}(C^* \otimes^{\prime}C^*)$; whereas if $\sigma \in B^p(C^*)$ and $\tau \in Z^q(^{\prime}C^*)$ (or vice versa, if $\sigma \in Z^p(C^*)$ and $\tau \in B^q(^{\prime}C^*)$), then $\sigma \otimes \tau \in B^{p+q}(C^* \otimes^{\prime}C^*)$. Thus there is a well-defined homomorphism

 $$ H^{p}(C^{*})\otimes H^{q}(^{\prime}C^{*})\to H^{p+q}(C^{*}\otimes^{\prime}C^{*}). $$ 

5.40 Lemma The tensor product of two torsionless K-modules, for K a principal ideal domain, is again a torsionless K-module.

PROOF Let $\lambda \neq 0 \in K$, and let $K/\lambda$ be the $K$-module whose elements are $\{k/\lambda: k \in K\}$, and in which addition and multiplication by $K$ are defined by

 $$ k_{2}/\lambda+k_{2}/\lambda=(k_{1}+k_{8})/\lambda, $$ 

 $$ k(k_{1}/\lambda)=k k_{1}/\lambda. $$ 

Let A be a K-module. We define a sequence of homomorphisms

 $$ A\to K/\lambda\otimes A\to K\otimes A\to A. $$ 

The first homomorphism is defined by $a \mapsto (\lambda / \lambda) \otimes a$, the second by $\sum (k_i / \lambda) \otimes a_i \mapsto \sum k_i \otimes a_i$, and the third by $\sum k_i \otimes a_i \mapsto \sum k_i a_i$. The second homomorphism obviously has an inverse, so is an isomorphism; and the third is an isomorphism according to 5.9(2). The composition (2) sends $a \in A$ to $\lambda a \in A$. By definition, $A$ is torsionless if and only if the composition (2) has kernel zero for each $\lambda \neq 0 \in K$. Thus $A$ is torsionless if and only if

 $$ 0\to A\to(K/\lambda)\otimes A $$ 

is exact for each $\lambda \neq 0 \in K$. Now let $A$ and $B$ be torsionless $K$-modules, and let $\lambda \neq 0 \in K$. Then (3) is exact, and so since $B$ is torsionless it follows from 5.14 that

 $$ 0\to A\otimes B\to(K/\lambda)\otimes A\otimes B $$ 

is exact, whence $A\otimes B$ is torsionless.

5.41 Definition The definitions of the direct sum $S\oplus\mathcal{T}$ of sheaves and the direct sum $S\oplus\mathcal{T}\to S\oplus\mathcal{T}^{\prime}$ of sheaf homomorphisms $S\to S^{\prime}$ and $\mathcal{T}\to\mathcal{T}^{\prime}$ are obtained by replacing $\otimes$ by $\oplus$ in $5.9(3)-(8)$, with the deletion of 5.9(7). Observe that the direct sum of fine sheaves is a fine sheaf.

### 5.42 The Multiplicative Structure Consider a resolution

 $$ 0\to\mathcal{H}\to\mathcal{C}_{0}\xrightarrow{d_{0}}\mathcal{C}_{1}\xrightarrow{d_{1}}\mathcal{C}_{2}\xrightarrow{d_{2}}\cdots. $$ 

By the tensor product of the resolution (1) with itself we mean the sequence

 $$ \begin{aligned}{0\to\mathcal{K}\to\mathcal{C}_{0}\otimes\mathcal{C}_{0}\to(\mathcal{C}_{0}\otimes\mathcal{C}_{1})\oplus(\mathcal{C}_{1}\otimes\mathcal{C}_{0})}&{{}\to\cdots}\\ {}&{{}\cdots\to\sum_{p+q=r}\mathcal{C}_{p}\otimes\mathcal{C}_{q}\to\cdots}\\ \end{aligned} $$ 

in which the homomorphism $\mathcal{H}\to\mathcal{C}_{0}\otimes\mathcal{C}_{0}$ is the composition $\mathcal{H}\cong\mathcal{H}\otimes\mathcal{H}\to\mathcal{C}_{0}\otimes\mathcal{C}_{0}$, and in which the homomorphism whose domain is $\sum\mathcal{C}_{p}\otimes\mathcal{C}_{q}$ is the direct sum

 $$ \sum_{p+q=r}\bigl(d_{p}\otimes(\mathtt{i d})_{q}+(-1)^{v}(\mathtt{i d})_{p}\otimes d_{q}\bigr). $$ 

If (1) is a fine torsionless resolution of $\mathcal{H}$, we claim that (2) is also a fine torsionless resolution of $\mathcal{H}$. That the sheaves in (2) are fine is a consequence of the fact that tensor products and direct sums of fine sheaves are also fine sheaves. From 5.40 and the observation that direct sums of torsionless $K$-modules are torsionless, it follows that the sheaves in (2) are torsionless. That (2) is exact, therefore a resolution, is easily seen at $\mathcal{H}$ and at $\mathcal{C}_0 \otimes \mathcal{C}_0$, and is proved elsewhere by applying the Kunneth formula to the cochain complexes obtained for each $m \in M$ from

 $$ \begin{array}{r l r}{4)}&{\;\cdots\;\to\;0\to\mathcal{C}_{0}\otimes\mathcal{C}_{0}\to(\mathcal{C}_{0}\otimes\mathcal{C}_{1})\oplus(\mathcal{C}_{1}\otimes\mathcal{C}_{0})\to\cdots}&\\ &{}&{\quad\cdots\to\displaystyle\sum_{p+q=r}\mathcal{C}_{p}\otimes\mathcal{C}_{q}\to\cdots}\end{array} $$ 

by restricting to the stalks over m. The extensive algebra necessary for a proof of the Kunneth formula, which expresses the cohomology of the tensor product of cochain complexes in terms of the cohomology of the individual complexes, would not be particularly illuminating for our purposes, so we shall simply refer the interested reader to Spanier [28, Ch. 5, §4, THEOREM 2], where the Kunneth formula is proved in detail.

Let $\mathcal{S}$ be a sheaf over $M$. From the resolution (2) we obtain as in 5.19(2) a cochain complex which we shall denote by $\Gamma(\mathcal{C}^*\otimes\mathcal{C}^*\otimes\mathcal{S})$. If $\mathcal{S}$ is a sheaf of algebras over $M$, then the natural homomorphism $\mathcal{S}\otimes\mathcal{S}\to\mathcal{S}$ determined by the multiplicative structure of the stalks induces homomorphisms

 $$ (5)\quad\Gamma(\mathcal{C}_{{p}}\otimes\mathcal{S})\otimes\Gamma(\mathcal{C}_{{q}}\otimes\mathcal{S})\to\Gamma(\mathcal{C}_{{p}}\otimes\mathcal{C}_{{q}}\otimes\mathcal{S}\otimes\mathcal{S})\to\Gamma(\mathcal{C}_{{p}}\otimes\mathcal{C}_{{q}}\otimes\mathcal{S}) $$ 

which in turn induce a cochain map

 $$ \Gamma(\mathcal{C}^{*}\otimes\mathcal{S})\otimes\Gamma(\mathcal{C}^{*}\otimes\mathcal{S})\to\Gamma(\mathcal{C}^{*}\otimes\mathcal{C}^{*}\otimes\mathcal{S}). $$ 

We have, according to 5.39(3), a well-defined homomorphism

 $$ H^{p}(M,\mathcal{S})\otimes H^{q}(M,\mathcal{S})\to H^{p+q}\big(\Gamma(\mathcal{C}^{*}\otimes\mathcal{S})\otimes\Gamma(\mathcal{C}^{*}\otimes\mathcal{S})\big). $$ 

In the case in which 8 is a sheaf of algebras over M, the cochain map (6) induces, together with (7), a homomorphism

 $$ H^{p}(M,\mathcal{S})\otimes H^{q}(M,\mathcal{S})\to H^{p+q}(M,\mathcal{S}). $$ 

This will define the multiplicative structure in sheaf cohomology. But first we need to show that the multiplication defined by (8) is independent of the resolution (1) with which we began. Consider another fine torsionless resolution

 $$ 0\to\mathcal{H}\to\widetilde{\mathcal{C}}_{0}\to\widetilde{\mathcal{C}}_{1}\to\widetilde{\mathcal{C}}_{2}\to\cdots. $$ 

By censoring the resolution (1) with the resolution (9) (construction completely analogous to the tensor product of (1) with itself given in (2) and (3)),

we obtain another fine torsionless resolution

 $$ \begin{aligned}{0\to\mathcal{K}\to\mathcal{C}_{0}\otimes\widetilde{\mathcal{C}}_{0}\to(\mathcal{C}_{0}\otimes\widetilde{\mathcal{C}}_{1})\oplus(\mathcal{C}_{1}\otimes\widetilde{\mathcal{C}}_{0})}&{{}\to\cdots}\\ {}&{{}\cdots\to\sum_{p+q=r}\mathcal{C}_{p}\otimes\widetilde{\mathcal{C}}_{q}\to\cdots.}\\ \end{aligned} $$ 

A homomorphism of the resolution (1) to the resolution (10), in the sense of 5.24, is generated by the homomorphisms

 $$ \mathcal{C}_{p}\cong\mathcal{C}_{p}\otimes\mathcal{N}\to\mathcal{C}_{p}\otimes\widetilde{\mathcal{C}}_{0}\to\sum_{r+s=p}\mathcal{C}_{r}\otimes\widetilde{\mathcal{C}}_{s}, $$ 

where the last map is inclusion. This homomorphism of resolutions induces a cochain map $\Gamma(\mathcal{C}^* \otimes \mathcal{S}) \to \Gamma(\mathcal{C}^* \otimes \mathcal{C}^* \otimes \mathcal{S})$ which, according to 5.24 and the corollary of 5.23, induces the identity map $H^q(M, \mathcal{S}) \to H^q(M, \mathcal{S})$. By applying these constructions to various resolutions and then tensoring resulting cochain complexes, one obtains a commutative diagram of cochain complexes and cochain maps

 $$ \begin{array}{c}\Gamma(\mathcal{C}^{*}\otimes\mathfrak{S})\quad\otimes\Gamma(\mathcal{C}^{*}\otimes\mathfrak{S})\quad\xrightarrow{\quad\quad\quad}\Gamma(\mathcal{C}^{*}\otimes\mathcal{C}^{*}\otimes\mathfrak{S})\\\downarrow\quad\downarrow\\\Gamma(\mathcal{C}^{*}\otimes\widetilde{\mathcal{C}}^{*}\otimes\mathfrak{S})\otimes\Gamma(\mathcal{C}^{*}\otimes\widetilde{\mathcal{C}}^{*}\otimes\mathfrak{S})\xrightarrow{\quad\quad\quad}\Gamma(\mathcal{C}^{*}\otimes\widetilde{\mathcal{C}}^{*}\otimes\mathcal{C}^{*}\otimes\widetilde{\mathcal{C}}^{*}\otimes\mathfrak{S})\\\uparrow\quad\downarrow\\\Gamma(\widetilde{\mathcal{C}}^{*}\otimes\mathfrak{S})\otimes\Gamma(\widetilde{\mathcal{C}}^{*}\otimes\mathfrak{S})\quad\xrightarrow{\quad\quad\quad}\Gamma(\widetilde{\mathcal{C}}^{*}\otimes\widetilde{\mathcal{C}}^{*}\otimes\mathfrak{S})\\\end{array} $$ 

from which is induced the following commutative diagram on cohomology:

 $$ \begin{array}{l}(12)\underbrace{\phantom{H^{p}(M,\mathcal{S})}\rightarrow H^{p+q}\big(\Gamma(\mathcal{C}^{*}\otimes\mathcal{S})\otimes\Gamma(\mathcal{C}^{*}\otimes\mathcal{S})\big)}_{\downarrow}\quad\underbrace{\phantom{H^{p}(M,\mathcal{S})}\rightarrow H^{p+q}}_{}H^{p}(M,\mathcal{S})\otimes H^{q}(M,\mathcal{S})\to H^{p+q}\big(\Gamma(\mathcal{C}^{*}\otimes\widetilde{\mathcal{C}}^{*}\otimes\mathcal{S})\otimes\Gamma(\mathcal{C}^{*}\otimes\widetilde{\mathcal{C}}^{*}\otimes\mathcal{S})\big)\to H^{p+q}(M,\mathcal{S})}\\ {\quad\uparrow}\\ {\quad\rightarrow H^{p+q}\big(\Gamma(\widetilde{\mathcal{C}}^{*}\otimes\mathcal{S})\otimes\Gamma(\widetilde{\mathcal{C}}^{*}\otimes\mathcal{S})\big)}\end{array} $$ 

From (12) it follows that the multiplicative structure (8) is independent of the choice of (1).

It follows from the construction of (8) and the associativity of tensor products that the multiplicative structure induced on $\sum H^{p}(M,S)$ by (8) is associative. Thus (8) makes $\sum H^{p}(M,S)$ into an associative algebra over $K$.

The homomorphisms  $ \mathcal{C}_{p} \otimes \mathcal{C}_{q} \to \mathcal{C}_{q} \otimes \mathcal{C}_{p} $ defined by  $ c_{p} \otimes c_{q} \to (-1)^{pq} c_{q} \otimes c_{p} $ induce a homomorphism of the resolution (2) with itself in the sense of 5.24. According to 5.24, this homomorphism of (2) induces a homomorphism of cohomology theories which by the corollary of 5.23 must

be the identity isomorphism. But the induced homomorphism  $ H^{p+q}(M,S) \to H^{p+q}(M,S) $ sends  $ u \cdot v $ into  $ (-1)^{pq}v \cdot u $ if  $ u \in H^p(M,S) $ and  $ v \in H^q(M,S) $. Thus the multiplicative structure of  $ \sum_p H^p(M,S) $ satisfies the anti-commutative relation

 $$ u\cdot v=(-1)^{p q}v\cdot u\qquad\big(u\in H^{p}(M,\mathbb{S});v\in H^{q}(M,\mathbb{S})\big). $$ 

5.43 The de Rham Cohomology Algebra Exterior multiplication of differential forms induces, by mapping  $ \sigma \otimes \alpha \mapsto \sigma \wedge \alpha $, a cochain map

 $$ E^{*}(M)\otimes E^{*}(M)\xrightarrow{\wedge}E^{*}(M) $$ 

which together with the natural homomorphisms

 $$ H_{\mathtt{d e R}}^{\mathfrak{p}}(M)\otimes H_{\mathtt{d e R}}^{\mathfrak{q}}(M)\to H^{\mathfrak{p}+\mathfrak{q}}\big(E^{\ast}(M)\otimes E^{\ast}(M)\big) $$ 

of 5.39(3) induces homomorphisms

 $$ H_{\mathtt{d e R}}^{\mathfrak{p}}(M)\otimes H_{\mathtt{d e R}}^{\mathfrak{q}}(M)\to H_{\mathtt{d e R}}^{\mathfrak{p}+\mathfrak{q}}(M), $$ 

which make the direct sum $\sum H_{deR}^{p}(M)$ into an associative algebra over $\mathbb{R}$. This is the classical multiplicative structure in de Rham cohomology. Now, $\sum H_{deR}^{p}(M)$ also inherits an associative algebra structure from the algebra structure 5.42(8) in sheaf cohomology via the canonical isomorphism

 $$ \sum_{\mathfrak{p}}H_{\mathrm{d e R}}^{\mathfrak{p}}(M)\cong\sum_{\mathfrak{p}}H^{\mathfrak{p}}(M,\mathscr{R}). $$ 

We shall now prove that these two algebra structures on $\sum_{p} H_{\mathrm{de}_{\mathrm{R}}}^{p}(M)$ are identical. For each open set $U \subset M$, exterior multiplication induces homomorphisms

 $$ E^{p}(U)\otimes E^{q}(U)\to E^{p+q}(U) $$ 

which commute with appropriate restrictions and thus yield presheaf homomorphisms

 $$ \left\{E^{p}(U);\rho_{U,V}\right\}\otimes\left\{E^{q}(U);\rho_{U,V}\right\}\to\left\{E^{p+q}(U);\rho_{U,V}\right\} $$ 

which in turn induce sheaf homomorphisms

 $$ \mathcal{E}^{\mathfrak{v}}(M)\otimes\mathcal{E}^{\mathfrak{q}}(M)\to\mathcal{E}^{\mathfrak{v}+q}(M). $$ 

The homomorphisms (6) induce, as is easily checked, a homomorphism (in the sense of 5.24) of the tensor product of the resolution 5.28(3) with itself into itself:

\[\begin{array}{l}0\to\mathcal{R}\to\mathcal{E}^{0}(M)\otimes\mathcal{E}^{0}(M)\to\left(\mathcal{E}^{0}(M)\otimes\mathcal{E}^{1}(M)\right)\oplus\left(\mathcal{E}^{1}(M)\otimes\mathcal{E}^{0}(M)\right)\to\cdots\\(7)\quad\downarrow\mathrm{i d}\quad\downarrow\quad\downarrow\quad\downarrow\\0\to\mathcal{R}\xrightarrow{\quad}\mathcal{E}^{0}(M)\quad\xrightarrow{\quad}\mathcal{E}^{1}(M)\xrightarrow{\quad}\cdots\quad

The homomorphism (7) induces a cochain map $\Gamma(\mathcal{E}^*(M)\otimes\mathcal{E}^*(M))\to\Gamma(\mathcal{E}^*(M))$ which, according to 5.24 and the corollary of 5.23, induces the identity map $H^q(M,\mathcal{R})\to H^q(M,\mathcal{R})$. Consider now the following commutative diagram of cochain complexes:

 $$ \begin{matrix}\Gamma\big(\mathcal{E}^{*}(M)\big)\otimes\Gamma\big(\mathcal{E}^{*}(M)\big)\to\Gamma\big(\mathcal{E}^{*}(M)\otimes\mathcal{E}^{*}(M)\big)\to\Gamma\big(\mathcal{E}^{*}(M)\big)\\\uparrow\quad\uparrow\\E^{*}(M)\otimes E^{*}(M)\xrightarrow{\quad}\quad\quad\quad E^{*}(M)\end{matrix} $$ 

The diagram (8), together with 5.39(3), induces the following commutative diagram on cohomology:

 $$ \begin{array}{l}{H^{p}(M,\mathcal{R})\otimes H^{q}(M,\mathcal{R})\to H^{p+q}\big(\Gamma\big(\mathcal{E}^{\ast}(M)\big)\otimes\Gamma\big(\mathcal{E}^{\ast}(M)\big)\big)\to H^{p+q}(M,\mathcal{R})\stackrel{i d}{\to}H^{p+q}(M,\mathcal{R})}\\ {(9)\quad\big\uparrow}\\ {H_{\mathtt{d e R}}^{p}(M)\otimes H_{\mathtt{d e R}}^{q}(M)\longrightarrow H^{p+q}\big(E^{\ast}(M)\otimes E^{\ast}(M)\big)\xrightarrow{\quad}}\\ \end{array}H_{\mathtt{d e R}}^{p+q}(M). $$ 

The composition of homomorphisms in the top row of (9) gives precisely the multiplicative structure 5.42(8) in sheaf cohomology; whereas the composition in the bottom row of (9) is precisely the classical multiplicative structure (2), and the first and last vertical arrows are the canonical isomorphisms. Thus the classical algebra structure on $\sum H_{d \cdot R}^{p}(M)$ is identical with that induced from the algebra structure on sheaf cohomology.

5.44 The Singular Cohomology Algebra This section will be written in terms of the continuous singular cohomology. All considerations, however, apply in exactly the same manner to the differentiable singular theory. Let  $ f \in S^\circ(M,K) $ be a singular p-cochain, and let  $ g \in S^\circ(M,K) $ be a singular q-cochain. We shall define a singular  $ (p+q) $ cochain  $ f \to g $ called the cup product of f and g. Let  $ \sigma $ be a singular  $ (p+q) $ simplex in M. Define

 $$ \begin{aligned}{}&{{}(f\smallsmile g)(\sigma)}\\ {}&{{}\quad=f(\sigma\circ k_{p+q}^{p+q-1}\circ k_{p+q-1}^{p+q-2}\circ\cdots\circ k_{p+1}^{p})g(\sigma\circ k_{0}^{p+q-1}\circ k_{0}^{p+q-2}\circ\cdots\circ k_{0}^{q}),}\\ \end{aligned} $$ 

where if $q=0$, then the first factor on the right-hand side of (1) is $f(\sigma)$; and if $p=0$, then the second factor on the right-hand side of (1) is $g(\sigma)$. The $k$'s are the mappings defined in 4.6(2). In other words, (1) says that we start with $\sigma$ and take the top face $q$ times to get a $p$-simplex to which we apply $f$, and we start with $\sigma$ and take the 0-face $p$ times to get a $q$-simplex to which we apply $g$. The multiplication on the right-hand side of (1) takes place in the principal ideal domain $K$. Associativity, namely,

 $$ f-(g-h)=(f-g)-h, $$ 

follows from (1) and from the identity

 $$ \begin{aligned}{k_{0}^{p+q+r-1}\circ\cdots\circ k_{0}^{q+r}\circ k_{q+r}^{q+r-1}}&{{}\circ\cdots\circ k_{q+1}^{q}}\\ {}&{{}=k_{p+q+r}^{p+q+r-1}\circ\cdots\circ k_{p+q+1}^{p+q}\circ k_{0}^{p+q-1}\circ\cdots\circ k_{0}^{q}}\\ \end{aligned} $$ 

which follows from repeated applications of 4.6(5). The bilinear map  $ (f,g) \mapsto f \smile g $ induces a homomorphism

 $$ S^{\mathfrak{p}}(M,K)\otimes S^{\mathfrak{q}}(M,K)\to S^{\mathfrak{p}+q}(M,K). $$ 

We claim that

 $$ (d f)\;\lrcorner\;g+(-1)^{\mathfrak{p}}f\lrcorner\;(d g)=d(f\lrcorner g). $$ 

We suggest that the reader check (5) first for the case in which $f$ and $g$ are 1-cochains and $\sigma$ is a 3-simplex. In this case some simple pictures will aid in following the computation. In general, let $\tau$ be a singular $(p+q+1)$ simplex. Then from (1) and 5.31(8), and from repeated applications of 4.6(5), we obtain

 $$ \begin{aligned}{d(f\smallsmile g)(\tau)}&{{}=\sum_{l=0}^{p+q+1}(-1)^{l}(f\smallsmile g)(\tau\circ k_{l}^{p+q})}\\ {=\sum_{l=0}^{p+q+1}}&{{}(-1)^{l}f(\tau\circ k_{l}^{p+q}\circ k_{p+q}^{p+q-1}\circ\cdots\circ k_{p+1}^{p})\;g(\tau\circ k_{l}^{p+q}\circ k_{0}^{p+q-1}\circ\cdots\circ k_{0}^{q})}\\ {=\sum_{l=0}^{p}}&{{}(-1)^{l}f(\tau\circ k_{l}^{p+q}\circ k_{p+q}^{p+q-1}\circ\cdots\circ k_{p+1}^{p})\;g(\tau\circ k_{0}^{p+q}\circ\cdots\circ k_{0}^{q})}\\ {}&{{}+\sum_{l=p+1}^{p+q+1}(-1)^{l}f(\tau\circ k_{p+q+1}^{p+q}\circ\cdots\circ k_{p+1}^{p})\;g(\tau\circ k_{0}^{p+q}\circ\cdots\circ k_{l-p}^{q+1}\circ k_{l-p}^{q})}\\ {=\sum_{l=0}^{p}}&{{}(-1)^{l}f(\tau\circ k_{p+q+1}^{p+q}\circ k_{p+q}^{p+q-1}\circ\cdots\circ k_{p+2}^{p+1}\circ k_{l}^{p})\;g(\tau\circ k_{0}^{p+q}\circ\cdots\circ k_{0}^{q})}\\ {}&{{}+(-1)^{p}f(\tau\circ k_{p+q+1}^{p+q}\circ\cdots\circ k_{p+1}^{p})\sum_{j=1}^{q+1}(-1)^{j}g(\tau\circ k_{0}^{p+q}\circ\cdots\circ k_{0}^{q+1}\circ k_{j}^{q})}\\ {=\sum_{l=0}^{p+1}}&{{}(-1)^{l}f(\tau\circ k_{p+q+1}^{p+q}\circ k_{p+q}^{p+q-1}\circ\cdots\circ k_{p+2}^{p+1}\circ k_{1}^{p})\;g(\tau\circ k_{0}^{p+q}\circ\cdots\circ k_{0}^{q})}\\ {}&{{}+(-1)^{p}f(\tau\circ k_{p+q+1}^{p+q}\circ\cdots\circ k_{p+1}^{p})\sum_{j=0}^{q+1}(-1)^{j}g(\tau\circ k_{0}^{p+q}\circ\cdots\circ k_{0}^{q+1}\circ k_{j}^{q})}\\ {}\\ {}&{{}=(d f\smallsmile g)(\tau)+(-1)^{p}(f\smallsmile d g)(\tau).}\\ \end{aligned} $$ 

It follows from (5) that the homomorphisms (4) determine a cochain map

 $$ S^{*}(M,K)\otimes S^{*}(M,K)\to S^{*}(M,K). $$ 

The cochain map (6) together with the natural homomorphisms

 $$ H_{\Delta}^{p}(M;K)\otimes H_{\Delta}^{q}(M;K)\to H^{p+q}\big(S^{*}(M,K)\otimes S^{*}(M,K)\big) $$ 

of 5.39(3) induces homomorphisms

 $$ H_{\Delta}^{p}(M;K)\otimes H_{\Delta}^{q}(M;K)\to H_{\Delta}^{p+q}(M;K) $$ 

(8)

which give the direct sum  $ \sum H_{\Delta}^{p}(M;K) $ the structure of an associative algebra over K. This is the classical multiplicative structure of singular cohomology. Now,  $ \sum H_{\Delta}^{p}(M;K) $ also inherits an associative algebra structure from the algebra structure 5.42(8) on sheaf cohomology via the canonical isomorphism  $ \sum H_{\Delta}^{p}(M;K) \cong \sum H_{\Delta}^{p}(M,\mathscr{K}) $. The proof that these two algebra structures on  $ \sum H_{\Delta}^{p}(M;K) $ are identical is exactly the same as the proof of the corresponding statement for the de Rham cohomology as given in 5.43(4) through (9), but with the replacement of  $ \delta^{*}(M) $ by  $ 8^{*}(M,K) $ and  $ E^{*}(M) $ by  $ S^{*}(M,K) $, and so on.

The results of 5.43 and 5.44 provide the following more complete version of the de Rham theorem 5.36.

5.45 The de Rham Theorem The de Rham homologyism

 $$ k^{*}\colon\sum_{\mathfrak{p}}H_{\tt d e R}^{\mathfrak{p}}(M)\to\sum_{\mathfrak{p}}H_{\Delta^{\infty}}^{\mathfrak{p}}(M,\mathbb{R}) $$ 

is an algebra isomorphism.

##### SUPPORTS

5.46 Definition A family of supports on $M$ is a family $\Phi$ of closed subsets of $M$ satisfying:

(a) The union of any two members of $\Phi$ is again in $\Phi$.

(b) Any closed subset of a member of $\Phi$ is also a member of $\Phi$.

(c) Each member of  $ \Phi $ has a neighborhood whose closure is in  $ \Phi $.

Let $\Phi$ be a family of supports on $M$. We recall that $M$ is assumed to be at least a paracompact Hausdorff space and where necessary is actually a differentiable manifold. If $\delta$ is a sheaf over $M$, we let $\Gamma_{\bullet}(\delta)$ be the set of sections of $\delta$ whose supports are members of $\Phi$. It follows from condition (a) that $\Gamma_{\bullet}(\delta)$ is a submodule of $\Gamma(\delta)$. It follows from (b) that a sheaf homomorphism $\delta \to \delta'$ induces a homomorphism $\Gamma_{\bullet}(\delta) \to \Gamma_{\bullet}(\delta')$.

Theorem 5.12 has an exact analog with supports. One needs only to make a slight modification in the proof by using condition (c) to help choose a cover which will guarantee that the resulting section of 8 actually lies in $\Gamma_{\bullet}(8)$. The details are left to the reader as an exercise.

A. cohomology theory $\mathcal{H}_{\bullet}$ for $M$ with supports $\Phi$ and with coefficients in sheaves of $K$-modules over $M$ is defined exactly as in 5.18, with the exceptions that $\Gamma(8)$ is replaced by $\Gamma_{\bullet}(8)$ in 5.18(a) and the cohomology modules are now denoted by $\bullet H^{p}(M,8)$. The entire development of this chapter can be carried through for cohomology with supports with very few modifications. We shall briefly sketch those modifications.

The proof of existence and uniqueness of a cohomology theory with supports (which will make use of the support version of Theorem 5.12) proceeds as in 5.18 through 5.25 with the exception that when given a fine torsionless resolution $0 \to \mathcal{H} \to \mathcal{C}_0 \to \mathcal{C}_1 \to \mathcal{C}_8 \to \cdots$, we now define the sheaf cohomology modules by setting

 $$ {}_{*}{H}^{q}(M,\mathbb{S})=H^{q}\big(\Gamma_{\otimes}(\mathcal{C}^{*}\otimes\mathbb{S})\big). $$ 

Let $\{S_U; \rho_{U,V}\}$ be a presheaf with associated sheaf 8. We let $\circledast S_M$ be the submodule of $S_M$ consisting of those elements mapping into $\Gamma_{\bullet}(8)$ under the canonical homomorphism $S_M \to \Gamma(8)$. It then follows from Proposition 5.27 and the definition of $\circledast S_M$ that 5.27 holds if we replace 5.27(2) by

 $$ 0\to(S_{M})_{0}\to\otimes S_{M}\to\Gamma_{\otimes}(\mathcal{S})\to0. $$ 

The classical cohomology theories with supports are defined by:

 $$ \begin{aligned}{\bullet H_{\mathcal{A}-S}^{q}(M;G)}&{{}=H^{q}\big(\bullet A^{*}(M,G)/A_{0}^{*}(M,G)\big),}\\ {\bullet H_{\mathtt{d e R}}^{q}(M)}&{{}=H^{q}\big(\bullet E^{*}(M)\big),}\\ {\bullet H_{\Delta}^{q}(M;G)}&{{}=H^{q}\big(\bullet S^{*}(M,G)\big),}\\ {\bullet H_{\Delta\infty}^{q}(M;G)}&{{}=H^{q}\big(\bullet S_{\infty}^{*}(M,G)\big).}\\ \end{aligned} $$ 

In the Čech theory, the support of a $q$-cochain $f\in C^q(U,8)$ is by definition the union of the supports of the sections $f(\sigma)$ as $\sigma$ runs over the $q$-simplices of the cover $U$. If we set $\odot C^q(U,8)$ equal to the module of $q$-cochains with supports in $\Phi$, then the development of the Čech theory proceeds as before and yields the Čech cohomology modules $\odot\tilde{H}^q(M,8)$ with supports.

The resultant cohomology theories will depend on the family of supports chosen. Ordinary cohomology is the same as the special case of cohomology with supports in which $\Phi$ is taken to be the family of all closed sets.

The isomorphism theorems and the development of the multiplicative structure all proceed for supports exactly as before. In particular, we have the de Rham theorem with supports:

 $$ k^{*}\colon\sum_{\mathfrak{p}}\bullet H_{\mathbf{d e}\mathbf{R}}^{\mathfrak{p}}(M)\cong\sum_{\mathfrak{p}}\bullet H_{\Delta}^{\mathfrak{p}}\infty(M;\mathbb{R}) $$ 

is an algebra isomorphism.

##### EXERCISES

1 Let S be a sheaf over M. Prove that the mapping  $ m \mapsto 0 \in \mathcal{S}_m $ (the “0-section”) is continuous.

2 Prove that sections of sheaves are local homeomorphisms and therefore are open maps.

3 Prove that if two sections of a sheaf agree at one point, then they agree on a neighborhood of that point. Conclude that the set of points on which a section is not zero is a closed set.

4 A $C^{\infty}$ function on $M$ determines a cross section of the sheaf of germs of $C^{\infty}$ functions $\mathcal{C}^{\infty}(M)$. The set of points in $M$ on which a $C^{\infty}$ function is not zero is an open set; whereas, according to Exercise 3, the set of points in $M$ where a section of $\mathcal{C}^{\infty}(M)$ is not zero is a closed set. Can you reconcile these two facts? Consider examples.

5 Prove that sheaf mappings are local homeomorphisms, and therefore are open maps.

6 Prove that if two sheaf mappings agree at a point then they agree on a neighborhood of that point. Conclude that the set of points where a sheaf mapping is not zero is a closed set.

7 Complete the details of the construction in 5.4 of quotient sheaves.

8 Complete the details of the proof begun in 5.6 that  $ \beta(\alpha(8)) $ is canonically isomorphic with 8.

9 Prove that there is a canonical isomorphism  $ (\delta \otimes \mathcal{T})_m \cong \delta_m \otimes \mathcal{T}_m $.

10 Prove that the tensor product of two complete presheaves need not be a complete presheaf.

11 Let $\varphi$ be a $C^{\infty}$ function on $M$. Define a mapping $\mathcal{C}^{\infty}(M) \to \mathcal{C}^{\infty}(M)$ by sending $\mathbf{f}_{m} \to \varphi(m) \cdot \mathbf{f}_{m}$. Here, as usual, $\mathbf{f}_{m}$ denotes the germ at $m$ of a $C^{\infty}$ function $f$ defined on a neighborhood of $m$. Prove that this mapping is not in general continuous and therefore cannot be a sheaf homomorphism. (Caution: Errors are often made at this point in the construction of partitions of unity on sheaves—review the correct procedure for the construction of a partition of unity on $\mathcal{C}^{\infty}(M)$ given in 5.10.)

12 Make the necessary modifications in the proof of Theorem 5.12 to prove that if $\Phi$ is a system of supports on $M$ and $8 \to \mathcal{T}$ is a surjective sheaf homomorphism with its kernel a fine sheaf, then $\Gamma_{\bullet}(8) \to \Gamma_{\bullet}(\mathcal{T})$ is a surjection.

13 Carry out the details in the proof of the exactness of 5.17(2).

14 Complete the details of 5.24.

15 Prove that the presheaves 5.26(5) satisfy  $ 5.7(C_3) $, but for  $ p \geq 1 $ do not satisfy  $ 5.7(C_1) $.

16 Give an example of an exact sequence of modules

 $$ 0\to A\to B\to C\to0 $$ 

and a module D such that

 $$ 0\to A\otimes D\to B\otimes D\to C\otimes D\to0 $$ 

is not exact.

17 Find an example of a fine sheaf which has a subsheaf which is not fine.

18 Prove that if you tensor a long exact sequence of torsionless sheaves with a sheaf S, then the resulting long sequence is still exact.

19 Prove that a continuous map $f\colon M\to N$ induces in a natural way a homomorphism

 $$ f_{*}\colon H_{\Delta}^{p}(N;G)\to H_{\Delta}^{p}(M;G) $$ 

such that if g:  $ N \to X $, then

 $$ (g\circ f)_{*}=f_{*}\circ g_{*}, $$ 

and such that

 $$ (\mathrm{id})_{*}=\mathrm{id}. $$ 

Conclude that homeomorphic spaces have isomorphic singular cohomology.

20 Prove that 5.37(1) is an isomorphism. Keep in mind that these vector spaces are generally infinite dimensional.

21 Prove that if $\sigma$ and $\tau$ are closed differential forms all of whose periods are integer-valued (see 4.17), then $\sigma \wedge \tau$ has integer periods.

THE HODGE THEOREM

Throughout this chapter, $M$ will be a compact oriented Riemannian manifold of dimension $n$ unless otherwise indicated. We will see that the ordinary Laplacian $(-1)\sum_{i}\partial^{2}/\partial x_{i}^{2}$ has a generalization to an operator $\Delta$ on differential forms, known as the Laplace-Beltrami operator. Our main objective in this chapter is a proof of the Hodge decomposition theorem, which says that the equation $\Delta\omega=\alpha$ has a solution $\omega$ in the smooth $p$-forms on $M$ if and only if the $p$-form $\alpha$ is orthogonal (in a suitable inner product on $E^{p}(M)$ to the space of harmonic $p$-forms (those for which $\Delta\varphi=0$). From the Hodge decomposition theorem we will conclude that there exists a unique harmonic form in each of Rham cohomology class. As another simple application we will obtain the Poincaré duality theorem for de Rham cohomology and, from it, the Poincaré duality theorem for real singular cohomology. To prove the Hodge theorem, we shall give a complete self-contained exposition of the local theory of elliptic operators, using Fourier series as our basic tool. The eigenfunctions of the Laplace-Beltrami operator and their use in a proof of the Peter-Weyl theorem are discussed in the exercises at the end of this chapter.

##### THE LAPLACE-BELTRAMI OPERATOR

6.1 Definitions Recall (from 4.10(6) and Exercise 13 of Chapter 2) that there is a linear operator * which assigns to each p-form on M an  $ (n-p) $ form and which satisfies

 $$ **=(-1)^{p(n-p)}. $$ 

We define an operator $\delta$ from $p$-forms to $(p-1)$ forms by setting

 $$ \delta=(-1)^{n(p+1)+1}{*}d{*}. $$ 

On 0-forms, $\delta$ is simply the zero linear functional. The Laplace-Beltrami operator $\Delta$ (Laplacian for short) is defined by

 $$ \Delta=\delta d+d\delta, $$ 

and is a linear operator on  $ E^p(M) $ for each  $ p $ with  $ 0 \leq p \leq n $. We leave it 220

to the reader as an exercise to check that on $E^{0}(\mathbb{R}^{n})$, that is, on $C^{\infty}$ functions on Euclidean space $\mathbb{R}^{n}$, the Laplacian is simply the operator $(-1)\sum_{i=1}^{n}\partial^{2}/\partial x_{i}^{2}$. Also, it is a straightforward exercise to check that the Laplacian commutes with *, that is,

 $$ *\triangle=\triangle*. $$ 

We define an inner product on the vector space $E^{p}(M)$ of $p$-forms on $M$ by setting

 $$ \langle\alpha,\beta\rangle=\int_{M}\alpha\wedge\ast\beta\quad\mathrm{f o r}\alpha,\beta\in E^{d}(M), $$ 

and we denote the corresponding norm by  $ \|\alpha\| $. It follows from (6) of Exercise 13 in Chapter 2 that the bilinear form defined in (5) is actually symmetric and positive definite. We extend the inner products (5) for  $ 0 \leq p \leq n $ to an inner product on the direct sum  $ \sum_{p=0}^{n} E^p(M) $ simply by requiring the various  $ E^p(M) $ to be orthogonal.

6.2 Proposition $\delta$ is the adjoint of $d$ on $\sum_{p=0}^{n} E^{p}(M)$; that is,

(1)

 $$ \langle d\alpha,\beta\rangle=\langle\alpha,\delta\beta\rangle. $$ 

PROOF By linearity, and the orthogonality of the $E^{p}(M)$, the proof reduces to consideration of the case in which $\alpha$ is a $(p-1)$ form and $\beta$ is a $p$-form. In this case,

 $$ \begin{aligned}{d(\alpha\wedge{*}\beta)}&{{}=d\alpha\wedge{*}\beta+(-1)^{*-1}\alpha\wedge d{*}\beta}\\ {}&{{}=d\alpha\wedge{*}\beta-\alpha\wedge{*}\delta\beta.}\\ \end{aligned} $$ 

By integrating both sides over $M$ and applying the special case of Stokes' theorem contained in the corollary of 4.9 to the left-hand side, we obtain

(3)

 $$ 0=\int_{\mathcal{M}}(d\alpha\wedge*\beta-\alpha\wedge*\delta\beta)=\langle d\alpha,\beta\rangle-\langle\alpha,\delta\beta\rangle. $$ 

Thus

(4)

 $$ \langle d\alpha,\beta\rangle=\langle\alpha,\delta\beta\rangle. $$ 

Corollary  $ \Delta $ is self-adjoint, that is,

 $$ \langle\Delta\alpha,\beta\rangle=\langle\alpha,\Delta\beta\rangle\qquad(\alpha,\:\beta\in E^{\mathfrak{p}}(M);\:0\leq p\leq n). $$ 

6.3 Proposition  $ \Delta\alpha = 0 $ if and only if  $ d\alpha = 0 $ and  $ \delta\alpha = 0 $.

PROOF Clearly  $ \Delta\alpha = 0 $ if  $ d\alpha = 0 $ and  $ \delta\alpha = 0 $. Now,

 $$ \langle\Delta\alpha,\alpha\rangle=\langle(d\delta+\delta d)\alpha,\alpha\rangle=\langle\delta\alpha,\delta\alpha\rangle+\langle d\alpha,d\alpha\rangle. $$ 

Thus if  $ \Delta\alpha = 0 $, it follows that  $ d\alpha = 0 $ and  $ \delta\alpha = 0 $.

Corollary The only harmonic functions $(\Delta f = 0)$ on a compact, connected, oriented, Riemannian manifold are the constant functions.

##### THE HODGE THEOREM

6.4 Definition We shall let $\Delta^{*}$ denote the adjoint of the Laplacian on $E^{*}(M)$. This operator is, of course, precisely $\Delta$ itself since the Laplacian is self-adjoint on $E^{*}(M)$, and usually we make no distinction between $\Delta$ and $\Delta^{*}$. However, this distinction will be important for the form of the following definition.

We shall be interested in finding necessary and sufficient conditions for there to exist a solution  $ \omega $ of the equation  $ \Delta\omega = \alpha $. Suppose that  $ \omega $ is a solution of  $ \Delta\omega = \alpha $. Then

 $$ \langle\Delta\omega,\varphi\rangle=\langle\alpha,\varphi\rangle\quad\mathrm{f o r~a l l~}\varphi\in E^{\mathfrak{p}}(M), $$ 

from which it follows that

 $$ \langle\omega,\Delta^{*}\varphi\rangle=\langle\alpha,\varphi\rangle\quad\mathrm{f o r~a l l~}\varphi\in E^{\mathfrak{p}}(M). $$ 

Now, (2) suggests that we can view a solution of $\Delta\omega = \alpha$ as a certain type of linear functional on $E^{p}(M)$, namely, $\omega$ determines a bounded linear functional $l$ on $E^{p}(M)$ by

 $$ l(\beta)=\langle\omega,\beta\rangle; $$ 

and in view of (2), the functional I satisfies

 $$ l(\Delta^{*}\varphi)=\langle\alpha,\varphi\rangle\quad\mathrm{f o r~a l l~}\varphi\in E^{*}(M). $$ 

This view of a solution turns out to be extremely useful, for it will allow us to bring various techniques of functional analysis to bear on the problem of solving $\Delta\omega = \alpha$. We shall call such a linear functional a weak solution of $\Delta\omega = \alpha$. That is, a weak solution of $\Delta\omega = \alpha$ is a bounded linear functional $l: E^p(M) \to \mathbb{R}$ such that

 $$ l(\Delta^{*}\varphi)=\langle\alpha,\varphi\rangle\quad\mathrm{f o r~a l l~}\varphi\in E^{\mathfrak{p}}(M). $$ 

Later we will deal with weak solutions of a general partial differential operator $L$ defined on an open set in Euclidean space, and in place of $\Delta^{*}$ in (5), there will be the formal adjoint $L^{*}$ of $L$ (see 6.24(3) and 6.31).

We have seen that each ordinary solution  $ \omega \in E^p(M) $ of  $ \Delta\omega = \alpha $ determines a weak solution by (3). It turns out that the major effort of this chapter will be to prove a regularity theorem which says that the converse of this is true; that is, each weak solution determines an ordinary solution. The main step in proving this converse is to show that if  $ l $ is a weak solution of  $ \Delta\omega = \alpha $, then  $ l $ is represented by a smooth form  $ \omega $ in the sense that there is a form  $ \omega \in E^p(M) $ such that (3) holds. That the form  $ \omega $ is then an ordinary solution follows from the fact that

 $$ \langle\Delta\omega,\beta\rangle=\langle\omega,\Delta^{*}\beta\rangle=l(\Delta^{*}\beta)=\langle\alpha,\beta\rangle $$ 

for all  $ \beta \in E^p(M) $, which implies that  $ \Delta\omega = \alpha $.

6.5 Regularity Theorem Let  $ \alpha \in E^p(M) $, and let  $ l $ be a weak solution of  $ \Delta\omega = \alpha $. Then there exists  $ \omega \in E^p(M) $ such that

 $$ l(\beta)=\langle\omega,\beta\rangle $$ 

for every  $ \beta \in E^p(M) $. Consequently,  $ \Delta\omega = \alpha $.

We shall assume Theorem 6.5 for the moment as well as the following.

6.6 Theorem Let $\{\alpha_n\}$ be a sequence of smooth $p$-forms on $M$ such that $\|\alpha_n\| \leq c$ and $\|\Delta\alpha_n\| \leq c$ for all $n$ and for some constant $c > 0$. Then a subsequence of $\{\alpha_n\}$ is a Cauchy sequence in $E^p(M)$.

We will begin the machinery necessary for the proofs of Theorems 6.5 and 6.6 in the unit beginning with 6.15. We eventually return to the proofs of Theorems 6.5 and 6.6 in 6.32 and 6.33 respectively. Meanwhile, we shall assume the two theorems as proved and shall proceed to the Hodge theorem.

### 6.7 Definition We let

 $$ H^{\mathfrak{p}}=\{\omega\in E^{\mathfrak{p}}(M)\colon\Delta\omega=0\}. $$ 

The elements of  $ H^{p} $ are called harmonic p-forms.

6.8 The Hodge Decomposition Theorem For each integer $p$ with $0 \leq p \leq n$, $H^p$ is finite dimensional, and we have the following orthogonal direct sum decompositions of the space $\mathcal{E}^p(M)$ of smooth $p$-forms on $M$:

 $$ \begin{aligned}{E^{p}(M)}&{{}=\Delta(E^{p})\oplus H^{p}}\\ {}&{{}=d\delta(E^{p})\oplus\delta d(E^{p})\oplus H^{p}}\\ {}&{{}=d(E^{p-1})\oplus\delta(E^{p+1})\oplus H^{p}.}\\ \end{aligned} $$ 

Consequently, the equation $\Delta\omega = \alpha$ has a solution $\omega \in E^p(M)$ if and only if the $p$-form $\alpha$ is orthogonal to the space of harmonic $p$-forms.

PROOF If $H^{p}$ were not finite dimensional, then $H^{p}$ would contain an infinite orthonormal sequence. But by Theorem 6.6, this orthonormal sequence would contain a Cauchy subsequence, which is impossible. Thus $H^{p}$ is finite dimensional.

It is sufficient to prove the decomposition in the first line of (1), for the other two lines of (1) then follow from 6.1(3), 6.2, and 6.3.

Let  $ \omega_1, \ldots, \omega_t $ be an orthonormal basis of  $ H^p $. Then an arbitrary form  $ \alpha \in E^p(M) $ can uniquely be written

 $$ \alpha=\beta+\sum_{i=1}^{i}\langle\alpha,\omega_{i}\rangle\omega_{i} $$ 

where $\beta$ lies in $(H^{p})^{\perp}$, the subspace of $E^{p}(M)$ consisting of all elements orthogonal to $H^{p}$. Thus we have an orthogonal direct sum decomposition

 $$ E^{{s}}(M)=(H^{{s}})^{\perp}\oplus H^{{s}}. $$ 

The theorem will be proved by showing that  $ (H^{p})^{\perp} = \Delta(E^{p}) $. We let H denote the projection operator of E^{p}(M) onto H^{p} so that H(\alpha) is the harmonic part of \alpha.

Now  $ \Delta(\bar{E}^p) \subset (H^p)^\perp $. For if  $ \omega \in E^p $ and  $ \alpha \in H^p $, then

 $$ \langle\Delta\omega,\alpha\rangle=\langle\omega,\Delta\alpha\rangle=0. $$ 

Conversely, we claim that  $ (H^v)^\perp \subset \Delta(E^v) $. In order to prove this, we first need the following inequality.

We claim that there is a constant c > 0 such that

 $$ \left\Vert\beta\right\Vert\leq c\left\Vert\Delta\beta\right\Vert\quad\mathrm{f o r~a l l}\quad\beta\in(H^{\mathfrak{s}})^{\bot}. $$ 

Suppose the contrary. Then there exists a sequence  $ \beta_j \in (H^p)^\perp $ with  $ \|\beta_j\| = 1 $ and  $ \|\Delta\beta_j\| \to 0 $. By Theorem 6.6, a subsequence of the  $ \beta_j $, which for convenience we can assume to be  $ \{\beta_j\} $ itself, is Cauchy. Thus  $ \lim_{j \to \infty} \langle \beta_j, \psi \rangle $ exists for each  $ \psi \in E^p(M) $. We define a linear functional  $ l $ on  $ E^p(M) $ by setting

 $$ l(\psi)=\operatorname*{l i m}_{j\to\infty}\langle\beta_{j},\psi\rangle\quad\mathrm{f o r}\quad\psi\in E^{p}(M). $$ 

Now l is clearly bounded, and

 $$ l(\Delta\varphi)=\operatorname*{l i m}_{j\to\infty}\langle\beta_{j},\Delta\varphi\rangle=\operatorname*{l i m}_{j\to\infty}\langle\Delta\beta_{j},\varphi\rangle=0, $$ 

so $l$ is a weak solution of $\Delta\beta = 0$. By Theorem 6.5, there exists $\beta \in E^p(M)$ such that $l(\psi) = \langle \beta, \psi \rangle$. Consequently, $\beta_j \to \beta$. Since $\|\beta_j\| = 1$ and $\beta_j \in (H^p)^\perp$, it follows that $\|\beta\| = 1$ and $\beta \in (H^p)^\perp$. But by Theorem 6.5, $\Delta\beta = 0$, so $\beta \in H^p$, which is a contradiction. Thus (4) is proved.

Now we shall use (4) to prove that $(H^p)^\perp \subset \Delta(E^p)$. Let $\alpha \in (H^p)^\perp$. We define a linear functional $I$ on $\Delta(E^p)$ by setting

 $$ I(\Delta\varphi)=\langle\alpha,\varphi\rangle\quad\mathrm{f o r~a l l~}\varphi\in E^{\mathfrak{p}}(M). $$ 

Now $l$ is well-defined; for if $\Delta\varphi_1 = \Delta\varphi_2$, then $\varphi_1 - \varphi_2 \in H^p$, so that $\langle \alpha, \varphi_1 - \varphi_2 \rangle = 0$. Also $l$ is a bounded linear functional on $\Delta(E^p)$, for let $\varphi \in E^p(M)$ and let $\psi = \varphi - H(\varphi)$. Then using (4), we obtain

 $$ \begin{aligned}{|I(\Delta\varphi)|}&{{}=|I(\Delta\psi)|=|\langle\alpha,\psi\rangle|\leq\|\alpha\|\|\psi\|}\\ {}&{{}\leq c\left\|\alpha\right\|.\|\Delta\psi\|=c\left\|\alpha\right\|\|\Delta\varphi\|.}\\ \end{aligned} $$ 

By the Hahn-Banach theorem [27, p. 228], $l$ extends to a bounded linear functional on $E^p(M)$. Thus $l$ is a weak solution of $\Delta\omega = \alpha$. By Theorem 6.5, there exists $\omega \in E^p(M)$ such that $\Delta\omega = \alpha$. Hence

 $$ (H^{p})^{\perp}=\Delta(E^{p}), $$ 

and the Hodge decomposition theorem is proved.

6.9 Definition We define the Green's operator $G: E^p(M) \to (H^p)^\perp$ by setting $G(\alpha)$ equal to the unique solution of $\Delta\omega = \alpha - H(\alpha)$ in $(H^p)^\perp$. We leave it to the reader as an exercise to prove that $G$ is a bounded self-adjoint linear operator which takes bounded sequences into sequences with Cauchy subsequences.

6.10 Proposition G commutes with $d$, $\delta$, and $\Delta$. In fact, $G$ commutes with any linear operator which commutes with the Laplacian $\Delta$.

PROOF Suppose that $T\Delta = \Delta T$ with, say, $T: E^p(M) \to E^q(M)$. Let $\pi_{(H^p)^\perp}$ denote the projection mapping of $E^p(M)$ onto $(H^p)^\perp$. By definition, $G = (\Delta \mid (H^p)^\perp)^{-1} \circ \pi_{(H^p)^\perp}$. Now, the fact that $T\Delta = \Delta T$ implies that $T(H^p) \subset H^q$; and since $(H^p)^\perp = \Delta(E^p)$, it implies also that $T((H^p)^\perp) \subset (H^q)^\perp$. It follows that

 $$ T\circ\pi_{(H^{\flat})^{\perp}}=\pi_{(H^{\flat})^{\perp}}\circ T, $$ 

and on  $ (H^{v})^{\perp} $,

 $$ T\circ\left(\Delta\bigm|(H^{p})^{\perp}\right)=\left(\Delta\bigm|(H^{q})^{\perp}\right)\circ T, $$ 

and hence on  $ (H^{v})^{\perp} $

 $$ T\circ\bigl(\Delta\bigm|(H^{p})^{\perp}\bigr)^{-1}=\bigl(\Delta\bigm|(H^{q})^{\perp}\bigr)^{-1}\circ T. $$ 

It follows from (1) and (3) that G commutes with T.

6.11 Theorem Each de Rham cohomology class on a compact oriented Riemannian manifold M contains a unique harmonic representative.

PROOF Let $\alpha$ be an arbitrary $p$-form on $M$. From the Hodge decomposition theorem and from the definition of the Green's operator $G$, we have

 $$ \alpha=d\delta G\alpha+\delta d G\alpha+H\alpha. $$ 

Since G, by 6.10, commutes with d, we have

 $$ \alpha=d\delta G\alpha+\delta G d\alpha+H\alpha. $$ 

Thus if  $ \alpha $ is a closed p-form,

(3)

 $$ \alpha=d\delta G\alpha+H\alpha, $$ 

so $H\alpha$ is a harmonic $p$-form in the same de Rham cohomology class as is $\alpha$. If two harmonic forms $\alpha_{1}$ and $\alpha_{2}$ differ by an exact form $d\beta$, then we have

 $$ 0=d\beta+(\alpha_{1}-\alpha_{2}). $$ 

But  $ d\beta $ and  $ (\alpha_{1}-\alpha_{2}) $ are orthogonal since

 $$ \langle d\beta,\alpha_{1}-\alpha_{3}\rangle=\langle\beta,\delta\alpha_{1}-\delta\alpha_{3}\rangle=\langle\beta,0\rangle=0. $$ 

Thus $d\beta=0$ and $\alpha_{1}=\alpha_{2}$. Thus there is a unique harmonic form in each de Rham cohomology class.

Corollary The de Rham cohomology groups for a compact, orientable, differentiable manifold are all finite dimensional.

PROOF Any differentiable manifold can be equipped with a Riemannian metric (Exercise 23 of Chapter 1), and so the corollary follows immediately from Theorem 6.11 and from the finite dimensionality (6.8) of the spaces $H^{p}$ of harmonic forms.

6.12 Let $M$ be a compact, oriented, differentiable manifold of dimension $n$. We define a bilinear function

 $$ H_{\mathbf{d e}\mathbf{R}}^{s}(M)\times\mathit{H}_{\mathbf{d e}\mathbf{R}}^{n-s}(M)\to\mathbb{R} $$ 

by sending

 $$ \left(\{\varphi\},\{\psi\}\right)\mapsto\int_{\mathcal{M}}\varphi\wedge\psi, $$ 

where $\varphi$ and $\psi$ are closed forms representing the cohomology classes $\{\varphi\}$ in $H_{\mathrm{de}\mathrm{R}}^{p}(M)$ and $\{\psi\}$ in $H_{\mathrm{de}\mathrm{R}}^{n-p}(M)$. Observe that the bilinear map (2) is well-defined. For example, if $\varphi_{1}$ is another representative of the de Rham class $\{\varphi\}$, then $\varphi_{1}=\varphi+d\xi$ for some form $\xi$, and by the special case of Stokes' theorem which is contained in the corollary of 4.9,

 $$ \begin{aligned}{\int_{\mathcal{M}}\varphi_{1}\wedge\psi=}&{{}\int_{\mathcal{M}}\varphi\wedge\psi}&{+}&{{}\quad\int_{\mathcal{M}}d\xi\wedge\psi}\\ {=}&{{}\int_{\mathcal{M}}\varphi\wedge\psi}&{+}&{{}\quad\int_{\mathcal{M}}d(\xi\wedge\psi)=\int_{\mathcal{M}}\varphi\wedge\psi.}\\ \end{aligned} $$ 

Observe also from its definition that the bilinear function (2) depends on the orientation on $M$.

6.13 Theorem (Poincaré duality for the de Rham cohomology of a compact oriented $n$-dimensional manifold $M$) The bilinear function 6.12(2) is a non-singular pairing and consequently determines isomorphisms of $H_{\mathrm{de}^{\mathbb{R}}}^{n-\mathbb{P}}(M)$ with the dual space of $H_{\mathrm{de}^{\mathbb{R}}}^{\mathbb{P}}(M)$:

 $$ H_{\mathrm{d e}\mathbf{R}}^{n-p}(M)\cong\big(H_{\mathrm{d e}\mathbf{R}}^{p}(M)\big)^{*}. $$ 

PROOF Given a non-zero cohomology class $\{\varphi\} \in H_{\mathrm{deR}}^{p}(M)$, we must find a non-zero cohomology class $\{\psi\} \in H_{\mathrm{deR}}^{n-p}(M)$ such that $\left(\{\varphi\},\{\psi\}\right) \neq 0$. Choose a Riemannian structure on $M$. We can assume, according to 6.11, that $\varphi$ is the harmonic representative of $\{\varphi\}$. Since the cohomology class $\{\varphi\}$ is not zero, $\varphi$ is not identically zero. Since $* \Delta = \Delta^*$, it follows that $* \varphi$ is also harmonic, and therefore closed by 6.3, and so $* \varphi$ represents a cohomology class $\{*\varphi\} \in H_{\mathrm{deR}}^{n-p}(M)$. Now

 $$ \left(\{\varphi\},\{\ast\varphi\}\right)=\int_{M}\varphi\wedge\ast\varphi=\|\varphi\|^{2}\neq0. $$ 

Thus the pairing 6.12(2) is non-singular, and the isomorphism (1) follows from 2.7.

Corollary If $M$ is a compact, connected, orientable, differentiable manifold of dimension $n$, then $H_{\mathrm{de}\, \mathbb{R}}^n(M) \cong \mathbb{R}$.

6.14 Remark The real continuous singular homology groups $H_{p}(M;\mathbb{R})$ are defined just as in 4.16, with the exception that all continuous simplices in $M$ are allowed, not just differentiable simplices. The isomorphism 5.37(1) holds for the continuous case exactly as for the differentiable theory. By combining 6.13 with the de Rham theorem 5.36, with the canonical isomorphism 5.32(5) of the differentiable with the continuous real singular homology of $M$, and with the isomorphism 5.37(1) for the continuous real cohomology and homology, we obtain the Poincaré duality between the real singular cohomology and the real singular homology of $M$:

 $$ H_{\Delta}^{p}(M;\mathbb{R})\cong H_{n-p}(M;\mathbb{R}). $$ 

##### SOME CALCULUS

We now begin to develop the machinery necessary for the proofs of Theorems 6.5 and 6.6.

6.15 Notation We shall be using multi-index notation  $ \alpha = (\alpha_1, \ldots, \alpha_n) $ where the  $ \alpha_i $ are integers. We let  $ |\alpha| $ denote the ordinary Euclidean norm of  $ \alpha $; that is,

 $$ |\alpha|=(\alpha_{1}^{2}+\cdots+\alpha_{n}^{2})^{1/2}, $$ 

and if the  $ \alpha_{i} $ are all non-negative, then we let

 $$ [\alpha]=\alpha_{1}+\cdots+\alpha_{n}. $$ 

If  $ \alpha $ and  $ \eta $ are both  $ n $-tuples of integers, then

 $$ \begin{array}{r}{\eta^{\alpha}=\eta_{1}^{\alpha_{1}}\cdots\eta_{n}^{\alpha_{n}},\quad\mathrm{w h e r e~w e~s e t~0^{o}=1.}}\end{array} $$ 

We shall use $x_{i}$ for the $i$th canonical coordinate function on $\mathbb{R}^{n}$, and let

 $$ x=(x_{1},\ldots,x_{n}). $$ 

The $\alpha$th derivative operator $D^{\alpha}$ is defined for each $n$-tuple $\alpha$ of nonnegative integers by

 $$ D^{\alpha}{}_{u}=\left(\frac{1}{i}\right)^{[\alpha]}\frac{\partial^{[\alpha]}{}_{u}}{\partial x_{1}^{\alpha_{1}}\cdots\partial x_{n}^{\alpha_{n}}}, $$ 

where  $ i = \sqrt{-1} $. (The addition of the factor of i will be convenient later.)

We let $\mathcal{P}$ denote the complex vector space consisting of $C^\infty$ functions defined on $\mathbb{R}^n$ which have values in complex $m$ space $\mathbb{C}^m$ and are periodic of period $2\pi$ in each variable. I would suggest that the reader assume $m$ to be 1 for the first reading of this section since that case contains all of the essential ideas and the computations are somewhat simpler. We will arrange the notation so that it is essentially the same for general $m$. One note of caution concerning the notation is this. If $\gamma, \beta \in \mathbb{C}^m$, then $\gamma \cdot \beta$ means the Hermitian product $\gamma_1 \overline{\beta}_1 + \cdots + \gamma_m \overline{\beta}_m$. If $m$ happens to be 1, then $\gamma \cdot \beta$ means $\gamma \beta$. The associated norm is denoted by $|\gamma|$.

If $\varphi, \psi \in \mathcal{P}$, then $\varphi \cdot \psi$ is the complex-valued function which is the Hermitian product of $\varphi$ and $\psi$; that is,

 $$ \varphi\cdot\psi=\varphi_{1}\overline{{\psi_{1}}}+\cdots+\varphi_{m}\overline{{\psi_{m}}}. $$ 

We let  $ |\psi| $ denote the real-valued function

 $$ |\psi|=(\psi\cdot\psi)^{1/2}. $$ 

If $\varphi \in \mathcal{P}$ and if $f$ is a periodic complex-valued $C^\infty$ function on $\mathbb{R}^*$ (all periods always $2\pi$), then $\varphi f$ shall denote the element of $\mathcal{P}$ whose $i$th component function is $\varphi_i f$; that is,

 $$ \varphi f=(\varphi_{1}f,\ldots,\varphi_{m}f). $$ 

Let  $ Q \subset \mathbb{R}^n $ be the open cube

 $$ \mathcal{Q}=\{p\in\mathbb{R}^{n}\colon0<x_{i}(p)<2\pi,i=1,\ldots,n\}. $$ 

We shall be introducing a number of different norms on $\mathcal{P}$. By $\|\psi\|$ we shall mean the ordinary $L_{2}$ norm of $\psi$ over $Q$,

 $$ \|\psi\|=\frac{1}{(2\pi)^{n/2}}\biggl(\int_{Q}\psi\cdot\psi\biggr)^{1/2}, $$ 

and  $ \langle\psi,\varphi\rangle $ shall denote the  $ L_{2} $ inner product,

 $$ \langle\psi,\varphi\rangle=\frac{1}{(2\pi)^{n}}\int_{Q}\psi\cdot\varphi. $$ 

The norm  $ \|\psi\|_{\infty} $ shall denote the uniform norm of  $ \psi $,

 $$ \left\lVert{\psi}\right\rVert_{\infty}=\operatorname*{s u p}_{Q}\left\lvert{\psi}\right\rvert. $$ 

6.16 Some Facts about Fourier Series If $\varphi \in \mathcal{P}$ and if $\xi = (\xi_1, \ldots, \xi_n)$ where the $\xi_i$ are integers, then the $\xi$th Fourier coefficient $\varphi_i \in \mathbb{C}^m$ is defined by

 $$ \varphi_{\xi}=\frac{1}{(2\pi)^{n}}\int_{Q}\varphi(x)e^{-i x\cdot\xi}d x, $$ 

where  $ x \cdot \xi = x_{1} \xi_{1} + \cdots + x_{n} \xi_{n} $

First we are going to show that the Fourier series  $ \sum_{\ell} \varphi_{\ell} e^{i\pi\cdot\ell} $ of  $ \varphi $ converges uniformly to  $ \varphi $. Let an integer  $ k > 0 $ be given. By integrating (1) repeatedly by parts, differentiating  $ \varphi $ and integrating  $ e^{-i\pi\cdot\ell} $, and observing that the boundary terms drop out since the integrand is periodic, one sees that there is a constant  $ c_{k}^{\prime} $ depending on  $ \varphi $ and its derivatives up to order at most  $ 2nk $ such that

 $$ |\varphi_{\xi}|\leq\frac{c_{k}^{\prime}}{(\prod\xi_{i})^{3k}}\quad\mathrm{f o r~a l l}\quad\xi\not\equiv0, $$ 

where $\prod\xi_{i}$ denotes the product of all the non-zero $\xi_{i}$. It follows that there is a constant $c_{k}$ such that

 $$ |\varphi_{\xi}|\leq\frac{c_{k}}{(1+|\xi|^{2})^{k}}\quad\mathrm{f o r~a l l~\xi.~} $$ 

Consider now the question of convergence of the series  $ \sum_{\xi} (1 + |\xi|^2)^{-k} $. If we let

 $$ S_{j}=\Big\{\xi=(\xi_{1},\ldots,\xi_{n})\colon\operatorname*{m a x}_{1\leq i\leq n}|\xi_{i}|=j\Big\}, $$ 

then the number of elements of $S_i$ is at most $2n(2j+1)^{n-1}$, and for each $\xi \in S_i$, $|\xi|^2 \geq j^2$, so that

 $$ s_{j}=\sum_{\xi\in S_{j}}\frac{1}{(1+|\xi|^{2})^{k}}\leq\frac{2n(2j+1)^{n-1}}{(1+j^{2})^{k}}\leq c j^{n-1-2k} $$ 

for $j \geq 1$, where $c$ is a constant depending only on $n$. Consequently,

 $$ \begin{array}{r c c c l}{\displaystyle\sum_{\xi}\frac{1}{(1+|\xi|^{2})^{k}}}&{=}&{1+\sum_{j=1}^{\infty}s_{j}}&{\leq}&{1+c\sum_{j=1}^{\infty}\frac{1}{j^{1+2k-n}},}\\ \end{array} $$ 

and so the series  $ \sum_{k} (1 + |\xi|^{2})^{-k} $ converges for  $ 1 + 2k - n > 1 $, or in other words, for

 $$ k\geq\left[\frac{n}{2}\right]+1, $$ 

where  $ [n/2] $ denotes the greatest integer less than or equal to n/2. It would be an interesting exercise for the reader to reach the same conclusion by using an integral test.

It follows from (3) that if we take  $ k \geq [n/2] + 1 $ as in (7), then the Fourier series

 $$ \sum_{\ell}\varphi_{\ell}e^{i\alpha\cdot\ell} $$ 

converges uniformly to some continuous function $\Phi$. We claim that $\Phi = \varphi$. This is of course due to the completeness of the trigonometric system and may be deduced as follows from the Stone-Weierstrass theorem [13], [27]. Let $\psi = \varphi - \Phi$, and let $t \in \mathcal{P}$ be a trigonometric polynomial; that is, $t$ is a finite linear combination of terms of the form $a_t e^{i x \cdot \xi}$ for $a_t \in \mathbb{C}^m$. Then since $\varphi$ and $\Phi$ have the same Fourier coefficients,

 $$ \int_{Q}\boldsymbol{\psi}\cdot\boldsymbol{t}=0. $$ 

Now if $\varepsilon > 0$ is given, then by the Stone-Weierstrass theorem there is a trigonometric polynomial $t \in \mathcal{P}$ such that $\|\psi - t\|_\infty < \varepsilon$. Thus, using (9), we see that

 $$ \bigg|\int_{Q}\psi\cdot\psi\bigg|=\bigg|\int_{Q}\psi\cdot(\psi-t)\bigg|\leq\varepsilon(2\pi)^{n}\|\psi\|. $$ 

Consequently  $ \|\psi\| \leq \varepsilon $. But  $ \varepsilon > 0 $ was arbitrary and  $ \psi $ is continuous, so  $ \psi = 0 $. Thus the Fourier series of a periodic  $ C^\infty $ function  $ \varphi $ converges uniformly to  $ \varphi $,

 $$ \varphi(x)=\sum_{\xi}\varphi_{\xi}e^{i x\cdot\xi}. $$ 

It follows from integration by parts that the $\xi$th Fourier coefficient of $D^{\alpha}\varphi$ is $\xi_{1}^{\alpha_{1}}\cdots\xi_{n}^{\alpha_{n}}\varphi_{\xi}$. Thus

 $$ D^{a}\varphi(x)=\sum_{\xi}\xi^{a}\varphi_{\xi}e^{i x\cdot\xi}. $$ 

From (11) and the orthogonality of the trigonometric system, we obtain the Parseval identity:

 $$ \int_{Q}|\varphi|^{2}=(2\pi)^{n}\sum_{\ell}|\varphi_{\ell}|^{2}. $$ 

Applying (13) to  $ D^{\alpha}\varphi $, we obtain

 $$ \Vert D^{\alpha}\varphi\Vert^{2}=\sum_{\xi}\xi^{2\alpha}|\varphi_{\xi}|^{2}. $$ 

It follows from (14) that given a non-negative integer $t$, there is a constant $c$ greater than zero and depending only on $t$ and $n$ such that

 $$ \begin{array}{r l r l r}{c\displaystyle\sum_{\xi}(1+\vert\xi\vert^{2})^{t}\vert\varphi_{\xi}\vert^{2}}&{\leq}&{\displaystyle\sum_{[\alpha]=0}^{t}\Vert D^{\alpha}\varphi\Vert^{2}}&{\leq}&{\displaystyle\sum_{\xi}(1+\vert\xi\vert^{2})^{t}\vert\varphi_{\xi}\vert^{2}.}\end{array} $$ 

6.17 The Sobolev spaces  $ H_s $ Let  $ \delta $ denote the complex vector space consisting of all sequences of complex vectors in  $ \mathbb{C}^m $ indexed by  $ n $-tuples of integers  $ \xi = (\xi_1, \ldots, \xi_n) $. Thus if  $ u \in \mathcal{B} $,  $ u = \{u_\xi\} $ where  $ \xi $ runs over all  $ n $-tuples of integers and where each  $ u_\xi \in \mathbb{C}^m $. For each integer  $ s $ (positive, negative, or zero) the Sobolev space  $ H_s $ is the subspace of  $ \delta $ defined by

 $$ H_{s}=\Big\{u\in\mathbb{S}\colon\sum_{\xi}(1+\vert\xi\vert^{2})^{s}\vert u_{\xi}\vert^{2}<\infty\Big\}. $$ 

It follows from the Schwarz inequality that

 $$ \begin{array}{r l}&{\bigg|\sum_{\xi}(1+\vert\xi\vert^{2})^{(s+t)/2}u_{\xi}\cdot v_{\xi}\bigg\rvert^{2}\leq\bigg(\sum_{\xi}(1+\vert\xi\vert^{3})^{s}\vert u_{\xi}\vert^{2}\bigg)\left(\sum_{\xi}(1+\vert\xi\vert^{2})^{t}\vert v_{\xi}\vert^{2}\right);}\end{array} $$ 

hence the left-hand side of (2) is finite whenever each member of the right-hand side is finite. We can therefore define an inner product on  $ H_{s} $ by

 $$ \langle u,v\rangle_{s}=\sum_{\xi}(1+\vert\xi\vert^{2})^{s}u_{\xi}\cdot v_{\xi}. $$ 

The associated norm is

 $$ \left\Vert{u}\right\Vert_{s}=\left\langle{u,u}\right\rangle_{s}^{1/2}. $$ 

It also follows from (2) that  $ \langle u, v \rangle_s $ exists if  $ u \in H_t $ and  $ v \in H_{t'} $, where  $ (t + t')/2 = s $.

Since $H_{s}$ is simply an $l_{2}$-space in which the measure space is the set of all $n$-tuples of integers $\xi$, and the measure is the counting measure weighted by $(1 + |\xi|^{2})^{s}$, it follows that $H_{s}$ is a Hilbert space.

We define a linear transformation  $ K^{t} $ on S for each integer t by setting

 $$ (K^{t}u)_{\xi}=(1+|\xi|^{2})^{t}u_{\xi}. $$ 

Finally, we identify $\mathcal{P}$ with a subspace of $\mathcal{S}$ by associating with each $\varphi \in \mathcal{P}$ its sequence of Fourier coefficients $\{\varphi_k\}$. In view of 6.16(12) we can extend the derivative operator $D^a$ from $\mathcal{P}$ to all of $\mathcal{S}$ by setting

 $$ (D^{a}u)_{\xi}=\xi^{a}u_{\xi}. $$ 

The inequality 6.16(3) together with 6.16(7) shows that the more differentiable a function is, the greater the order $s$ of the Sobolev space $H_s$ in which its sequence of Fourier coefficients lies. In particular, $\mathcal{P} \subset H_s$ for each $s$. Moreover, $\mathcal{P}$ is dense in each $H_s$ since each $u \in H_s$ for which all but a finite number of the $u_s$ are zero belongs to $\mathcal{P}$. We consider elements of the Sobolev spaces $H_s$ as formal Fourier series or “generalized functions.” A fundamental lemma due to Sobolev says that if $u \in H_s$ for sufficiently large $s$, then the formal Fourier series determined by $u$ actually converges to a function with a certain number of derivatives depending on $s$. This lemma will be one of the key steps in the proof of the regularity theorem, for it will allow us to conclude that a generalized solution of a partial differential equation which belongs to a sufficiently high Sobolev space is an actual solution.

## 232 The Hodge Theorem

Some salient features of the $H_{s}$ spaces are collected in the following theorem, which is divided into parts (a)-(j).

### 6.18 Theorem

(a) Let s be a non-negative integer. Then there are constants c and  $ c' $, depending at most on s and n, such that

 $$ c\left\Vert{\varphi}\right\Vert_{s}\leq\sum_{\left\lceil{z}\right\rceil=0}^{s}\left\Vert{D^{\alpha}\varphi}\right\Vert\leq c^{\prime}\left\Vert{\varphi}\right\Vert_{s}{~f o r~a l l~}\varphi\in\mathcal{P}. $$ 

Moreover, for the case $s=0$, we actually have the equality

 $$ \left\lVert{\varphi}\right\rVert=\left\lVert{\varphi}\right\rVert_{0}{~f o r~a l l~}\varphi\in\mathcal{P}. $$ 

(b) If $t < s$, then $\|u\|_t \leq \|u\|_s$, so $H_s \subset H_t$. Thus the union of the $H_s$ spaces over all integers $s$ is a subspace of $\mathbb{S}$, which we denote by $H_{-\infty}$.

(c)  $ \mathcal{P} $ is a dense subspace of  $ H_{s} $ for each s.

(d) $K^{t}$ is an isometry of $H_{s}$ onto $H_{s-2t}$ with inverse $K^{-t}$,

(3)

 $$ \left\Vert u\right\Vert_{s}=\left\Vert K^{t}u\right\Vert_{s-2t}; $$ 

and  $ K^t $ maps  $ \mathcal{P} $ into  $ \mathcal{P} $. If  $ \varphi \in \mathcal{P} $ and  $ t \geq 0 $, then

(4)

 $$ K^{t}\varphi=\left(1-\sum_{i=1}^{n}\frac{\partial^{2}}{\partial x_{i}^{2}}\right)^{t}\varphi. $$ 

Moreover, for all s and t

 $$ \langle u,v\rangle_{s}=\langle u,K^{t}v\rangle_{s-t}=\langle K^{t}u,v\rangle_{s-t}\quad{f o r~}u,v\in H_{s}. $$ 

(e) Schwartz Inequality If  $ u \in H_{s+t} $ and  $ v \in H_{s-t} $, then

 $$ |\left\langle u,v\right\rangle_{s}|\leq\left\|u\right\|_{s+t}\left\|v\right\|_{s-t}. $$ 

(f) If  $ u \in H_{s+t} $, then

 $$ \left\Vert{u}\right\Vert_{s+t}=\operatorname*{s u p}_{\stackrel{v\in H_{s-t}}{v\neq0}}\frac{|\langle u,v\rangle_{s}|}{\left\Vert{v}\right\Vert_{s-t}}. $$ 

(g) Peter-Paul Inequality Given integers $t^{\prime}<t<t^{\prime\prime}$ and $\varepsilon>0$, there is a constant $c(\varepsilon)>0$ such that

 $$ \left\|{u}\right\|_{t}{}^{2}\leq\varepsilon\left\|{u}\right\|_{t^{\prime}}{}^{2}+c(\varepsilon)\left\|{u}\right\|_{t^{\prime}}{}^{2} $$ 

for all $u \in H_{t^*}$. (We refer to this inequality as the Peter-Paul inequality in view of the comparison with part (b), although the morality has been twisted around. Rather than robbing Peter to pay Paul, here we are paying Paul ($\|u\|_{t^*}$) in order to rob Peter ($\|u\|_{t^*}$).)

(h)  $ D^{\alpha} $ is a bounded operator from  $ H_{s+[\alpha]} $ to  $ H_{s} $ for each s; indeed,

 $$ \|D^{\alpha}u\|_{s}\leq\|u\|_{s+[\alpha]}\quad{f o r~a l l}\quad u\in H_{s+[\alpha]}. $$ 

(i) Let $\omega$ be a $C^{\infty}$ complex-valued periodic function on $\mathbb{R}^{n}$. Then given an integer $s$, these are positive integers $c$ and $c^{\prime}$, with $c$ depending only on $s$ and $n$, and $c^{\prime}$ depending on $s, n$, and on $\omega$ and its derivatives, such that

 $$ \left\Vert{\omega\varphi}\right\Vert_{s}\leq c\left\Vert{\omega}\right\Vert_{\infty}\left\Vert{\varphi}\right\Vert_{s}+c^{\prime}\left\Vert{\varphi}\right\Vert_{s-1},\quad{f o r~\varphi\in\mathcal{P}.~} $$ 

In particular, there is a constant $c^{\prime \prime}$ depending on $\omega$, $s$, and $n$ such that

 $$ \left\lVert{\omega\varphi}\right\rVert_{s}\leq c^{\prime\prime}\left\lVert{\varphi}\right\rVert_{s}, $$ 

so multiplication by $\omega$ extends by continuity to a bounded operator on $H_{s}$

(j) Let $\omega$ be a $C^{\infty}$ complex-valued periodic function on $\mathbb{R}^{n}$. Then given an integer $s$, there is a positive constant $c$ such that

 $$ \left|\left\langle\omega u,v\right\rangle_{s}-\left\langle u,\bar{\omega}v\right\rangle_{s}\right|\leq c(\left\|u\right\|_{s}\left\|v\right\|_{s-1}+\left\|u\right\|_{s-1}\left\|v\right\|_{s}) $$ 

for each $u, v \in H_{s}$. For the case $s = 0$, we have

 $$ \langle\omega u,v\rangle_{0}=\langle u,\bar{\omega}v\rangle_{0}. $$ 

PROOF The inequality (1) follows from 6.16(15) and the fact that whenever $a_{1},\ldots,a_{n}$ are positive numbers, then

 $$ \frac{1}{n}\Big(\sum_{i=1}^{n}a_{i}\Big)^{2}\leq\sum_{i=1}^{n}a_{i}^{2}\leq\Big(\sum_{i=1}^{n}a_{i}\Big)^{2}. $$ 

The equality (2) is simply the Parseval identity 6.16(13).

Part (b) is obvious. The fact that 6.16(3) holds for each integer $k > 0$ implies that $\{\varphi_{\xi}\} \in H_s$ whenever $\varphi \in \mathcal{P}$, and as we have already indicated in the remarks immediately preceding the theorem, $\mathcal{P}$ is dense in $H_s$ since each $u \in H_s$ for which all but a finite number of the $u_\xi$ are zero belongs to $\mathcal{P}$.

The identities (3) and (5) in (d) are obvious; that the inner products are all well-defined follows from the remark immediately following 6.17(4). Let $\varphi \in \mathcal{P}$. We have $K^t\varphi = \{(1 + |\xi|^2)^t\varphi_\xi\}$. It follows from 6.16(3) and (7) and from the fact that there exists the inequality

 $$ \xi^{2\alpha}\leq(1+\vert\xi\vert^{2})^{[\alpha]} $$ 

that the series

 $$ \sum_{\xi}(1+\vert\xi\vert^{2})^{t}\varphi_{\xi}e^{i x\cdot\xi} $$ 

and all its formal derivatives

 $$ \sum_{\xi}D^{\alpha}(1+\vert\xi\vert^{2})^{t}\varphi_{\xi}e^{i x\cdot\xi}=\sum_{\xi}\xi^{\alpha}(1+\vert\xi\vert^{2})^{t}\varphi_{\xi}e^{i x\cdot\xi} $$ 

converge uniformly. Thus (12) converges to a periodic $C^\infty$ function and therefore is an element of $\mathcal{P}$. Hence $K^t$ maps $\mathcal{P}$ into $\mathcal{P}$. For (4), simply observe that the $\xi$th Fourier coefficient of the right-hand side equals $(1 + |\xi|^2)^t \varphi_\xi$.

The Schwartz inequality (e) is none other than 6.17(2). It follows from (e) that

 $$ \left\Vert{u}\right\Vert_{s+t}\geq\operatorname*{s u p}_{v\in\underline{{H}}_{s-t\atop v\neq0}}\frac{|\langle u,v\rangle_{s}|}{\|v\|_{s-t}}. $$ 

To prove the equality in (f), let  $ v = K^{t} u $. Then by (d),

 $$ \left\|u\right\|_{s+t}=\frac{\left\langle u,u\right\rangle_{s+t}}{\left\|u\right\|_{s+t}}=\frac{\left\langle u,v\right\rangle_{s}}{\left\|v\right\|_{s-t}}. $$ 

To prove the Peter-Paul inequality (g), first observe that for any positive number y,

 $$ 1\leq y^{t^{\prime\prime}-t}+\;\left(\frac{1}{y}\right)^{t-t^{\prime}} $$ 

since either y or 1/y is greater than or equal to 1. If in (14) we let

 $$ y=e^{1/(t^{\prime\prime}-t)}(1+\vert\xi\vert^{3}), $$ 

we obtain

 $$ (1+|\xi|^{2})^{t}\leq\varepsilon(1+|\xi|^{2})^{t^{\prime}}+\varepsilon^{(t^{\prime}-t)/(t^{\prime\prime}-t)}(1+|\xi|^{2})^{t^{\prime}}, $$ 

from which the Peter-Paul inequality follows with

 $$ c(\varepsilon)=\varepsilon^{(t^{\prime}-t)/(t^{\prime \prime}-t)}. $$ 

The inequality in (h) follows from the inequality (11).

In part (i), the inequality (7) follows immediately from part (b) and inequality (6). To prove (6), we first consider the case in which $s \geq 0$. Let $\varphi \in \mathcal{P}$. Then by applying (1), we obtain

 $$ \begin{aligned}{\|\omega_{\varphi}\|_{s}}&{{}\leq\operatorname{c o n s t}\sum_{[\alpha]=0}^{s}\|D^{\alpha}\omega_{\varphi}\|}\\ {}&{{}\leq\operatorname{c o n s t}\sum_{[\alpha]=0}^{s}\|\omega D^{\alpha}\varphi\|+\operatorname{c o n s t}\sum_{[\alpha]=0}^{s}\|D^{\alpha}\omega_{\varphi}-\omega D^{\alpha}\varphi\|}\\ {}&{{}\leq c\|\omega\|_{\infty}\|\varphi\|_{s}+\operatorname{c o n s t}\sum_{[\alpha]=0}^{s-1}\|D^{\alpha}\varphi\|}\\ {}&{{}\leq c\|\omega\|_{\infty}\|\varphi\|_{s}+c^{\prime}\|\varphi\|_{s-1}.}\\ \end{aligned} $$ 

At the third stage we have used the fact that  $ D^{\alpha}\omega\varphi - \omega D^{\alpha}\varphi $ only contains derivatives of  $ \varphi $ up to order [ $ \alpha $] - 1. For s < 0 we have

 $$ \begin{aligned}{\|\omega\varphi\|_{s}^{2}}&{{}=\langle\omega\varphi,\omega\varphi\rangle_{s}=\langle\omega K^{-s}K^{s}\varphi,K^{s}\omega\varphi\rangle_{0}}\\ {}&{{}=\langle K^{-s}\omega K^{s}\varphi,K^{s}\omega\varphi\rangle_{0}+\langle(\omega K^{-s}-K^{-s}\omega)K^{s}\varphi,K^{s}\omega\varphi\rangle_{0}}\\ {}&{{}\leq|\langle K^{-s}\omega K^{s}\varphi,K^{s}\omega\varphi\rangle_{0}|+\left|\bigvee_{\lbrace\alpha\rbrace=0}^{-2s-1}a_{\alpha}D^{\alpha}K^{s}\varphi,K^{s}\omega\varphi\biggr\rangle_{0}\right|,}\\ \end{aligned} $$ 

where the  $ a_a $ are combinations of derivatives of  $ \omega $. Now, by the case  $ s \geq 0 $ of (i) we obtain

 $$ \begin{aligned}{|\langle K^{-s}\omega K^{s}\varphi,K^{s}\omega\varphi\rangle_{0}|}&{{}=|\langle\omega K^{s}\varphi,K^{s}\omega\varphi\rangle_{-s}|\leq\|\omega K^{s}\varphi\|_{-s}\|K^{s}\omega\varphi\|_{-s}}\\ {}&{{}\leq(c\|\omega\|_{\infty}\|K^{s}\varphi\|_{-s}+k^{\prime}\|K^{s}\varphi\|_{-s-1})(\|K^{s}\omega\varphi\|_{-s})}\\ {}&{{}=(c\|\omega\|_{\infty}\|\varphi\|_{s}+k^{\prime}\|\varphi\|_{s-1})\|\omega\varphi\|_{s}.}\\ \end{aligned} $$ 

As for the last term in (15),

 $$ \begin{aligned}{\left|\left\langle\sum_{[\epsilon]=0}^{-2s-1}a_{\epsilon}D^{\alpha}K^{\epsilon}\varphi,K^{\epsilon}\omega\varphi\right\rangle_{0}\right|}&{{}\leq\operatorname{c o n s t}\sum_{[\epsilon]=0}^{-2s-1}|\langle D^{\alpha}K^{\epsilon}\varphi,K^{\epsilon}\omega\varphi\rangle_{0}|}\\ {}&{{}\leq\operatorname{c o n s t}\sum_{[\epsilon]=0}^{-2s-1}\|D^{\alpha}K^{\epsilon}\varphi\|_{s}\|K^{\epsilon}\omega\varphi\|_{-s}}\\ {}&{{}\leq\operatorname{c o n s t}\sum_{[\epsilon]=0}^{-2s-1}\|K^{\epsilon}\varphi\|_{s+[\epsilon]}\|K^{\epsilon}\omega\varphi\|_{-s}}\\ {}&{{}\leq\operatorname{c o n s t}\|K^{\epsilon}\varphi\|_{-s-1}\|K^{\epsilon}\omega\varphi\|_{-s}}\\ {}&{{}\leq\operatorname{c o n s t}\|\varphi\|_{s-1}\|\omega\varphi\|_{s}.}\\ \end{aligned} $$ 

Thus for $s < 0$, (6) follows from (15), (16), and (17).

It is sufficient to prove (8) and (9) in part (j) on the dense subspace  $ \mathcal{P} $ of  $ H_s $. Observe that (9) follows immediately from the fact (1) that the  $ L_2 $-norm is identical with the Sobolev norm  $ \|\cdot\|_0 $ on  $ \mathcal{P} $. Let  $ \varphi, \psi \in \mathcal{P} $. We consider the case of (8) in which  $ s $ is negative. Using part (d) and equation (9), we obtain

 $$ \begin{aligned}{\langle\omega\varphi,\psi\rangle_{s}}&{{}=\langle\omega K^{-s}K^{s}\varphi,K^{s}\psi\rangle_{0}}\\ {}&{{}=\langle K^{-s}K^{s}\varphi,\bar{\omega}K^{s}\psi\rangle_{0}=\langle K^{s}\varphi,K^{-s}\bar{\omega}K^{s}\psi\rangle_{0}}\\ {}&{{}=\langle\varphi,\bar{\omega}\psi\rangle_{s}+\langle K^{s}\varphi,(K^{-s}\bar{\omega}-\bar{\omega}K^{-s})K^{s}\psi\rangle_{0}.}\\ \end{aligned} $$ 

It follows as in (17) that

 $$ |\langle\omega_{\Phi},\psi\rangle_{s}-\langle\varphi,\bar{\omega}\psi\rangle_{s}|\leq\mathrm{c o n s t}\|\varphi\|_{s}\|\psi\|_{s-1}. $$ 

By symmetry we also have

 $$ |\langle\omega\varphi,\psi\rangle_{s}-\langle\varphi,\bar{\omega}\psi\rangle_{s}|\leq\mathrm{c o n s t}\|\psi\|_{s}\|\varphi\|_{s-1}. $$ 

Thus (8) is proved for $s$ negative. The proof is similar for $s$ positive. The proof of Theorem 6.18 is complete.

6.19 Difference Quotients If $\varphi \in \mathcal{P}$, then the $\xi$th Fourier coefficient of the translate $\varphi(x + h)$ of $\varphi$ by an element $h \in \mathbb{R}^n$ is $e^{ih \cdot \xi} \varphi_\xi$. Thus if $u \in \mathcal{S}$ and $h \in \mathbb{R}^n$, we define the translate $u$ by $h$ to be the element

 $$ T_{h}(u)=\{e^{i h\cdot\xi}u_{\xi}\}\in\mathcal{S}. $$ 

The difference quotient of u determined by a non-zero h is the element

 $$ u^{h}=\frac{T_{h}(u)-u}{|h|}=\left\{\left(\frac{e^{i h\cdot\xi}-1}{|h|}\right)u\right\}\in\mathcal{S}. $$ 

So if  $ \varphi \in \mathcal{P} $, then  $ T_{h}(\varphi)(x) = \varphi(x + h) $ and

 $$ \varphi^{h}(x)=\frac{\varphi(x+h)-\varphi(x)}{|h|}. $$ 

Observe that if  $ u \in H_{s} $, then

 $$ \left\Vert T_{h}(u)\right\Vert_{s}=\left\Vert u\right\Vert_{s}, $$ 

so $T_h$ is an isometry on $H_s$. Thus, in particular, if $u \in H_s$, then also $u^h \in H_s$ for each $h$. It follows from the inequality

 $$ \begin{aligned}{\bigg|\frac{e^{i h\cdot\xi}-1}{|h|}\bigg|^{2}}&{{}=\bigg|\frac{(\operatorname{c o s}h\cdot\xi)-1}{|h|}\bigg|^{2}+\bigg|\frac{\operatorname{s i n}h\cdot\xi}{|h|}\bigg|^{2}=\frac{2(1-\operatorname{c o s}h\cdot\xi)}{|h|^{2}}}\\ {}&{{}=\frac{4\operatorname{s i n}^{2}(\frac{1}{2}h\cdot\xi)}{|h|^{2}}\leq\frac{(h\cdot\xi)^{2}}{|h|^{2}}\leq(1+|\xi|^{2})}\\ \end{aligned} $$ 

that if  $ u \in H_{s+1} $, then the  $ u^k $ are uniformly bounded in the  $ s $-norm. In fact,

 $$ \|u^{h}\|_{s}\leq\|u\|_{s+1}. $$ 

We shall need the converse of this, as follows.

6.20 Lemma Let  $ u \in H_s $, and assume that there is a constant  $ k $ such that  $ \|u^h\|_s \leq k $ for all non-zero  $ h \in \mathbb{R}^n $. Then  $ u \in H_{s+1} $.

PROOF For each positive integer N we let  $ u_{v} $ be the element of  $ H_{s} $ obtained by truncating u at N; that is,

 $$ (u_{N})_{\xi}=\left\{\begin{matrix}{u_{\xi}}&{\mathrm{i f}\quad|\xi|<N}\\ {0}&{\mathrm{o t h e r w i s e}.}\\ \end{matrix}\right. $$ 

We need only prove that the  $ \|u_N\|_{s+1} $ are uniformly bounded. Let  $ (e_1, \ldots, e_n) $ be the standard orthonormal basis of  $ \mathbb{R}^n $, and let  $ h = te_i $. Then

 $$ \bigg|\frac{e^{i h\cdot\xi}-1}{|h|}\bigg|^{2}=\bigg|\frac{e^{i t\xi_{i}}-1}{t}\bigg|^{2}\to|\xi_{i}|^{2}\quad\mathrm{a s}\quad t\to0. $$ 

Since there are only finitely many  $ \xi $ with  $ |\xi| < N $, and since by hypothesis

 $$ \sum_{|\xi|<N}(1+|\xi|^{2})^{s}\left|u_{\xi}\right|^{2}\left|\frac{e^{i h\cdot\xi}-1}{|h|}\right|^{2}\leq k^{2}, $$ 

it follows from (2) that

 $$ \sum_{|\xi|<N}(1+|\xi|^{2})^{s}\left|u_{\xi}\right|^{2}|\xi_{i}|^{2}\leq k^{2}. $$ 

Thus  $ \|u_N\|_s+1 = \sum_{|\xi|<N}(1 + |\xi|^2)^{s+1}|u_\xi|^2 \leq nk^2 + \|u\|_{s^2}^2 $, so the  $ \|u_N\|_s+1 $ are uniformly bounded, and consequently  $ u \in H_{s+1} $.

6.21 Associate with each $u \in H_{-\infty}$ the series $\sum u_{\xi} e^{ix \cdot \xi}$. It will be of fundamental importance in what follows to know when this series converges, and (if it converges) how differentiable its limit is. The answer is supplied by the following lemma due to Sobolev.

6.22 Sobolev Lemma If $t \geq [n/2] + 1$ and $u \in H_t$, then the series $\sum_{t} u_t e^{i x \cdot \xi}$ converges uniformly. Thus each $u \in H_t$ for $t \geq [n/2] + 1$ corresponds to a continuous function.

PROOF It is sufficient to demonstrate that the series converges absolutely,  $ \sum |u_{\xi}| < \infty $. Now,

 $$ \begin{align*}\sum_{|\xi|<N}|u_{\xi}|&=\sum_{|\xi|<N}(1+|\xi|^{2})^{-t/2}(1+|\xi|^{2})^{t/2}|u_{\xi}|\\&\leq\left(\sum_{|\xi|<N}(1+|\xi|^{2})^{-t}\right)^{1/2}\binom{\sum_{|\xi|<N}(1+|\xi|^{2})^{t}|u_{\xi}|^{2}}{||\xi||<N}\\&\leq\left(\sum_{|\xi|<N}(1+|\xi|^{2})^{-t}\right)^{1/2}\|u\|_{t}.\end{align*} $$ 

Thus the result follows from 6.16(7).

Corollary (a) If $u \in H_t$ where $t \geq [n/2] + 1 + m$, then $D^s u = \sum \xi^s u_\xi e^{i\pi \cdot\xi}$ converges uniformly for $(\alpha) \leq m$. Thus each $u \in H_t$ for this range of $t$ corresponds to a function $\sum u_\xi e^{i\pi \cdot\xi}$ of class $C^m$.

PROOF With $u \in H_t$ for $t \geq [n/2] + 1 + m$ and with $[\alpha] \leq m$, it follows from 6.18(h) that $D^x u \in H_{t-[\alpha]}$, where $t - [\alpha] \geq [n/2] + 1$. Thus it follows from the Sobolev lemma that $\sum \xi^x u_\xi e^{ix \cdot \xi}$ converges uniformly. Now this series is the $\alpha$th “formal” derivative of the series $\sum u_\xi e^{ix \cdot \xi}$. Thus $\sum u_\xi e^{ix \cdot \xi}$ is of class $C^m$.

Corollary (b) From the proof of 6.22 it follows that if  $ t \geq [n/2] + 1 $, then there is a constant  $ c > 0 $ such that if  $ \varphi \in \mathcal{P} $, then

 $$ \left\|\varphi\right\|_{\infty}\leq c\left\|\varphi\right\|_{t}. $$ 

Applying (1) to  $ D^{*} \varphi $ and using 6.18(h), we obtain

 $$ \left\|D^{\alpha}\varphi\right\|_{\infty}\leq c\left\|\varphi\right\|_{\mathfrak{t}+[\alpha]}. $$ 

6.23 Rellich Lemma Let  $ \{u^i\} $ be a sequence of elements of  $ H_t $ with  $ \|u^i\|_t \leq 1 $. If  $ s < t $, then there is a subsequence of  $ \{u^i\} $ which converges in  $ H_s $.

PROOF By assumption.

PROOF By assumption,

 $$ \sum_{\xi}(1+\vert\xi\vert^{2})^{t}\vert u_{\xi}^{t}\vert^{2}\leq1. $$ 

For each fixed $\xi$, elements of the sequence $\{|(1 + |\xi|^s)^{t/2}u_{\xi}^{t}|\}$ are all bounded by 1, so the sequence $\{(1 + |\xi|^s)^{t/2}u_{\xi}^{t}\}$ has a convergent subsequence in $\mathbb{C}^m$. By the usual diagonal process, one can select a subsequence $\{u^{t_i}\}$ such that the sequence $(1 + |\xi|^s)^{t/2}u_{\xi}^{t_i}$ converges in $\mathbb{C}^m$ for each fixed $\xi$. We claim that $\{u^{t_i}\}$ is Cauchy, and therefore convergent, in $H_s$ if $s < t$. Let $e > 0$ be given. Now,

 $$ \begin{aligned}{\|u^{j_{t}}-u^{j_{k}}\|_{s}^{2}=}&{{}\sum_{|\xi|<N}(1+|\xi|^{2})^{s-t}(1+|\xi|^{2})^{t}|u_{\xi}^{j_{t}}-u_{\xi}^{j_{k}}|^{2}}\\ {}&{{}+\sum_{|\xi|\geq N}(1+|\xi|^{2})^{s-t}(1+|\xi|^{2})^{t}|u_{\xi}^{j_{t}}-u_{\xi}^{j_{k}}|^{2}.}\\ \end{aligned} $$ 

The second sum in (2) is bounded by

 $$ N^{2(s-t)}\sum_{|\xi|\geq N}(1+|\xi|^{2})^{t}(|u_{\xi}^{j_{t}}|^{2}+2|u_{\xi}^{j_{t}}||u_{\xi}^{j_{k}}|+|u_{\xi}^{j_{k}}|^{2}), $$ 

which is $\leq4N^{2(s-t)}$ in view of (1). Since $s-t<0$, $4N^{2(s-t)}$ can be made less than $\varepsilon/2$ by taking $N$ large enough, say $N=N_{0}$. The first sum in (2) is then bounded by

 $$ \sum_{|\xi|<N_{0}}(1+|\xi|^{2})^{t}|u_{\xi}^{j_{t}}-u_{\xi}^{j_{k}}|^{2}, $$ 

and since there are only a finite number of terms in this sum and since the sequences $(1 + |\xi|^2)^{i/2}u_{\xi}^{j_i}$ converge for each fixed $\xi$, there is a constant $J > 0$ such that if $j_i$ and $j_k$ are greater than $J$, then (3) is less than $\varepsilon/2$. Thus for $j_i, j_k > J$, we have $\|u^{j_i} - u^{j_k}\|_s^2 < \varepsilon$, and the proof is complete.

6.24 Definitions A (linear) differential operator L of order l on the  $ C^{m} $-valued  $ C^{\infty} $ functions on  $ R^{n} $ consists of an  $ m \times m $ matrix  $ (L_{ij}) $ in which

 $$ {\cal L}_{i j}=\sum_{\{a\}=0}^{i}a_{i j}^{a}D^{a}, $$ 

and the $a_{ij}^{e}$ are $C^{\infty}$ complex-valued functions on $\mathbb{R}^{n}$, with at least one $a_{ij}^{e} \neq 0$ for some $i, j$ and for some $\alpha$ for which $|\alpha| = l$. A differential operator $L$ is a periodic differential operator, or an operator on $\mathcal{P}$, if, in addition, the $a_{ij}^{e}$ are periodic functions.

Let $L$ be a periodic differential operator, and let $\varphi \in \mathcal{P}$ with component functions $\varphi_1, \ldots, \varphi_m$. Then

 $$ L_{\Psi}=\left(\sum_{j}L_{1j}\varphi_{j},\ldots,\sum_{j}L_{m j}\varphi_{j}\right). $$ 

It follows from integration by parts that if we define the operator  $ L^{*} $ on  $ \mathcal{P} $ by

 $$ L_{i j}^{*}=\sum_{\{a\}=0}^{l}D^{a}\overline{{a_{j i}^{a}}} $$ 

so that the ith component of  $ L^{*}\phi $ is given by

 $$ (L^{*}\varphi)_{i}=\sum_{j=0}^{m}\sum_{[a]=-0}^{l}D^{a}(\overline{{a_{j i}^{a}}}\varphi_{j}), $$ 

then in the $L_{2}$ inner product on $\mathcal{P}$ we have

 $$ \langle L\varphi,\psi\rangle=\langle\varphi,L^{*}\psi\rangle $$ 

for $\varphi, \psi \in \mathcal{P}$. $L^{*}$ is called the formal adjoint of $L$. The word “formal” is used here to emphasize that $L^{*}$ is not the adjoint of $L$ on a Hilbert space. It is simply the adjoint relative to the $L_{2}$ inner product on $\mathcal{P}$.

6.25 Proposition Let L be a partial differential operator on $\mathcal{P}$ of order $l$, and let s be an integer. Then there are positive constants $c, k$, and $c',$ where $c$ depends only on $n, m, l$, and $s$, where $k$ is a bound on the absolute values of the coefficients of the highest order terms in $L$, and where $c'$ depends on $n, m, l$, and on all the coefficients of L and their derivatives up to order $l$, such that

 $$ \left\Vert{L\varphi}\right\Vert_{s}\leq c k\left\Vert{\varphi}\right\Vert_{s+l}+c^{\prime}\left\Vert{\varphi}\right\Vert_{s+l-1} $$ 

for all $\varphi \in \mathcal{P}$. In particular, there is a constant $c$ such that

 $$ \left\Vert L\varphi\right\Vert_{s}\leq c^{\prime\prime}\left\Vert\varphi\right\Vert_{s+1} $$ 

for all $\varphi \in \mathcal{P}$, so $L$ extends by continuity to a bounded operator from $H_{s+1}$ to $H_{s}$ for each $s$.

PROOF The inequality (2) is an immediate consequence of (1) and 6.18(b). As for (1), the case $m=1$ (in which elements of $\mathcal{P}$ are $\mathbb{C}^1$ valued functions and the operator $L$ is a single partial differential operator $\sum a^a D^a$ rather than a matrix) follows immediately from 6.18(h) and (i). The inequality (1) for general $m$ follows from the case $m=1$ and from the inequality $\|L\varphi\|_s \leq \sup_{i,j} \|L_{ij}\varphi_j\|_s$, where

 $ \varphi = (\varphi_1, \ldots, \varphi_m) \in \mathcal{P} $, and the constant depends only on  $ m $.

6.26 Remark If $L$ is an operator on $\mathcal{P}$ of order $l$, and if $\omega$ is a $C^\infty$ complex-valued function on $\mathbb{R}^n$, then the operator $M = \omega L - L\omega$, where $M\varphi = \omega(L\varphi) - L(\omega\varphi)$, is of order at most $l-1$. Consequently, given $s$, there is a positive constant such that

 $$ \left\Vert M\varphi\right\Vert_{s}\leq\mathrm{c o n s t}\left\Vert\varphi\right\Vert_{s+l-1} $$ 

for all  $ \varphi \in \mathcal{P} $.

6.27 Lemma If $\omega$ is a real-valued periodic $C^{\infty}$ function, and $L$ is a differential operator of order $l$ on $\mathcal{P}$, then there is a positive constant such that

 $$ |\langle L(\omega^{2}u),L u\rangle_{s}-\|L(\omega u)\|_{s}^{2}|\leq\mathtt{c o n s t}\left(\|u\|_{s+1}\|u\|_{s+l-1}\right) $$ 

for all  $ u \in H_{e+1} $.

 $$ \begin{aligned}{\mathtt{P R O O F}\quad|\langle L(\omega^{z}u),L u\rangle_{s}-\langle L(\omega u),L(\omega u)\rangle_{s}|}&{{}}\\ {}&{{}\leq|\langle\omega L(\omega u),L u\rangle_{s}-\langle L(\omega u),\omega L u\rangle_{s}|}\\ {}&{{}+|\langle L(\omega u),(\omega L-L\omega)u\rangle_{s}|}\\ {}&{{}+|\langle(L\omega-\omega L)(\omega u),L u\rangle_{s}|,}\\ \end{aligned} $$ 

and (1) follows by applying 6.18(j), 6.25(2), and 6.18(7) to the first term and applying the Schwartz inequality, 6.26(1), 6.25(2), and 6.18(7) to the last two terms.

##### ELLIPTIC OPERATORS

6.28 Definition Let L be a partial differential operator of order l. We write L as

 $$ {\cal L}=P_{t}(D)+\cdots+P_{0}(D), $$ 

where $P_{i}(D)$ is an $m \times m$ matrix each entry of which is a differential operator $\sum [a_{a}D^{a}$, homogeneous of order $j$, and where the $a_{a}$ are $C^{\infty}$ complex

 $ ^{[a]=i} $ valued functions on  $ \mathbb{R}^n $. We let  $ P_i(\xi) $ denote the matrix obtained by substituting  $ \xi^a $ for  $ D^a $ in  $ P_i(D) $, where  $ \xi = (\xi_1, \ldots, \xi_n) $ is a point in  $ \mathbb{R}^n $. L is said to be elliptic at the point  $ x \in \mathbb{R}^n $ if the matrix  $ P_i(\xi) $ is non-singular at x for each non-zero  $ \xi $. L is elliptic if it is elliptic at each x. Observe that ellipticity is a condition on the highest-order part of L only. Observe also that L is elliptic at x if and only if

 $$ L(\varphi^{\iota}u)(x)\neq0 $$ 

for each $C^{m}$-valued $C^{\infty}$ function $u$ such that $u(x) \neq 0$ and each smooth real-valued function $\varphi$ such that $\varphi(x) = 0$ but $d\varphi(x) \neq 0$, since for each such $\varphi$ and $u$,

 $$ L(\varphi^{l}u)(x)=P_{l}(D)(\varphi^{l}u)(x)=P_{l}(d\varphi|_{\alpha})(u(x)). $$ 

The advantage of this criterion (2) for ellipticity is that it generalizes to a coordinate-free definition of ellipticity on manifolds, as we shall see later.

The basic analytic property of an elliptic operator that we shall need is the following.

6.29 Fundamental Inequality Let L be an elliptic operator on  $ \mathcal{P} $ of order l, and let s be an integer. Then there is a constant c > 0 such that

 $$ \|u\|_{s+l}\leq c(\|L u\|_{s}+\|u\|_{s}) $$ 

for all  $ u \in H_{s+1} $.

PROOF It is sufficient to prove (1) for all $\varphi \in \mathcal{P}$. The proof consists of several parts. We first consider the case of an elliptic operator $L_0$ on $\mathcal{P}$ with constant coefficients, which consists of the leading term

$P_i(D)$ only. If $u \in \mathbb{R}^n$ with $u \neq 0$, and if $\xi \neq 0$, then since $P_i(\xi)$ is non-singular, we have $|P_i(\xi)u|^2 > 0$. It follows from the compactness of the unit sphere in $\mathbb{R}^n$ that there is a constant $c > 0$ such that

 $$ |P_{i}(\xi)u|^{2}\geq c $$ 

for all  $ u $ and  $ \xi $ such that  $ |u| = |\xi| = 1 $. From this it follows that

 $$ |P_{i}(\xi)u|^{\sharp}\geq c|\xi|^{\underline{{s}}l}|u|^{\underline{{s}}} $$ 

for all $u$ and $\xi$ in $\mathbb{R}^n$. Thus for $\varphi \in \mathcal{P}$, it follows from (2) and the fact that $L_0$ has constant coefficients that

 $$ \begin{aligned}{\|L_{0}\varphi\|_{s}^{2}}&{{}=\sum_{\xi}|P_{l}(\xi)\varphi_{\xi}|^{2}\left(1+|\xi|^{2}\right)^{s}}\\ {}&{{}\geq\operatorname*{c o n s t}\sum_{\xi}|\xi|^{2l}|\varphi_{\xi}|^{2}(1+|\xi|^{2})^{s}.}\\ \end{aligned} $$ 

Hence

(4)

 $$ \begin{aligned}{(\|L_{0}\varphi\|_{s}+\|\varphi\|_{s})^{2}}&{{}\geq\|L_{0}\varphi\|_{s}^{2}+\|\varphi\|_{s}^{2}}\\ {}&{{}\geq\sum_{\xi}|\varphi_{\xi}|^{2}(1+|\xi|^{2})^{s}(1+\operatorname{c o n s t}|\xi|^{2l})}\\ {}&{{}\geq\operatorname{c o n s t}\sum_{\xi}|\varphi_{\xi}|^{2}(1+|\xi|^{2})^{s+l}}\\ {}&{{}=\operatorname{c o n s t}\|\varphi\|_{s+l}^{2}.}\\ \end{aligned} $$ 

Secondly, consider a general periodic elliptic operator $L$ of order $l$, and let $p \in \mathbb{R}^n$. We shall prove that there is a neighborhood $U$ of $p$ such that (1) holds for all $\varphi \in \mathcal{P}$ with support in $U$. (By a slight abuse of terminology we say that the support of a periodic function $\varphi$ lies in $U$ if the support of $\varphi$ lies in the union of $U$ with all of the periodic translates of $U$.) Let $L_0$ denote the constant coefficient elliptic operator, homogeneous of order $l$, determined by the highest-order part of $L$ at the point $p$. Then it follows from (4) that for each $\varphi \in \mathcal{P}$,

 $$ \begin{aligned}{\|\varphi\|_{s+l}}&{{}\leq\mathsf{c o n s t}\left(\|L_{0}\varphi\|_{s}+\|\varphi\|_{s}\right)}\\ {}&{{}\leq\mathsf{c o n s t}\left(\|L\varphi\|_{s}+\|(L_{0}-L)\varphi\|_{s}+\|\varphi\|_{s}\right).}\\ \end{aligned} $$ 

Let $k$ denote the constant in (5). Then choose a positive $\varepsilon$ smaller than $1/(2ck)$, where $c$ denotes the constant $c$ of 6.25. On a small enough neighborhood of $p$ the coefficients of the highest-order part of $L_0-L$ are less than $\varepsilon$ in absolute value. Let $L$ be a periodic operator agreeing with $L_0-L$ on a possibly smaller neighborhood $U$ of $p$ and with coefficients in the highest-order part everywhere less than $\varepsilon$ in absolute value. Then it follows from (5), 6.25(1), and the choice of $\varepsilon$, that for an element $\varphi\in\mathcal{P}$ whose support lies in $U$,

 $$ \begin{aligned}{\|\varphi\|_{s+l}}&{{}\leq\operatorname{c o n s t}\left(\|L\varphi\|_{s}+\|\tilde{L}\varphi\|_{s}+\|\varphi\|_{s}\right)}\\ {}&{{}\leq\operatorname{c o n s t}\|L\varphi\|_{s}+\frac{1}{2}\|\varphi\|_{s+l}+\operatorname{c o n s t}\|\varphi\|_{s+l-1}+\operatorname{c o n s t}\|\varphi\|_{s}.}\\ \end{aligned} $$ 

Applying the Peter-Paul inequality to the term  $ \|\varphi\|_{s+l-1} $, we obtain

 $$ \left\Vert\varphi\right\Vert_{s+1}\leq\mathrm{c o n s t}\left\Vert L\varphi\right\Vert_{s}+\frac{3}{4}\left\Vert\varphi\right\Vert_{s+1}+\mathrm{c o n s t}\left\Vert\varphi\right\Vert_{s}, $$ 

which proves (1) for these φ.

Let  $ T^n $ be the torus obtained as the quotient of  $ \mathbb{R}^n $ by the lattice consisting of all points  $ 2\pi\xi $, where  $ \xi $ is an  $ n $-tuple of integers. The open sets  $ U $ obtained above for each  $ p \in \mathbb{R}^n $ project to an open cover of  $ T^n $. Let  $ U_1, \ldots, U_k $ be a finite subcover, and let  $ \omega_1, \ldots, \omega_k $ be a partition of unity fitting this cover, of the special form

 $$ \sum_{i=1}^{k}\omega_{i}^{2}=1. $$ 

This is easily arranged—see the proofs of 1.11 and 1.10. Now consider the  $ \omega_i $ as periodic  $ C^\infty $ (real-valued) functions on  $ \mathbb{R}^n $. Let  $ \varphi \in \mathcal{P} $. Then by (6), and by 6.18(i) and (j),

 $$ \begin{aligned}{\|\varphi\|_{s+l}^{2}}&{{}=\langle\varphi,\varphi\rangle_{s+l}=\left\langle\sum_{i}\omega_{i}{}^{2}\varphi,\varphi\right\rangle_{s+l}}\\ {}&{{}\leq\sum_{i}\langle\omega_{i}\varphi,\omega_{i}\varphi\rangle_{s+l}+\operatorname{c o n s t}\|\varphi\|_{s+l}\|\varphi\|_{s+l-1}.}\\ \end{aligned} $$ 

Now since $\omega_{i}\varphi$ has support in one of the small open sets $U$ obtained above, and since there are only finitely many of the $\omega_{i}$, there are constants such that the last displayed line above is

\[\begin{aligned}&\leq\mathrm{const}\sum_{i}\|L\omega_{i}\varphi\|_{s}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s+l}\|\varphi\|_{s+l-1}\\&\leq\mathrm{const}\sum_{i}\langle L(\omega_{i}^{\frac{2}{s}}\varphi),L\varphi\rangle_{s}+\mathrm{const}\|\varphi\|_{s}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s+l}\|\varphi\|_{s+l-1}\\&=\mathrm{const}\|L\varphi\|_{s}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s+l}\|\varphi\|_{s+l-1}\tag{by6.27}\\&\leq\mathrm{const}\|\dot{L}\varphi\|_{s}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s}^{\frac{2}{s}}+\frac{1}{2}\|\varphi\|_{s+l}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s+l-1}^{\frac{2}{s}}\\&\leq\mathrm{const}\|L\varphi\|_{s}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s}^{\frac{2}{s}}+\frac{2}{4}\|\varphi\|_{s+l}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s}^{\frac{2}{s}},\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\

It follows that (1) holds for all  $ \varphi \in \mathcal{P} $ and hence for all  $ u \in H_{s+1} $.

6.30 Theorem (Regularity for Periodic Elliptic Operators) Let $L$ be a periodic elliptic operator of order $l$. Assume that $u \in H_{-\infty}, v \in H_{t}$, and

 $$ Lu=v. $$ 

Then  $ u \in H_{t+1} $.

PROOF It is sufficient to prove that if  $ u \in H_s $ and  $ v = Lu \in H_{s-l+1} $, then  $ u \in H_{s+1} $. Let  $ h \in \mathbb{R}^n $ with  $ h \neq 0 $, and let  $ L^h $ represent the operator obtained from  $ L $ by replacing each coefficient  $ \alpha $ by its difference quotient

 $$ \frac{\alpha(x+h)-\alpha(x)}{|h|}. $$ 

Then it follows for  $ \varphi \in \mathcal{P} $, and hence by continuity for all  $ u \in H_{-\infty} $, that

 $$ L(u^{h})=(L u)^{h}-L^{h}(T_{h}u) $$ 

It follows from (2) and the Fundamental Inequality 6.29(1), that

 $$ \begin{aligned}{\|u^{h}\|_{s}}&{{}\leq\operatorname{c o n s t}\|L(u^{h})\|_{s-l}+\operatorname{c o n s t}\|u^{h}\|_{s-l}}\\ {}&{{}\leq\operatorname{c o n s t}\|(L u)^{h}\|_{s-l}+\operatorname{c o n s t}\|L^{h}(T_{h}u)\|_{s-l}+\operatorname{c o n s t}\|u^{h}\|_{s-l}.}\\ \end{aligned} $$ 

Now since the coefficients of the operator L are periodic  $ C^{\infty} $ functions, their difference quotients are uniformly bounded, so that

 $$ \|L^{h}(T_{h}u)\|_{s-l}\leq\mathrm{c o n s t}\|T_{h}(u)\|_{s} $$ 

where the constant does not depend on h. It follows from (3), (4), and 6.19(3) and (5) that

 $$ \left\Vert{u^{h}}\right\Vert_{s}\leq\mathrm{c o n s t}\left\Vert{L u}\right\Vert_{s-l+1}+\mathrm{c o n s t}\left\Vert{u}\right\Vert_{s}, $$ 

where the right-hand side is independent of $h$. Thus, by $6.20$, $u \in H_{s+1}$, and the theorem is proved.

##### REDUCTION TO THE PERIODIC CASE

6.31 Remarks Before beginning the proof of Theorem 6.5 we need to establish some convenient notation and to make a few observations.

We are going to let $C^{\infty}$ denote the set of all complex $m$-space valued $C^{\infty}$ functions on $\mathbb{R}^n$. $C_0^{\infty}$ will denote those of compact support, and $C_0^{\infty}(V)$ those whose compact support lies in $V$. By the $L_2$ inner product on $C_0^{\infty}$ we shall mean

 $$ \langle u,v\rangle=\frac{1}{(2\pi)^{n}}\int_{R^{n}}u\cdot v, $$ 

where  $ u \cdot v $ as before denotes the Hermitian product  $ u_1\overline{v_1} + \cdots + u_m\overline{v_m} $.

Let $V$ be an open set in $\mathbb{R}^n$ with $\overline{V}$ contained in some $2\pi$ cube. Then by extending periodically we can (and do) identify $C_0^\infty(V)$ with a subspace of $\mathcal{P}$. Observe that the $L_2$ inner product on $C_0^\infty(V)$ agrees with the $L_2$ inner product on $C_0^\infty(V)$ considered as a subset of $\mathcal{P}$, which in turn agrees with the Sobolev inner product $\|\cdot\|_0$.

Now suppose that $L$ is an elliptic partial differential operator of order $l$ on $C^\infty$ (no assumption of periodic coefficients). $L$ has a formal adjoint $L^*$ on $C_0^\infty$, with respect to the ordinary $L_2$ inner product on $C_0^\infty$, obtained by integration by parts. Just as in 6.24, if $L = (L_{ij})$ where $L_{ij} = \sum a_i^e D^e$, then $L^* = (L_{ij}^*)$ where $L_{ij}^* = \sum D^e a_{ji}^e$. $L^*$ is also a differential operator of order $l$.

Now let $p \in \mathbb{R}^n$. Then there is a sufficiently small neighborhood $V$ of $p$ and a periodic elliptic operator $L$ such that $L$ agrees with $L$ on $V$. For let $L_0$ denote the constant coefficient operator determined by $L$ at $p$. Then since $L$ is elliptic at $p$, there is some $\varepsilon > 0$ such that any operator whose coefficients are everywhere within $\varepsilon$ in absolute value of the corresponding coefficients of $L_0$ is elliptic. So let $U$ be a neighborhood of $p$, small enough to be contained in some $2\pi$ cube $Q$, on which the coefficients of $L$ differ from the corresponding coefficients of $L_0$ by at most $\varepsilon$; and let $V \subset \overline{V} \subset U$. Choose a $C^\infty$ function $\varphi$ with $0 \leq \varphi \leq 1$ such that $\varphi$ is 1 on $V$ and has support in $U$. Then the operator

 $$ \varphi\cdot L+(1-\varphi)L_{0} $$ 

is elliptic on all of  $ \mathbb{R}^n $ and clearly can be extended from Q to be a periodic elliptic operator L which agrees with L on V.

We shall need the following slight extension of the formal adjoint property of  $ L^* $. Let  $ u \in H_s $, and let  $ \varphi \in C_0^\infty(V) $. Then

 $$ \langle\mathcal{I}u,\varphi\rangle_{0}=\langle u,L^{*}\varphi\rangle_{0}. $$ 

For let  $ \psi_{j} \to u $ in  $ \| \| $, with  $ \psi_{j} \in \mathcal{P} $. Then

 $$ \begin{aligned}{\langle\widetilde{L}\psi_{j},\varphi\rangle_{0}}&{{}=\langle\widetilde{L}\psi_{j},\varphi\rangle=\langle L\psi_{j},\varphi\rangle}\\ {}&{{}=\langle\psi_{j},L^{*}\varphi\rangle=\langle\psi_{j},L^{*}\varphi\rangle_{0},}\\ \end{aligned} $$ 

so that

 $$ \begin{aligned}{|\langle\widetilde{L}u,\varphi\rangle_{0}-\langle u,L^{*}\varphi\rangle_{0}|}&{{}=|\langle\widetilde{L}(u-\psi_{j}),\varphi\rangle_{0}-\langle u-\psi_{j},L^{*}\varphi\rangle_{0}|}\\ {}&{{}\leq\|\widetilde{L}(u-\psi_{j})\|_{s-l}\|\varphi\|_{-s+l}+\|u-\psi_{j}\|_{s}\|L^{*}\varphi\|_{-s}}\\ {}&{{}\leq\operatorname{c o n s t}\|u-\psi_{j}\|_{s}\|\varphi\|_{-s+l}+\|u-\psi_{j}\|_{s}\|L^{*}\varphi\|_{-s},}\\ \end{aligned} $$ 

which converges to zero as  $ j \to \infty $.

Let $V$, as above, be an open set whose closure lies in some $2\pi$ cube. Let $u$ and $v$ belong to $H_{s}$. Then we shall say that $u$ and $v$ are equal on $V$ if

 $$ \langle u-v,\varphi\rangle_{0}=0 $$ 

for all $\varphi \in C_0^\infty(V)$. We shall say that a periodic operator $L$ has support in $V$ if the coefficients of $L$ belong to $C_0^\infty(V) \subset \mathcal{P}$. Now, if $L$ has support in $V$, and if the elements $u$ and $v$ of $H_s$ are equal on $V$, then

 $$ L u=L v. $$ 

For by 6.18(f), it is sufficient to prove that

 $$ \langle L(u-v),\varphi\rangle_{0}=0 $$ 

for all $\varphi \in \mathcal{P}$. But applying (2) (with $\tilde{L} = L$), we obtain

 $$ \langle L(u-v),\varphi\rangle_{0}=\langle(u-v),L^{*}\varphi\rangle_{0} $$ 

which is zero by (3) since  $ L^{*}\varphi\in C_{0}^{\infty}(V)\subset\mathcal{P} $.

6.32 Proof of the Regularity Theorem 6.5 We are going to restate Theorem 6.5 in slightly different notation, adapted to the local problem in  $ \mathbb{R}^{n} $ to which the theorem will immediately be reduced. We shall use  $ \langle $,  $ \rangle $ to denote the inner product 6.1(5) on  $ E^{p}(M) $. We shall prove:

(1) Given a $C^\infty$ p-form for $M$ and a bounded linear functional $l^\prime$: $E^p(M) \to \mathbb{R}$ such that $l^\prime(\Delta^* \phi) = \langle f, \phi \rangle^\prime$ for every $\phi \in E^p(M)$, then there exists a $C^\infty$ p-form $u$ on $M$ such that $l^\prime(t) = \langle u, t \rangle^\prime$ for every $t \in E^p(M)$.

We note that the last statement of Theorem 6.5, which says that $\Delta u = f$, is an immediate consequence of (1), since, as we have already observed in 6.4(6), $\langle\Delta u,\varphi\rangle' = \langle u,\Delta^*\varphi\rangle' = l'(\Delta^*\varphi) = \langle f,\varphi\rangle'$ for all $\varphi \in E^p(M)$.

We now reduce Theorem 6.5 to a local problem. Let $U$ be a coordinate patch on $M$ with coordinate map $\gamma$ such that $\gamma(U) = \mathbb{R}^n$. Via this coordinate system, differentiable $p$-forms become vector-valued functions from $\mathbb{R}^n$ to $\mathbb{R}^m \subset \mathbb{C}^m$ where $m = \binom{n}{p}$. We adopt the notation of 6.31. So via the coordinate system $(U,\gamma)$, $p$-forms on $M$ yield elements of $C^\infty$; and in the reverse direction, each element of $C^\infty$ extends by zero to a complex-valued $p$-form on all of $M$. The Laplacian $\Delta$ induces a partial differential operator $L$ of order 2 on $C^\infty$. The basic fact that we shall need concerning $L$ is that $L$ is an elliptic operator. This we assume for the moment and shall establish in 6.35. We let $L^*$ denote the formal adjoint of $L$ with respect to the $L_2$ inner product on $C_0^\infty$.

We extend the inner product  $ \langle\cdot,\rangle' $ to complex-valued p-forms in the obvious way, so that if  $ u_{1}, u_{2}, v_{1} $, and  $ v_{2} $ are real-valued p-forms, then

 $$ \langle u_{1}+i u_{2},v_{1}+i v_{2}\rangle^{\prime}=\langle u_{1},v_{1}\rangle^{\prime}+\langle u_{2},v_{2}\rangle^{\prime}+i(\langle u_{2},v_{1}\rangle^{\prime}-\langle u_{1},v_{2}\rangle^{\prime}). $$ 

Then by transferring this to Euclidean space we obtain another inner product  $ \langle $,  $ \rangle $ on  $ C_{0}^{\infty} $ induced from the inner product on complex-valued p-forms on M. It follows from the observation that both the  $ L_{2} $ inner product  $ \langle $,  $ \rangle $ and the inner product  $ \langle $,  $ \rangle $ on  $ C_{0}^{\infty} $ are integrals of pointwise inner products, that there exists a matrix A of smooth functions on  $ R^{n} $, Hermitian and positive definite at each point, such that

 $$ \langle\varphi,\psi\rangle^{\prime}=\langle\varphi,A\psi\rangle $$ 

for all  $ \varphi, \psi \in C_0^\infty $.

The adjoint of $L$ on $C_0^\infty$ with respect to $\langle \ , \rangle' $ is simply $\Delta^*$ restricted to $C_0^\infty$. We claim that for $\varphi \in C_0^\infty$,

 $$ {\cal L}^{*}\varphi=A\Delta^{*}A^{-1}\varphi. $$ 

Indeed, for arbitrary  $ \psi \in C_{0}^{\infty} $,

 $$ \begin{aligned}{\langle L^{*}\varphi,\psi\rangle}&{{}=\langle\varphi,L\psi\rangle=\langle A^{-1}\varphi,L\psi\rangle^{\prime}}\\ {}&{{}=\langle\Delta^{*}A^{-1}\varphi,\psi\rangle^{\prime}=\langle A\Delta^{*}A^{-1}\varphi,\psi\rangle.}\\ \end{aligned} $$ 

We extend the linear functional $l': E^p(M) \to \mathbb{R}$ complex linearly to complex-valued differential forms, and we define a complex-valued linear functional $l$ on $C_0^\infty$ by setting

 $$ I(\varphi)=I^{\prime}(A^{-1}\varphi). $$ 

We claim that $l$ is locally represented by a $C^{\infty}$ function. Precisely, we shall prove:

(5) If $p \in \mathbb{R}^n$, then there is a neighborhood $W_p$ of $p$ and an element $u_p \in \mathcal{P}$ such that $l(t) = \langle u_p, t \rangle$ for every $t \in C_0^\infty(W_p)$.

First we show that (5) implies (1). It follows from (5) that for each $p, q \in \mathbb{R}^n$, $u_p \mid W_p \cap W_q = u_q \mid W_p \cap W_q$, since both $u_p$ and $u_q$ have the same $L_2$ inner product with all elements of $C_0^w(W_p \cap W_q)$. Thus the $u_p$ piece together to give $u \in C^\infty$ such that $u \mid W_p = u_p \mid W_p$ for each $p \in \mathbb{R}^n$. Now let $\{\varphi_i\}$ be a partition of unity on $\mathbb{R}^n$ subordinate to the $\{W_p\}$. Then if $t \in C_0^\infty$, $l(t) = \sum_i l(\varphi_i t) = \sum_i \langle u, \varphi_i t \rangle = \langle u, t \rangle$. Now if $\varphi$ is a smooth $p$-form on $M$ with support in $U$, then $l'(\varphi) = l(A\varphi) = \langle u, A\varphi \rangle = \langle u, \varphi \rangle$. By the same argument as above, the $u$'s for various coordinate systems on $M$ piece together to form a $C^\infty$ $p$-form $u$ (necessarily real-valued) on $M$ such that $l'(\varphi) = \langle u, \varphi \rangle$ for every $\varphi \in E^p(M)$. Thus we have reduced the proof of (1) to the proof of (5), which follows.

Let $p \in \mathbb{R}^n$ be fixed, and let $Q'$ be some open $2\pi$ cube containing $p$. Choose an open set $V$ such that $p \in V \subset \overline{V} \subset Q'$, and let

 $$ \tilde{l}=l\mid C_{0}^{\infty}(V). $$ 

First of all, we observe that  $ \tilde{I} $ is a bounded linear functional on  $ C_0^\infty(V) $. For since  $ \overline{V} $ is compact, the matrix norms  $ \|A_a^{-1}\| $ have a maximum as x ranges over  $ \overline{V} $, and thus, using the fact that  $ I' $ is bounded, we obtain

 $$ \begin{aligned}{|\tilde{l}(\varphi)|}&{{}=|l(\varphi)|=|l^{\prime}(A^{-1}\varphi)|\leq\operatorname{c o n s t}\|A^{-1}\varphi\|^{\prime}}\\ {}&{{}=\operatorname{c o n s t}\left(\langle A^{-1}\varphi,A^{-1}\varphi\rangle^{\prime}\right)^{1/2}=\operatorname{c o n s t}\langle\varphi,A^{-1}\varphi\rangle^{1/2}}\\ {}&{{}\leq\operatorname{c o n s t}\left(\|\varphi\|\|A^{-1}\varphi\|\right)^{1/2}\leq\operatorname{c o n s t}\|\varphi\|}\\ \end{aligned} $$ 

for all  $ \varphi \in C_0^\infty(V) $. Second, we observe that it follows from (6), (4), (3), (2), and (1) that

 $$ \tilde{l}(L^{*}\varphi)=l^{\prime}(A^{-1}L^{*}\varphi)=l^{\prime}(\Delta^{*}A^{-1}\varphi)=\langle f,A^{-1}\varphi\rangle^{\prime}=\langle f,\varphi\rangle $$ 

for all  $ \varphi \in C_{0}^{\infty}(V) $. Thus  $ \tilde{l} $ is a weak solution of  $ Lu = f $.

Since $\tilde{l}$ is bounded, $\tilde{l}$ extends to a bounded linear functional on $H_0$. It follows that there is an element $\tilde{u} \in H_0$ such that

(8)

 $$ \tilde{l}(t)=\langle\tilde{u},t\rangle_{0}\quad\mathrm{f o r~a l l~}t\in H_{0}. $$ 

Our task is to show that on a small enough neighborhood of $p$, the element $\tilde{u}$ agrees with an element of $\mathcal{P}$.

Choose a neighborhood $O_{0}$ of $p$ with $\overline{O_{0}} \subset V$ small enough so that there exists a periodic elliptic operator $\widetilde{L}$ which agrees with $L$ on $O_{0}$ (cf. 6.31). Choose a neighborhood $O$ of $p$ such that $\overline{O} \subset O_{0}$, and then choose a sequence

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//fa06cdba-fa45-445f-af46-dfae42077371/markdown_2/imgs/img_in_image_box_490_419_808_707.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A17Z%2F-1%2F%2F459664f837b9100750613cf53e77f579efaf1c49f98a3507266ccb018bf6bfe8" alt="Image" width="33%" /></div>


of neighborhoods $O_n$ of $p$ such that $\overline{O} \subset O_n$ and $\overline{O_n} \subset O_{n-1}$ for each $n=1,2,\ldots$. For each integer $n\geq1$, choose a $C^\infty$ function $\omega_n$ which is identically equal to 1 on $O_n$, has values between 0 and 1, and has support in $O_{n-1}$. Let

(9)

 $$ v_{1}=\omega_{1}\tilde{u}\in H_{0}. $$ 

Then

 $$ \begin{array}{r}{\tilde{L}\boldsymbol{v}_{1}=\tilde{L}\omega_{1}\tilde{\boldsymbol{u}}=\omega_{1}\tilde{L}\tilde{\boldsymbol{u}}+\boldsymbol{M}_{1}\tilde{\boldsymbol{u}},}\end{array} $$ 

where

 $$ \begin{array}{r}{M_{1}=\tilde{L}\omega_{1}-\omega_{1}\tilde{L}.}\end{array} $$ 

In order to apply 6.30, we must first determine to which Sobolev space the right-hand side of (10) belongs.

First, we claim that

(12)

 $$ \omega_{1}\tilde{L}\tilde{u}=\omega_{1}f, $$ 

from which it follows that  $ \omega_1\tilde{L}\tilde{u} \in C_0^\infty(O_0) $ and thus belongs to  $ H_s $ for each  $ s $. Now both sides of (12) belong to some  $ H_s $, and it follows from 6.18(f) that for (12) to hold, it is sufficient to prove that

 $$ \langle\omega_{1}\tilde{L}\tilde{u}-\omega_{1}f,\varphi\rangle_{0}=0 $$ 

for all  $ \varphi \in \mathcal{P} $. We compute, using (7), (8), 6.18(9), and 6.31(2):

 $$ \begin{aligned}{\langle\omega_{1}\widetilde{L}\widetilde{u}-\omega_{1}f,\varphi\rangle_{0}}&{{}=\langle\omega_{1}\widetilde{L}\widetilde{u},\varphi\rangle_{0}-\langle\omega_{1}f,\varphi\rangle_{0}}\\ {}&{{}=\langle\widetilde{L}\widetilde{u},\omega_{1}\varphi\rangle_{0}-\langle f,\omega_{1}\varphi\rangle_{0}}\\ {}&{{}=\langle\widetilde{u},L^{*}\omega_{1}\varphi\rangle_{0}-\widetilde{l}(L^{*}\omega_{1}\varphi)}\\ {}&{{}=\widetilde{l}(L^{*}\omega_{1}\varphi)-\widetilde{l}(L^{*}\omega_{1}\varphi)=0.}\\ \end{aligned} $$ 

Thus (12) holds. Now since $L$ (and hence $\tilde{L}$) is an operator of order 2, then $M_1$ is of order 1; hence $M_1\tilde{u} \in H_{-1}$. Thus the right-hand side of (10) belongs to $H_{-1}$. It follows from the periodic regularity theorem 6.30 that $v_1 \in H_1$. Now we let

 $$ v_{2}=\omega_{2}\tilde{u}. $$ 

Then

 $$ \begin{array}{r}{\tilde{L}\boldsymbol{v}_{\mathbf{z}}=\omega_{\mathbf{z}}\tilde{L}\tilde{\boldsymbol{u}}+\boldsymbol{M}_{\mathbf{z}}\tilde{\boldsymbol{u}}=\omega_{\mathbf{z}}\tilde{L}\tilde{\boldsymbol{u}}+\boldsymbol{M}_{\mathbf{z}}\boldsymbol{v}_{\mathbf{1}},}\end{array} $$ 

where the last equality follows from 6.31(4) since  $ M_2 = \tilde{L}\omega_2 - \omega_2\tilde{L} $ has support in  $ O_1 $ and  $ \tilde{u} = v_1 $ on  $ O_1 $. Now, arguing as before, we see that the right-hand side of (15) lies in  $ H_0 $. Thus by 6.30,  $ v_2 \in H_2 $. Continuing in the same manner, we obtain

 $$ v_{n}=\omega_{n}\tilde{u}\quad\mathrm{w i t h}v_{n}\in H_{n}. $$ 

Finally, let $W_p$ be an open neighborhood of $p$ with $\overline{W}_p \subset O$, and let $\omega$ be identically 1 on $W_p$ with values between 0 and 1, and with support in $O$. Then $\omega\tilde{u} = \omega\omega_n\tilde{u}$ for each $n$; and so by (16), $\omega\tilde{u} \in H_n$ for every $n$. By the corollary to the Sobolev lemma 6.22, $\omega\tilde{u}$ represents a $C^\infty$ function $u \in \mathcal{P}$. Now if $t \in C_0^\infty(W_p)$, then

 $$ \begin{aligned}{l(t)}&{{}=\tilde{l}(t)=\langle\tilde{u},t\rangle_{0}=\langle\tilde{u},\omega t\rangle_{0}}\\ {}&{{}=\langle\omega\tilde{u},t\rangle_{0}=\langle u,t\rangle,}\\ \end{aligned} $$ 

and (5) is proved. Except for a proof of the fact that $L$ is elliptic, this completes the proof of Theorem 6.5.

6.33 Proof of Theorem 6.6 It suffices to show that if $m \in M$, then there is some neighborhood of $m$ such that if $\varphi$ is any $C^\infty$ function on $M$ with support in that neighborhood, then $\{\varphi\alpha_n\}$ has a Cauchy subsequence. For then we simply cover $M$ by a finite number of such neighborhoods

and take a partition of unity $\varphi_{1},\ldots,\varphi_{N}$ subordinate to this cover. One can select a subsequence $\alpha_{n_{k}}$ such that $\varphi_{j}\alpha_{n_{k}}$ is Cauchy for each $j$. Then $\{\alpha_{n_{k}}\}$ is Cauchy for

 $$ \begin{array}{r l}{\|\alpha_{n_{k}}-\alpha_{n_{1}}\|=\Big\|\underset{j=1}{\overset{N}{\sum}}\varphi_{j}(\alpha_{n_{k}}-\alpha_{n_{1}})\Big\|}&{\leq\quad\underset{j=1}{\overset{N}{\sum}}\|\varphi_{j}\alpha_{n_{k}}-\varphi_{j}\alpha_{n_{1}}\|.}\end{array} $$ 

We reduce the problem to Euclidean space by choosing a coordinate neighborhood of $m$ with $m$ going to $p \in \mathbb{R}^n$. We continue with the notation and setup as developed in 6.31 and 6.32; in particular, the norm on $M$ and the corresponding induced norm on $C_0^\infty$ will now be denoted by $\| \cdot \|$. Let $\varphi$ be a real-valued $C^\infty$ function with support in $O_0$. It suffices to show that the sequence $\{\varphi_{\alpha_n}\}$ of elements of $\mathcal{P}$ has a Cauchy subsequence $\{\varphi_{\alpha_n}\}$ in the 0-norm, since the 0-norm and the $L_2$-norm agree on $C_0^\infty(O_0)$, and the $L_2$-norm and the norm $\| \cdot \|$ are equivalent on $C_0^\infty(O_0)$. According to the Rellich lemma 6.23, in order to prove that $\{\varphi_{\alpha_n}\}$ has a Cauchy subsequence in the 0-norm, it is sufficient to show that the sequence is bounded in $H_1$. It follows from the Fundamental Inequality that

 $$ \begin{aligned}{\|\varphi\alpha_{n}\|_{1}}&{{}\leq\operatorname{c o n s t}\left(\|\widetilde{L}\varphi\alpha_{n}\|_{-1}+\|\varphi\alpha_{n}\|_{-1}\right)}\\ {}&{{}=\operatorname{c o n s t}\left(\|L\varphi\alpha_{n}\|_{-1}+\|\varphi\alpha_{n}\|_{-1}\right)}\\ {}&{{}\leq\operatorname{c o n s t}\|\varphi L\alpha_{n}\|_{-1}+\operatorname{c o n s t}\|(L\varphi-\varphi L)\alpha_{n}\|_{-1}+\operatorname{c o n s t}\|\varphi\alpha_{n}\|_{-1}.}\\ \end{aligned} $$ 

Now

 $$ \begin{aligned}{\|\varphi L\alpha_{n}\|_{-1}}&{{}\leq\|\varphi L\alpha_{n}\|_{0}=\|\varphi L\alpha_{n}\|}\\ {}&{{}\leq\operatorname{c o n s t}\|\varphi L\alpha_{n}\|^{\prime}\leq\operatorname{c o n s t}\|L\alpha_{n}\|^{\prime}\leq\operatorname{c o n s t}\|\Delta\alpha_{n}\|^{\prime}.}\\ \end{aligned} $$ 

Let  $ \tau $ be a  $ C^{\infty} $ function with values between 0 and 1 which equals 1 on  $ O_{0} $ and has support in V. Then

 $$ (L_{\varphi}-\varphi L)\alpha_{n}=(L\varphi-\varphi L)(\tau\alpha_{n}), $$ 

so that

 $$ \begin{aligned}{\|(L\varphi-\varphi L)\alpha_{n}\|_{-1}}&{{}=\|(L\varphi-\varphi L)(\tau\alpha_{n})\|_{-1}}\\ {}&{{}\leq\operatorname{c o n s t}\|\tau\alpha_{n}\|_{0}=\operatorname{c o n s t}\|\tau\alpha_{n}\|}\\ {}&{{}\leq\operatorname{c o n s t}\|\tau\alpha_{n}\|^{\prime}\leq\operatorname{c o n s t}\|\alpha_{n}\|^{\prime}.}\\ \end{aligned} $$ 

Finally,

 $$ \begin{array}{r}{\|\varphi\alpha_{n}\|_{-1}\leq\|\varphi\alpha_{n}\|_{0}=\|\varphi\alpha_{n}\|\leq\mathrm{c o n s t}\|\varphi\alpha_{n}\|^{\prime}\leq\mathrm{c o n s t}\|\alpha_{n}\|^{\prime}.}\end{array} $$ 

So from (1), (2), (3), and (4) we obtain

 $$ \|\varphi\alpha_{n}\|_{1}\leq\mathrm{c o n s t}\left(\|\Delta\alpha_{n}\|^{\prime}+\|\alpha_{n}\|^{\prime}\right). $$ 

But by assumption $\|\Delta\alpha_n\|' $ and $\|\alpha_n\|' $ are bounded. Therefore, the sequence $\{\varphi\alpha_n\}$ is bounded in $H_1$, and the proof of Theorem 6.6 is complete (assuming the ellipticity of $L$).

#### ELLIPTICITY OF THE LAPLACE-BELTRAMI OPERATOR

6.34 Remark We shall make use of the following observation. Let $U$, $V$, and $W$ be finite dimensional inner product spaces, and suppose that

 $$ U\mathop{\longrightarrow}\limits^{\mathbf{A}}\vphantom{\int}V\mathop{\longrightarrow}\limits^{\mathbf{B}}\vphantom{W}\rightarrow W $$ 

is exact. Let $A^{*}\colon V\to U$ and $B^{*}\colon W\to V$ be the adjoints of $A$ and $B$ respectively. Then $B^{*}B+AA^{*}$ is an isomorphism on $V$. For let $v$ be a non-zero element of $V$. We need only show that $(B^{*}B+AA^{*})v\neq0$. Now

 $$ \langle(B^{*}B+A A^{*})v,v\rangle=\langle B v,B v\rangle+\langle A^{*}v,A^{*}v\rangle. $$ 

If $Bv \neq 0$, then $(B^*B + AA^*)v \neq 0$. If $Bv = 0$, then by the exactness, $v$ lies in the image of $A$. But $A^*$ is injective on the image of $A$. Thus $A^*v \neq 0$, which implies that $(B^*B + AA^*)v \neq 0$.

We shall apply this to the special case in which $U$, $V$, and $W$ are $\Lambda_{p-1}(M_{m}^{*}), \Lambda_{p}(M_{m}^{*})$, and $\Lambda_{p+1}(M_{m}^{*})$ respectively, with the inner products

 $$ \langle\omega,\tau\rangle=\ast(\omega\wedge\ast\tau), $$ 

and with $A$ and $B$ both left exterior multiplication by $\xi \in M_{m}^{*}$:

 $$ \Lambda_{p-1}(M_{m}^{*})\xrightarrow{\xi}\Lambda_{p}(M_{m}^{*})\xrightarrow{\xi}\Lambda_{p+1}(M_{m}^{*}). $$ 

According to Exercise 15 of Chapter 2, the sequence (1) is exact; and according to Exercise 14 of Chapter 2, the adjoint of  $ \xi\colon \Lambda_{p}(M_{m}^{*})\to\Lambda_{p+1}(M_{m}^{*}) $ is

 $$ (-1)^{n p}*{\xi}*:\:\Lambda_{p+1}(M_{m}^{*})\to\Lambda_{p}(M_{m}^{*}). $$ 

Thus it follows from the above remarks that

 $$ (-1)^{n p}{*}\xi{*}\xi+(-1)^{n(p-1)}\xi{*}\xi{*} $$ 

is an isomorphism on  $ \Lambda_{p}(M_{m}^{*}) $.

6.35 The Laplacian is Elliptic. In order to complete the proofs of Theorems 6.5 and 6.6, we need to prove that the operator $L$ of 6.32 induced on Euclidean space by the Laplace-Beltrami operator $\Delta$ via a coordinate system is elliptic. Proving this, according to 6.28(2), is equivalent to showing that for each $m \in M$,

 $$ \Delta(\varphi^{2}\alpha)(m)\neq0 $$ 

for each smooth form $\alpha$ such that $\alpha(m) \neq 0$ and for each $C^\infty$ function $\varphi$ on $M$ such that $\varphi(m) = 0$ but $d\varphi(m) \neq 0$. Assume that $\alpha$ is a $p$-form, and let $0 \neq d\varphi = \xi \in M_m^*$. Recall that

 $$ \Delta=(-1)^{n(\mathfrak{p}+1)+1}d{*}d{*}+(-1)^{n\mathfrak{p}+1}{*}d{*}d{.} $$ 

We compute the left-hand side of (1), keeping in mind at each stage that  $ \varphi(m) = 0 $. Thus

 $$ \begin{aligned}{d{*}d{*}(\varphi^{\sharp}\alpha)(m)}&{{}=\big(d{*}d(\varphi^{\sharp}){*}\alpha\big)(m)=\big(2d{*}\varphi(d\varphi){*}\alpha\big)(m)}\\ {}&{{}=\big(2(d\varphi){*}(d\varphi){*}\alpha\big)(m)=2\xi{*}\xi{*}\big(\alpha(m)\big).}\\ \end{aligned} $$ 

Similarly,

 $$ *d*d(\varphi^{8}\alpha)(m)=2*\xi*\xi\bigl(\alpha(m)\bigr). $$ 

Thus

 $$ \Delta(\varphi^{2}\alpha)(m)=-2[(-1)^{n p}\ast\xi\ast\xi+(-1)^{n(p-1)}\xi\ast\xi\ast]\bigl(\alpha(m)\bigr), $$ 

which is not zero, according to 6.34(3). Hence  $ \Delta $ is elliptic, and the proof of the Hodge theorem is at last complete.

6.36 Remark We have seen that for each $\xi$ in $M_m^*$ there is a well-defined linear transformation $\sigma_\Delta(\xi)$ on $\Lambda_p(M_m^*)$ defined by

 $$ \sigma_{\Delta}(\xi)(v)=\Delta(\varphi^{\sharp}\alpha)(m), $$ 

where  $ v \in \Lambda_p(M_m^*) $, where  $ \alpha $ is any  $ p $-form such that  $ \alpha(m) = v $, and where  $ \varphi $ is any  $ C^\infty $ function such that  $ \varphi(m) = 0 $ and  $ d\varphi(m) = \xi $. This linear transformation  $ \sigma_\Delta(\xi) $ is known as the symbol of the operator  $ \Delta $. The ellipticity of all the operators  $ L $ on  $ \mathbb{R}^n $ obtained from  $ \Delta $ via coordinate systems is equivalent to the property that the symbol  $ \sigma_\Delta(\xi) $ is an isomorphism at each point  $ m $ for each non-zero  $ \xi \in M_m^* $. Our computations in 6.35 contain a proof of the fact that the symbol of the exterior derivative operator  $ d $, namely  $ \sigma_d(\xi): \Lambda(M_m^*) \to \Lambda(M_m^*) $, is simply left exterior multiplication by  $ \xi $; whereas the symbol of the adjoint  $ \delta $ of  $ d $ is the adjoint of left exterior multiplication by  $ \xi $. In the theory of general partial differential operators on vector bundles over  $ M $, ellipticity is defined, as above, in terms of the symbol.

##### EXERCISES

1 Prove that  $ *\Delta = \Delta* $.

2 (a) Prove that the Green's operator G is a bounded linear operator.

(b) Prove that $G$ is self-adjoint on $(H^{p})^{\perp}$.

(c) Prove that G takes bounded sequences into sequences with Cauchy subsequences.

3 By using an integral test, prove that the series  $ \sum(1 + |\xi|^{\sharp})^{-k} $, where  $ \xi $ ranges over all  $ n $-tuples of integers  $ (\xi_1, \ldots, \xi_n) $, converges for  $ k \geq [n/2] + 1 $. (Hint: Induct on  $ n $, and evaluate the appropriate integrals in terms of spherical coordinates.)

4 Prove in detail the inequality 6.16(15).

5 Establish the existence of the matrix A of 6.32(2) together with its stated properties.

6 Derive explicit formulas for $d, \ast, \delta$, and $\Delta$ in Euclidean space. In particular, show that if

 $$ \alpha=\sum_{i_{1}<\cdots<i_{p}}\alpha_{I}\;d x_{i_{1}}\wedge\cdots\wedge d x_{i_{p}}, $$ 

then

 $$ \Delta\alpha=(-1)\sum_{i_{1}<\cdots<i_{p}}\left(\sum_{i=1}^{n}\frac{\partial^{2}\alpha_{I}}{\partial x_{i}^{2}}\right)\;d x_{i_{1}}\wedge\cdots\wedge d x_{i_{p}}. $$ 

7 Let  $ \varphi $ belong to the  $ C^{\infty} $ periodic functions  $ \mathcal{P} $ on the plane. Prove that

 $$ \left\|\frac{\partial^{2}\varphi}{\partial x\partial y}\right\|\leq\frac{1}{\varepsilon}\left\|\Delta\varphi\right\|. $$ 

8 The Rellich lemma 6.23 says that the natural injection $i: H_{t} \to H_{s}$ for $s < t$ is a compact operator; that is, it takes bounded sequences into sequences with convergent subsequences. An analogous example of this phenomenon is the following. Let $C$ denote the Banach space of periodic continuous functions on the real line, say with period $2\pi$, and with norm the sup norm $\|\cdot\|_{\infty}$. Let $C^{1}$ be the subset of $C$ consisting of functions with continuous first derivative. As a norm for $C^{1}$ we take

 $$ \left\|f\right\|=\left\|f\right\|_{\infty}+\left\|\frac{d f}{d x}\right\|_{\infty}. $$ 

Use the Arzelà-Ascoli theorem [27, p. 126] to prove that the natural injection $i\colon C^{1}\to C$ is a compact operator.

9 We shall consider a number of elliptic equations of the form $Lu = f$ on the real line. In each case, $f$ will be smooth and periodic of period 1, and we look for solutions $u$ also periodic of period 1. This restriction to periodic functions makes this in essence a problem on a compact space, the unit circle. We let $u' = du/dx$. etc.

(a)  $ u' = f $. This is the simplest example of an elliptic operator which exhibits all of the essential ingredients of the theory. What is the formal adjoint of this differential operator? Show that there is a solution u (periodic) if and only if f is orthogonal to the kernel of this adjoint.

(b)  $ u^{\prime}-u=f $. What is the kernel (in the periodic functions) in this case? What are the necessary and sufficient conditions on f for there to exist a periodic solution?

(c) $u'' = f$. Show that this operator is formally self-adjoint. Show that there is a periodic solution if and only if $f$ is orthogonal to the kernel; and using the fact that

 $$ \int_{0}^{\infty}\left(\int_{0}^{t}f(s)ds\right)dt=\int_{0}^{\infty}f(s)\left(\int_{s}^{\infty}dt\right)ds, $$ 

show that the unique solution orthogonal to the kernel is

 $$ \begin{aligned}{u(x)=}&{{}\int_{0}^{\varepsilon}t(x-1)f(t)\mathop{}{d}t\quad+\quad\int_{\varepsilon}^{1}x(t-1)f(t)\mathop{}{d}t}\\ {}&{{}+\frac{1}{2}\int_{0}^{1}t(t-1)f(t)\mathop{}{d}t.}\\ \end{aligned} $$ 

This explicitly exhibits the Green's operator for this case.

(d)  $ u'' + \pi^u = f $. Show that this operator is formally self-adjoint. What is its kernel? Derive an explicit formula for the solution u, and show that u is periodic if and only if f is orthogonal to the kernel.

10 In Theorem 6.11 we used the fact that the Green's operator commutes with $d$ in proving that each closed form on a compact orientable Riemannian manifold differs from a harmonic form by an exact form. Give a proof of this result directly from the Hodge decomposition theorem without using the Green's operator.

11 A periodic distribution $l$ is a linear functional on $\mathcal{P}$ for which there exists some integer $k \geq 0$ and a positive constant $c$ such that

 $$ |l(\varphi)|\leq c\sum_{|\alpha|\leq k}\|D^{\alpha}\varphi\|_{\infty} $$ 

for all $\varphi \in \mathcal{P}$. Prove that if $l$ is a periodic distribution, then there is an element $u \in H_{-\infty}$ such that

 $$ l(\varphi)=\langle u,\varphi\rangle_{0} $$ 

for all $\varphi \in \mathcal{P}$. Conversely show that every element of $H_{-\infty}$ determines a periodic distribution via (2).

12 Let  $ \alpha $ and  $ \beta $ be n-forms on a compact oriented manifold  $ M^n $ such that  $ \int_M \alpha = \int_M \beta $. Prove that  $ \alpha $ and  $ \beta $ differ by an exact form.

13 Show that Theorem 6.6 cannot be strengthened to the assertion of the existence of a subsequence which is convergent in  $ E^{p}(M) $.

14 One should observe that in the course of proving Theorem 6.5 we have proved the following regularity theorem. Let $L$ be an elliptic operator on $C^\infty$ (the complex $m$-space valued smooth functions on $\mathbb{R}^n$). Suppose that $u$ is sufficiently differentiable for $Lu$ to make sense, and suppose that $Lu = f$ where $f \in C^\infty$. Then $u \in C^\infty$.

In fact, we have proved more—every weak solution $l$ is smooth. Precisely: Let $l$ be a linear functional on $C_0^\infty$ which is bounded on $C_0^\infty(V)$ whenever $\overline{V}$ is compact, and which satisfies $l(L^*\varphi) = \langle f, \varphi \rangle$ for every $\varphi \in C_0^\infty$. Then $l$ is smooth in the sense that there exists $u \in C^\infty$ which represents $l$; that is, $l(t) = \langle u, t \rangle$ for every $t \in C_0^\infty$. Such a smooth representative $u$ of a weak solution $l$ is an actual solution, $Lu = f$.

15 Observe that the Cauchy-Riemann operator $(\partial/\partial x) + i(\partial/\partial y)$ is elliptic. Conclude from the general theory of elliptic operators that every holomorphic function is $C^{\infty}$. Prove that every holomorphic function is a complex-valued harmonic function on the plane, and use Green's 1st identity (Exercise 5, Chapter 4) to prove that a holomorphic function with compact support must be identically zero.

16 The Eigenvalues of the Laplacian This is an extended exercise in which the fundamental properties of the eigenfunctions and eigenvalues of the Laplacian are developed. Proofs for the more difficult parts are outlined, and in some cases are given nearly in full.

Consider the Laplace-Beltrami operator  $ \Delta $ acting on the p-forms  $ E^{p}(M) $ for some fixed p. A real number  $ \lambda $ corresponding to which there exists a not identically zero p-form u such that  $ \Delta u = \lambda u $ is called an eigenvalue of  $ \Delta $. If  $ \lambda $ is an eigenvalue, then any p-form u such that  $ \Delta u = \lambda u $ is called an eigenfunction of  $ \Delta $ corresponding to the eigenvalue  $ \lambda $. The eigenfunctions corresponding to a fixed  $ \lambda $ form a subspace of  $ E^{p}(M) $ called the eigenspace of the eigenvalue  $ \lambda $.

(a) Prove that the eigenvalues of  $ \Delta $ are non-negative.

(b) Prove that the eigenspaces of  $ \Delta $ are finite dimensional.

(c) Prove that the eigenvalues have no finite accumulation point.

(d) Prove that eigenfunctions corresponding to distinct eigenvalues are orthogonal.

(e) Existence. In order for the above statements to have substance we must prove that there exist eigenvalues of $\Delta$. First of all, zero is an eigenvalue if and only if there are non-trivial harmonic $p$-forms on $M$, and the corresponding eigenspace is precisely the space $H^p$ of harmonic forms. We shall now establish that $\Delta$ has a positive eigenvalue—in fact, a whole sequence of eigenvalues diverging to $+\infty$. Consider $\Delta$ to be restricted to $(H^p)^\perp$. Then we have $\Delta: (H^p)^\perp \to (H^p)^\perp$, and also we have the Green's operator $G: (H^p)^\perp \to (H^p)^\perp$, and $\Delta G\alpha = \alpha$, $G\Delta\alpha = \alpha$ for all $\alpha \in (H^p)^\perp$. Observe that the eigenvalues of $G \mid (H^p)^\perp$ are the reciprocals of the eigenvalues of $\Delta \mid (H^p)^\perp$. Let

 $$ \begin{array}{r}{\eta=\operatorname*{s u p}_{\|\varphi\|=1}\|G\varphi\|.}\\ {\varphi e(H^{p})^{\perp}}\end{array} $$ 

Then $\eta > 0$ and $\|G\varphi\| \leq \eta \|\varphi\|$ for every $\varphi \in (H^{\varphi})^{\perp}$. We shall prove that $1/\eta$ is an eigenvalue of $\Delta$. Let $\{\varphi_j\} \in (H^{\varphi})^{\perp}$ be a maximizing sequence for $\eta$; that is, $\|\varphi_j\| = 1$ and $\|G\varphi_j\| \to \eta$.

First, we claim that  $ \|G^2\varphi_j - \eta^2\varphi_j\| \to 0 $, for

 $$ \begin{aligned}{\|G^{\mathtt{s}}\varphi_{j}-\eta^{\mathtt{s}}\varphi_{j}\|^{\mathtt{s}}}&{{}=\|G^{\mathtt{s}}\varphi_{j}\|^{\mathtt{s}}-2\eta^{\mathtt{s}}\langle G^{\mathtt{s}}\varphi_{j},\varphi_{j}\rangle+\eta^{4}}\\ {}&{{}\leq\eta^{\mathtt{s}}\|G\varphi_{j}\|^{\mathtt{s}}\cdot-2\eta^{\mathtt{s}}\|G\varphi_{j}\|^{\mathtt{s}}+\eta^{4}\to0.}\\ \end{aligned} $$ 

Second, we claim that  $ \|G\varphi_j - \eta\varphi_j\| \to 0 $. For if we let  $ \psi_j = G\varphi_j - \eta\varphi_j $, then

where we have used the fact that  $ \langle\psi_i,G\psi_i\rangle\geq0 $. (Why?) Now there is a subsequence of the  $ \varphi_i $, call it  $ \{\varphi_i\} $, such that  $ \{G\varphi_i\} $ is Cauchy. Define a linear functional  $ I $ on  $ E^p(M) $ by setting

 $$ \begin{aligned}{0\leftarrow\langle\psi_{j},G^{2}\varphi_{j}-\eta^{3}\varphi_{j}\rangle}\\ {=\langle\psi_{j},G\psi_{j}+\eta\psi_{j}\rangle}\\ {=\langle\psi_{j},G\psi_{j}\rangle+\dot{\eta}\Vert\psi_{j}\Vert^{3}\geq\eta\Vert\psi_{j}\Vert^{3},}\\ \end{aligned} $$ 

 $$ \begin{array}{r}{I(\beta)=\operatorname*{l i m}_{j\to\infty}\eta\langle G\varphi_{j},\beta\rangle\quad\mathrm{f o r}\quad\beta\in E^{v}(M).}\end{array} $$ 

Prove that $l$ is a non-trivial weak solution of

 $$ \big(\Delta-(1/\eta)\big)u=0. $$ 

From this and the fact that  $ \Delta - 1/\eta $ is elliptic, conclude that  $ \lambda = 1/\eta $ is an eigenvalue of  $ \Delta $.

(f) Existence of Other Eigenvalues. Suppose that we have eigenvalues  $ \lambda_1 \leq \lambda_2 \leq \cdots \leq \lambda_n $ and corresponding eigenfunctions  $ u_1, u_2, \ldots, u_n $ (orthonormalized) for  $ \Delta \big| (H^p)^{\perp}  $. Let  $ R_n $ be the subspace of  $ (H^p)^{\perp} $ spanned by  $ \{u_1, \ldots, u_n\} $. Observe that  $ G $ and  $ \Delta $ map  $ (H^p \oplus R_n)^{\perp} $ into itself, then define

 $$ \eta_{n+1}=\operatorname*{s u p}_{\substack{\|\varphi\|-1\\ \varphi\in(H^{p}\oplus R_{n})^{\perp}}}\|G\varphi\| $$ 

and proceed as in part (e) to establish that  $ \lambda_{n+1} = 1/\eta_{n+1} $ is an eigenvalue of  $ \Delta $. Clearly,  $ \lambda_{n+1} \geq \lambda_n $.

(g) $L_{2}$ Completeness. Let $\lambda_{1} \leq \lambda_{2} \leq \cdots \leq$ be the eigenvalues of $\Delta$ on $E^{p}(M)$, where each eigenvalue is included as many times as the dimension of its eigenspace, with a corresponding orthonormalized sequence of eigenfunctions $\{u_{i}\}$. Let $\alpha \in E^{p}(M)$. Then

 $$ \lim_{n\to\infty}\left\|\alpha-\sum_{i=1}^{n}\langle\alpha,u_{i}\rangle u_{i}\right\|=0. $$ 

For the proof, let $k$ be the dimension of $H^p$. Then there exists $\beta \in (H^p)^\perp$ such that $G\beta = \alpha - \sum_{i=1}^{k} \langle \alpha, u_i \rangle u_i$. It follows that

 $$ \left\|\alpha-\sum_{i=1}^{n}\langle\alpha,u_{i}\rangle u_{i}\right\|=\left\|G\left(\beta-\sum_{i=k+1}^{n}\langle\beta,u_{i}\rangle u_{i}\right)\right\| $$ 

for $n > k$. But, by the definition of $\lambda_{n+1}$,

 $$ \begin{align*}\bigg\|G\bigg(\beta-\sum_{i=k+1}^{n}\langle\beta,u_{i}\rangle u_{i}\bigg)\bigg\|&\leq\frac{1}{\lambda_{n+1}}\bigg\|\beta-\sum_{i=k+1}^{n}\langle\beta,u_{i}\rangle u_{i}\bigg\|\\&\leq\frac{1}{\lambda_{n+1}}\|\beta\|\to0\quad as\quad n\to\infty.\end{align*} $$ 

(h) Uniform Completeness. The uniform norm  $ \|\alpha\|_{\infty} $ is defined on  $ E^{p}(M) $ by

 $$ \|\alpha\|_{\infty}=\operatorname*{s u p}_{m\in\mathcal{M}}\left(*(\alpha\land*\alpha)(m)\right)^{1/3}. $$ 

From the Sobolev inequality 6.22(1) and the compactness of $M$, one can conclude that there exists a large enough integer $k$ and a constant $c > 0$ such that

 $$ \|\alpha\|_{\infty}\leq c\|(1+\Delta)^{k}\alpha\| $$ 

for every $\alpha \in E^p(M)$. Let $\alpha \in E^p(M)$, and let $P_n(\alpha) = \sum_{i=1}^{n} \langle \alpha, u_i \rangle u_i$, where we are continuing with the notation of part (g). Now $\Delta P_n = P_n \Delta$, so that

 $$ \begin{aligned}{\|\alpha-P_{n}(\alpha)\|_{\infty}}&{{}\leq c\left\|(1+\Delta)^{k}[\alpha-P_{n}(\alpha)]\right\|}\\ {}&{{}=\|\varphi-P_{n}\varphi\|\to0,}\\ \end{aligned} $$ 

where  $ \varphi = (1 + \Delta)^{k}\alpha $.

17 We define the operator  $ \Delta^s \colon E^p(M) \to E^p(M) $ by  $ \Delta^s(\alpha) = \Delta(\Delta\alpha) $. Discuss the solvability of  $ \Delta^s\alpha = \beta $.

18 Consider the operator

 $$ L=\sum_{i,j=1}^{n}a_{ij}\frac{\partial^{2}}{\partial x_{i}\partial x_{j}}+\sum_{i=1}^{n}b_{i}\frac{\partial}{\partial x_{i}}+c $$ 

acting on $C^{2}(\mathbb{R}^{n})$. Show that there is no loss of generality in assuming that $a_{ij}=a_{ji}$, and prove that $L$ is elliptic at a point $x$ if and only if the matrix $(a_{ij}(x))$ is (positive or negative) definite. In particular, show that the wave equation

 $$ \Box u=\frac{\partial^{2}u}{\partial x^{2}}-\frac{\partial^{2}u}{\partial y^{2}}=f $$ 

is not elliptic, and give an example where

 $$ \Box u=f\in C^{\infty}\quad\mathrm{b u t}\quad u\notin C^{\infty}. $$ 

19 Consider $\Delta\colon E^p(M)\to E^p(M)$. Prove that if $\lambda$ is the minimum eigenvalue of $\Delta$, and if $c>-\lambda$, then $(\Delta+c)\alpha=\beta$ can be solved for every $\beta\in E^p(M)$.

20 The Peter-Weyl Theorem The representative ring of a compact Lie group $G$ is the ring generated over the complex numbers by the set of all continuous functions $f$ for which there is a continuous homomorphism $\rho: G \to G/(n, \mathbb{C})$ for some $n$ such that $f = \rho_{ij}$ for some choice of $i$ and $j$. The Peter-Weyl theorem states that the representative ring is dense in the space of complex-valued continuous functions on $G$ in the uniform norm. That is, if $g$ is a complex-valued continuous function on $G$, and if $\varepsilon > 0$ is given, then there is a function $f$ in the representative ring such that $|f(\sigma) - g(\sigma)| < \varepsilon$ for all $\sigma \in G$. We outline a proof of this theorem which is based on the uniform completeness of the eigenfunctions of the Laplacian. One can choose a Riemannian structure on $G$ such that each of the diffeomorphisms $l_\sigma$ for $\sigma \in G$ (left translation by $\sigma$) is an isometry (that is, $\langle v, w \rangle_\tau = \langle dl_\sigma v, dl_\sigma w \rangle_\sigma$ for all $\tau \in G$ and all $v, w \in G_\tau$). Since the $C^\infty$ functions are dense in the space of continuous functions in the uniform norm, and since by Exercise 16(h) the direct sum of the eigenspaces of the Laplacian is dense in the space of $C^\infty$ functions in the uniform norm, it suffices for the Peter-Weyl theorem to prove that each eigenfunction of the Laplacian $\Delta: C^\infty(G) \to C^\infty(G)$ belongs to the representative ring.

Now, G acts on the  $ C^{\infty} $ functions on G by

 $$ \sigma(f)=f\circ l_{*}\quad\mathrm{f o r~}\sigma\in G. $$ 

Prove that since the $l_{e}$ are isometries, this action commutes with the Laplacian:

 $$ \Delta(f\circ l_{e})=(\Delta f)\circ l_{e}\qquad(\sigma\in G). $$ 

Let $V_\lambda$ be the (finite dimensional) eigenspace associated with the eigenvalue $\lambda$ of $\Delta$: $C^\infty(G) \to C^\infty(G)$. Prove that the action of $G$ leaves $V_\lambda$ invariant. Then let $\varphi_1, \ldots, \varphi_n$ be a basis of $V_\lambda$, and let

 $$ \sigma(\varphi_{i})=\sum_{j}g_{i j}(\sigma)\varphi_{j}. $$ 

Then $\sigma \mapsto \{g_{if}(\sigma)\}$ is a homomorphism of $G \to Gl(n, \mathbb{R})$. Prove that this homomorphism is continuous. Then observe that

 $$ \varphi_{i}(\sigma)=\varphi_{i}\circ l_{\sigma}(e)=\sum_{j}g_{i j}(\sigma)\varphi_{j}(e), $$ 

so that  $ \varphi_{i} $ belongs to the representative ring.

21 The reader who is familiar with the theory of vector bundles should observe that the results in this chapter on the Laplace-Beltrami operator are valid for general elliptic operators on vector bundles. We outline the statements of the results in this situation:

Let $E$ and $F$ be (real or complex) vector bundles over a compact orientable manifold $M$. Let $C^\infty(E)$ and $C^\infty(F)$ denote the vector spaces of smooth sections of $E$ and $F$ respectively. A (linear) differential operator $L$ of order $l$ from $E$ to $F$ is a linear map from $C^\infty(E)$ to $C^\infty(F)$ which when expressed in terms of local trivialization of $E$ and $F$ yields an ordinary linear partial differential operator of order $l$. The operator $L$ is elliptic if it is locally elliptic. Equivalently, ellipticicity of $L$ can be defined in terms of the symbol as in 6.36. Observe that for $L$ to be elliptic, the fibre dimensions of $E$ and $F$ must be equal. Choose inner products in the fibres $E_m$ and $F_m$ which vary smoothly with $m$, and choose a Riemannian structure and an orientation on $M$ with respect to which smooth functions can be integrated over $M$. By integrating the fibre inner products over $M$, we obtain inner products on $C^\infty(E)$ and $C^\infty(F)$. Let $L: C^\infty(E) \to C^\infty(F)$ be a differential operator. Prove that $L$ has a formal adjoint $L^*: C^\infty(F) \to C^\infty(E)$. Assume that $L$ is elliptic.

(a) Prove that ker L and ker  $ L^{*} $ are finite dimensional.

(b) Prove that  $ C^{\infty}(E) $ and  $ C^{\infty}(F) $ have the following orthogonal direct sum decompositions:

 $$ \begin{aligned}{}&{{}C^{\infty}(F)=L\big(C^{\infty}(E)\big)\oplus\ker L^{*},}\\ {}&{{}C^{\infty}(E)=L^{*}\big(C^{\infty}(F)\big)\oplus\ker L.}\\ \end{aligned} $$ 

22 Let $\varphi_n$, for $n=1,2,3,\ldots$, be a periodic $C^\infty$ function on the plane which agrees with $\log \log(1/(r+(1/n)))$ for $0 \leq r \leq \frac{1}{2}$, where $r = \sqrt{x^2 + y^2}$. Show that there is no constant $c > 0$ such that

 $$ \left\|\varphi_{n}\right\|_{\infty}\leq c\left\|\varphi_{n}\right\|_{1}\qquad\mathrm{f o r~a l l~}n. $$ 

This shows, in the case $n=2$, that the restriction $t\geq[n/2]+1$ in Corollary (b) of the Sobolev lemma 6.22 is essential.

23 Let $L$ be a (linear) elliptic operator on the $C^\infty$ functions on a compact oriented Riemannian manifold $M$. Let $\gamma$ be a diffeomorphism of $M$ which preserves the volume form on $M$. We say that a $C^\infty$ function $f$ on $M$ is invariant under $\gamma$ if $f\circ\gamma=f$, and we say that the operator $L$ is invariant under $\gamma$ if $Lu\circ\gamma=L(u\circ\gamma)$ for all $C^\infty$ functions $u$ on $M$. Suppose that $L$ and $f$ are invariant under $\gamma$ and that $f$ is orthogonal to the kernel of $L^*$. Prove that there is an invariant solution $u$ of $Lu=f$.



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Bibliography</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Index of Notation</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Index</td></tr></table>

## Bibliography

[1] Bers, L., F. John, and M. Schechter. Partial Differential Equations. New York: John Wiley & Sons, Inc., 1964.

[2] Bishop, R. L., and R. J. Crittenden. Geometry of Manifolds. New York: Academic Press, 1964.

[3] Bredon, G. E. Sheaf Theory. New York: McGraw-Hill, 1967.

[4] Cartan, H. Séminaire 1950/1951. Paris: Ecole Normale Supérieure, 1955.

[5] Chevalley, C. Theory of Lie Groups I. Princeton, N.J.: Princeton University Press, 1946.

[6] Fleming, W. H. Functions of Several Variables. Reading, Mass.: Addison-Wesley, 1965.

[7] Godement, R. Topologie Algébrique et Théorie des Faisceaux. Paris: Hermann, 1958.

[8] Gunning, R. C. Lectures on Riemann Surfaces. Princeton, N.J.: Princeton University Press, 1966.

[9] Helgason, S. Differential Geometry and Symmetric Spaces. New York: Academic Press, 1962.

[10] Hodge, W. V. D. The Theory and Applications of Harmonic Integrals. 2d ed. Cambridge: Cambridge University Press, 1952.

[11] Hurewicz, W. Lectures on Ordinary Differential Equations. New York and Cambridge, Mass.: John Wiley & Sons, Inc., and MIT Press, 1958.

[12] Jacobson, N. Lie Algebras. New York: John Wiley & Sons, Inc., 1962.

[13] Kelley, J. L. General Topology. Princeton, N.J.: Van Nostrand Company, Inc., 1955.

[14] Kervaire, M. A Manifold which does not admit any differentiable structure. Comment. Math. Helv., 35(1961), 1–14.

[15] Kobayashi, S., and K. Nomizu. Foundations of Differential Geometry, vol. 1. New York: John Wiley & Sons, Inc., 1963.

[16] Kohn, J. J. Introduccion a la teoria de integrales harmonicas. Lecture notes issued by the Centro de Investigacion del IPN, Mexico, 1963.

[17] Lang, S. Introduction to Differentiable Manifolds. New York: John Wiley & Sons, Inc., 1962.

[18] Loomis, L. H., and S. Sternberg. Advanced Calculus. Reading, Mass.: Addison-Wesley, 1968.

[19] Milnor, J. On manifolds homeomorphic to the 7-sphere. Ann. of Math., 64(1956), 399–405.

[20] Montgomery, D., and L. Zippin. Topological Transformation Groups. New York: Interscience, 1955.

[21] Newns, N., and A. Walker. Tangent planes to a differentiable manifold. J. London Math. Soc., 31(1956), 400–407.

[22] Nirenberg, L. On elliptic partial differential equations. Ann. Scuola Norm. Sup. Pisa, 13(1959), 115–162.

[23] Pontrjagin, L. S. Topological Groups. Princeton, N.J.: Princeton University Press, 1939.

[24] de Rham, G. Variétés Differentiables. Paris: Hermann, 1960.

[25] Samelson, H. Uber die Sphären die als Gruppenräume auftreten. Comment Math. Helv., 13(1940), 144–155.

[26] Singer, I. M., and J. Thorpe. Lecture Notes on Elementary Topology and Geometry. Glenview, Ill.: Scott, Foresman and Company, 1967.

[27] Simmons, G. F. Introduction to Topology and Modern Analysis. New York: McGraw-Hill, 1963.

[28] Spanier, E. H. Algebraic Topology. New York: McGraw-Hill 1966.

[29] Spivak, M. Calculus on Manifolds. New York: W. A. Benjamin, Inc., 1965.

[30] Sternberg, S. Lectures on Differential Geometry. Englewood Cliffs, N.J.: Prentice-Hall, Inc., 1964.

[31] Woll, J. W., Jr. Functions of Several Variables. New York: Harcourt, Brace & World, Inc., 1966.

## Index of Notation

$\varnothing$ 3 $T(M), T^{*}(M)$ 19    
$\mapsto$ 3 $^{k}M_{m}, d^{k}f, M_{m}^{k}$ 20    
$g\circ f$ 3 $(x-x(m))^{*}$ 20    
id 3 $d^{k}\varphi, \delta^{k}\varphi$ 22    
$\mathbb{R}^{d}, r_{i}:\mathbb{R}^{d}\to\mathbb{R}$ 4 $(M,\psi)$ 22    
$\mathbb{C}^{n}$ 4 $i:A\to M$ 26    
supp $\varphi$ 4 $O(d)$ 33    
$\bar{A}$ 4 $X_{m}, X_{m}(f), X(f)$ 35    
$[\alpha]$ 5, 227 $[X,Y]$ 36    
$\alpha!$ 5 $(a(m),b(m))$ 37    
$\frac{\partial^{a}}{\partial r^{a}}$ 5 $X_{t}, D_{t}$ 37    
$C^{k}, C^{\infty}$ 5 $\langle\ , \rangle_{m}$ 52    
$(U,\varphi), (U,x_{1},\ldots,x_{d})$ 5 $V\otimes W, v\otimes w$ 54    
$(M,\mathcal{F})$ 6 Hom$(V,W)$ 55    
$M^{d}$ 6 $V_{r,s}, T(V)$ 55    
$S^{d}$ 7 $C(V), I(V), I_{k}(V)$ 56    
$G l(n,\mathbb{R})$ 7 $\Lambda(V), \Lambda_{k}(V)$ 56    
$C^{\infty}(U), C^{\infty}(M,N)$ 8 $v\land w$ 56    
$\tilde{F}_{m}, F_{m}, F_{m}^{k}$ 12 sgn $\pi$ 56    
$\mathbf{f}, \mathbf{f}(m)$ 12 $A_{r}(V)$ 56    
$M_{m}$ 12 $M_{r,s}(V)$ 58    
$\{\mathbf{f}-\mathbf{f}(\mathbf{m})\}$ 13 $\varepsilon(u), i(u)$ 61    
$\frac{\partial}{\partial x_{i}}\bigg|_{m}(f), \frac{\partial f}{\partial x_{i}}\bigg|_{m}$ 15 $T_{r,s}(M)$ 62    
$d\varphi, d\varphi_{m}, \delta\varphi$ 16 $\Lambda_{k}^{*}(M), \Lambda^{*}(M)$ 62    
$M_{m}^{*}$ 16 $\omega(X_{1},\ldots,X_{k})$ 64    
$\dot{\sigma}(t)$ 17 $\mathfrak{X}(M)$ 64

$d\omega$ 65 $\int_{D}\omega$ 147    
$i(X)\omega$ 68 $grad f$, $div V$ 150    
$\delta\psi(\omega)$ 68 $H_{d\circ\mathrm{R}}^{p}(M)$ 153    
$L_{X}Y$ 69 $\infty S_{p}(M,\mathbb{R}),\infty H_{p}(M;\mathbb{R})$ 154    
$L_{X}\omega$ 70 $\Delta g$ 158, 220    
$\mathcal{J}(\mathcal{D})$ 73 $K,Z$ 163    
$\langle w_{1}\wedge\cdots\wedge w_{p},v_{1}\wedge\cdots\wedge v_{p}\rangle$ 79 $\delta,s_{m}$ 163    
$\bullet:\Lambda(V)\rightarrow\Lambda(V)$ 79, 149, 220 $\delta\circ\delta$ 163    
$T^{n}$ 83 $\Gamma(8,U),\Gamma(8)$ 163    
$g$ 84, 86 $\mathcal{C}^{\infty}(M),\mathcal{C}^{p}(M)$ 164    
$gl(n,\mathbb{R})$ 84 $P=\{S_{U};\rho_{U,V}\}$ 165    
$l_{e},r_{e}$ 84 $\alpha(8)$ 166    
$V\sigma,\sigma V$ $(\sigma\in G,V\subset G)$ 84 $\beta(P)$ 167    
$G_{e}$ 86 $8\otimes\mathcal{T}$ 169    
$x_{ij}(\sigma)$ $(\sigma\text{a matrix})$ 86 $C^{*}$ 173    
$End(V),Aut(V)$ 87 $d^{q}\colon C^{q}\to C^{q+1}$ 173    
$gl(n,\mathbb{C}),Gl(n,\mathbb{C})$ 88 $Z^{q}(C^{*}),B^{q}(C^{*}),H^{q}(C^{*})$ 173    
$E_{inv}^{p},E_{inv}^{*}^{\ast}$ 88 $C^{\ast}\to D^{\ast}$ 173    
$\pi_{1}(X,x_{0})$ 98 $\partial$ 174    
$exp_{x},\exp$ 102 $\mathcal{H},H^{q}(M,\mathcal{S})$ 176    
$e^{A}$ 105 $\Gamma(\mathcal{C}^{\ast}\otimes\mathcal{S})$ 178    
$A^{t},A,A^{-1}$ 107 $s_{0}$ 181    
$U(n),u(n)$ 107 $U^{p+1},A^{p}(U,K)$ 186    
$Sl(n,\mathbb{C}),sl(n,\mathbb{C})$ 107 $d:A^{p}(U,K)\to A^{p+1}(U,K)$ 186    
$O(N,\mathbb{C}),\mathfrak{o}(n,\mathbb{C})$ 107 $A^{*}(U,K),\mathcal{A}^{p}(M,K)$ 186    
$SU(n)\quad su(n)$ 108 $\mathcal{A}^{*}(M,K),A^{p}(U,G),A_{0}^{p}(U,G)$ 187    
$Sl(n,\mathbb{R}),sl(n,\mathbb{R})$ 108 $H_{A-S}^{q}(M;G)$ 188    
$O(n),v(n),SO(n)$ 108 $\mathcal{E}^{p}(M)$ 189    
$Ad$ 113 $\mathcal{E}^{*}(M)$ 190    
$ad$ 114 $E^{*}(M)$ 191    
$G|H$ 120 $S_{p}(U),S^{p}(U,K),S_{0}^{p}(U,K)$ 192    
$P^{n},CP^{n}$ 128 $d:S^{p}(U,K)\to S^{p+1}(U,K)$ 193    
$S_{p}(V),M_{k}(V)$ 129 $S^{*}(U,K),S^{p}(M,K),S_{0}^{p}(M,K)$ 193    
$J_{q}$ 141 $S^{p}(U,G)$ 196    
$\Delta^{p}$ 141 $H_{\Delta}^{q}(M;G),H_{\Delta}^{\infty}(M;G)$ 196    
$k_{i}^{p},\sigma^{i},\partial\sigma$ 142 $S_{U}^{q}(M,G)$ 197    
$f_{a}\omega$ 143 $C^{q}(U,S)$ 200



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>d:  $ C^{q}(\mathbb{U},\mathbb{S}) \to C^{\#+1}(\mathbb{U},\mathbb{S}) $</td><td style='text-align: center; word-wrap: break-word;'>200</td><td style='text-align: center; word-wrap: break-word;'>$ \varphi \cdot \psi $</td><td style='text-align: center; word-wrap: break-word;'>228</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \tilde{H}^{q}(\mathbb{U},\mathbb{S}) $</td><td style='text-align: center; word-wrap: break-word;'>201</td><td style='text-align: center; word-wrap: break-word;'>$ |\psi| $,  $ \|\psi\| $</td><td style='text-align: center; word-wrap: break-word;'>228</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \tilde{H}^{q}(M,\mathbb{S}) $,  $ \tilde{H}^{q}(M;G) $</td><td style='text-align: center; word-wrap: break-word;'>202</td><td style='text-align: center; word-wrap: break-word;'>$ \langle\psi,\varphi\rangle $</td><td style='text-align: center; word-wrap: break-word;'>228, 243</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ C^{*} \otimes \mathcal{C}^{*}&#x27; $</td><td style='text-align: center; word-wrap: break-word;'>207</td><td style='text-align: center; word-wrap: break-word;'>$ \|\psi\|_\infty $</td><td style='text-align: center; word-wrap: break-word;'>228</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathcal{S} \oplus \mathcal{T} $</td><td style='text-align: center; word-wrap: break-word;'>208</td><td style='text-align: center; word-wrap: break-word;'>$ \varphi_{\xi} $ ( $ \xi=(\xi_1,\dots,\xi_n) $)</td><td style='text-align: center; word-wrap: break-word;'>229</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ f \smile g $</td><td style='text-align: center; word-wrap: break-word;'>212</td><td style='text-align: center; word-wrap: break-word;'>$ H_s $,  $ \langle\ ,\ ,\ ,\ | $</td><td style='text-align: center; word-wrap: break-word;'>231</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ H^p $</td><td style='text-align: center; word-wrap: break-word;'>223</td><td style='text-align: center; word-wrap: break-word;'>$ K^t $</td><td style='text-align: center; word-wrap: break-word;'>231</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ (H^p)^\perp $</td><td style='text-align: center; word-wrap: break-word;'>224</td><td style='text-align: center; word-wrap: break-word;'>$ T_h $</td><td style='text-align: center; word-wrap: break-word;'>235</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ H_p(M;\mathbb{R}) $</td><td style='text-align: center; word-wrap: break-word;'>227</td><td style='text-align: center; word-wrap: break-word;'>$ u^b $</td><td style='text-align: center; word-wrap: break-word;'>236</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \eta^a = \eta_1^{a_1} \cdots \eta_n^{a_n} $</td><td style='text-align: center; word-wrap: break-word;'>227</td><td style='text-align: center; word-wrap: break-word;'>$ L = \{L_{ij}\} $,  $ L^* $</td><td style='text-align: center; word-wrap: break-word;'>238</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ D^a $</td><td style='text-align: center; word-wrap: break-word;'>228</td><td style='text-align: center; word-wrap: break-word;'>$ C^\infty $,  $ C_0^\infty $</td><td style='text-align: center; word-wrap: break-word;'>243</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathcal{P} $</td><td style='text-align: center; word-wrap: break-word;'>228</td><td style='text-align: center; word-wrap: break-word;'>$ C_0^\infty(V) $</td><td style='text-align: center; word-wrap: break-word;'>244</td></tr></table>

### Index

Action of Lie groups, 112, 123

Adjoint representation, 112 ff.

Ado's theorem, 101

Affine motions, group of, 83

Alexander-Spanier cohomology, 186 ff. with supports, 215

Alternating multilinear maps, 56 ff.

Anti-derivation, 61

Axiomatic sheaf cohomology, 176 multiplicative structure, 207 ff. with supports, 214 ff.

Ball in Euclidean space, 4

Bilinear forms, automorphisms and

derivations of, 118–119

Bilinear operations, automorphisms and derivations of, 117–118

Boundary

differentiable singular, 154

of a p-simplex, 142

Cartan lemma, 80 (Ex. 16)

Cartesian product of

manifolds, 7, 52 (Ex. 24)

mappings, 3

sets, 3

Cauchy-Riemann operator, 254 (Ex. 15)

Cech cohomology, 200 ff. with supports, 215

Centered coordinate system, 5

Chain, 142

Chain complex, 199

Chain rule, 17

Class C $ ^{x} $, 5-6

Class $C^{\infty}$

differentiable manifold, 6

function on Euclidean space, 5

mapping, 8

Classical cohomology theories. See

Cohomology theories.

Cochain complex, 173 ft.

Cochain complex (cont)

coboundaries, 173

cobondary operator, 173

cocytes, 173

cohomology of, 173

tensor product of, 207

Cochain map, 173

Coframe field, 149

Cohomology with coefficients in sheaves, 176 ff.

Cohomology theories

Alexander-Spanier, 186 ff., 215

Čech, 200 ff., 215

differentiable singular, 191 ff., 205–207, 212–215, 227

de Rham, 153 ff., 189 ff., 205–207, 211–215, 217 (Ex. 21), 225–227

singular, 191 ff., 205, 212–215, 217 (Ex. 19)

Commutative diagram, 3

Completely integrable distribution, 42

Complex analytic structure, 6

Complex general linear group, 88 connectedness, 136 (Ex. 25)

exponential map, 105 ff., 134 (Exs. 14, 15), 135 (Ex. 22)

polar decomposition, 136 (Ex. 24)

subgroups, 107–108

Complex manifold, 6

Complex n-space, 4, 7

Complex number field, 4, 83

Complex orthogonal group, 107–108

Complex projective space, 128

Composition of mappings, 3

Constant sheaf, 164

Coordinate functions on Euclidean space,4

Coordinate functions, 5

Coordinate map, 5

Coordinate system, 5

centered, 5

cubic, 5

slice of, 27

Cotangent bundle, 19

Countability, second axiom of, 6, 8 ft.

Covering spaces, 98 ff., 132 (Ex. 7) base, 98 covering, 98 evenly covered set, 98 from Lie group homomorphism, 100

Cube in Euclidean space, 4

Cubic coordinate system, 5

Curve, 17

integral, 36 ff.

piecewise smooth, 34

smooth on [a,b], 34

tangent vector to, 17

Cycle, differentiable singular, 154

de Rham. See under R-listing.

Derivation

on functions, 12

on forms, 61

Derivative, 4 exterior, 65 ft. Lie, 69 ft. partial, 4

Determinants, 79 (Ex. 12)

Diffeomorphism,22-23

Difference quotients, 235 ff.

Differentiable (see also Class C∞), 6

Differentiable manifold (see also Manifold), 5 ff.

Differentiable singular cohomology,

191 ff., 205–207, 227

multiplicative structure, 212–214

with supports, 215

Differentiable structure, 5–6

of class $C^{*}$, 5

of class $C^{\infty}$, 5

of class $C^{\infty}$, 6

complex analytic, 6

Differential

of a function, 16–17

of coordinate functions, 17

higher order, 20–22

of a map, 16

Differential forms, 62 ff.

closed, 153

differential ideals, 74

exact, 153

exterior derivative, 65

independent 1-forms, 73

interior multiplication by 68

left invariant, 88 ff.

Lie derivative, 70 ff.

effect of mappings, 68

Differential forms (cont)

Maurer-Cartan forms, 88

periods, 155

de Rham cohomology, 153 ff., 189 ff., 205 ff., 211, 215, 226

Differential ideal, 74 integral manifold, 74–75 maximal integral manifold, 74–75

Direct limit of K-modules, 167

Distributions, 41 ff.

annihilating forms, 73

annihilating ideal, 73

Frobenius theorem, 42, 48, 75

integral manifold, 42

involutive (completely integrable), 42, 74

maximal integral manifold, 48, 75

Divergence of a vector field, 150

Divergence theorem, 151, 157 (Ex. 4)

Effective action of a Lie group, 123

Elliptic equations, simple examples, 252 (Ex. 9)

Elliptic operators, 240 π.

fundamental inequality, 240

on vector bundles, 257 (Ex. 21)

invariant solutions, 258 (Ex. 23)

Equivalence of submanifolds, 26

Euclidean space, 4

integration on, 140–141

as a Lie group, 83

as a manifold, 6

de Rham cohomology of, 156, 158

(Ex. 10)

standard orientation, 140

Exact sequences, 165

Exponential map, 102 ff., 116 for general linear group, 105 ff., 134 (Exs. 10, 14, 15), 135 (Ex. 22) relation between subgroup and subalgebra. 104

Extension of vector field, 39–40

Exterior algebra, 56 ff.

anti-derivations, 61

derivations, 61

dualities, 58 ff.

endomorphisms of degree k, 61

inner products on, 79 (Ex. 13)

interior product, 61

star operator, 79 (Ex. 13)

universal mapping property, 57–5

Exterior k-bundle, 62

Exterior algebra bundle, 62

Exterior derivative, 65 ft.

Exterior (wedge) product, 56, 60

Family of supports, 214

Fine resolution,178

Formal adjoint, 239

Forms. See Differential forms.

Fourier series, 229 ft.

Frame field, 149

Frobenius theorem, 42, 48, 75 classical, 45–46

Function, 3

coordinate, 4, 5

component, 4

independent, 23

Fundamental group, yo

Fundamental inequality, 240

General linear group, 7, 83, 86–88

components, 131

exponential map, 105 ff., 134 (Ex. 10)

polar decomposition, 131, 136 (Ex. 23)

subgroups, 107–108

See also Complex general linear group.

Germ of a function, 12

Gradient, 150

Grassmann manifold, 130

Graph of a map, 75 as integral manifold, 75 ff.

Green's identities, 158 (Ex. 5)

Green's operator, 225

Harmonic function, 222

Harmonic form,223

Hilbert's Fifth Conjecture, 110

Hodge decomposition theorem, 223

Homogeneous manifolds, 120 ff., 125 ff.

Homology

real continuous singular, 227

real differentiable singular, 154, 206

Homomorphism

Lie algebra, 90

Lie group, 89

of sheaf cohomology theories, 180 ff.

Homotopy operator, 157, 190, 194, 199, 202

Imbedding,22

Identity map, 3

Immersion, 22

Implicit function theorems, 30 ff. classical, 30

Independent set of functions, 23

Injective mapping, 3

Integral curve, 36 ft.

Integral manifold, 42, 74

maximal, 48, 74

Integration, 140 ff.

over chains, 141 ff.

in Euclidean space, 140

of n-forms in Euclidean space, 141

on Lie groups, 151 ff.

on oriented manifolds, 145 ff.

on Riemannian manifolds, 149 ff.

Interior multiplication, 61 by vector fields, 68

Invariant differential operators, 258 (Ex. 23)

Invariant solutions, 258 (Ex. 23)

Inverse function theorem, 23

Involutive distributions, 42, 74

Isotropy group, 123

Jacobi identity, 36, 84

Jacobian, 17

K-modules, 163

direct limit, 167

tensor product, 169

torsionless, 172, 207

Kronecker index, 4

L<sub>4</sub> norm, 228, 243

Laplace-Beltrami operator, 220 ff.

eigenvalues, 254 (Ex. 16)

ellipticity, 250–251

in Euclidean space, 158 (Ex. 5), 252 (Ex. 6)

symbol. 251

Laplacian, 158 (Ex. 5), 220 ft.

Left invariant forms, 88-89, 90-92

Left invariant vector fields, 84 ff. completeness, 103

Left multiplication, 61

Left translation, 84

Lie algebra, 36, 84

abelian, 84

center, 116

homomorphism, 90

isomorphism, 90

of a Lie group, 86

of $n \times n$ matrices, 84, 86–88, 107–108

representation, 90

subalgebra, 93

Lie bracket, 36, 78 (Ex. 6), 84 as Lie derivative, 70

Lie derivative

of differential forms, 70

of vector fields, 69

Lie group, 82 ff.

abelian, 116, 135 (Ex. 18)

action on manifolds, 112–113, 123

adjoint representation, 112 ff.

associated with each Lie algebra, 101, 117

automorphism, 89

automorphism group, 119, 135 (Ex. 20)

bi-invariant metric, 158 (Ex. 9)

center, 116

closed subgroup, 93, 110 ff., 135 (Ex. 17)

Lie groups (cont)

closed subgroup topology, 97

connectivity, 130

continuous homomorphism, 109

examples, 83, 86–88, 107–108

exponential map, 102 ff.

faithful representation, 101

fundamental group, 134 (Ex. 12)

as a homogeneous manifold, 124

homomorphism, 89 ff.

homomorphism as a covering map, 100

homomorphism with simply connected domain, 101

identity component, 83

identity element, 82

integration on, 151 ff.

left invariant forms, 88 ff.

left invariant vector fields, 84 ff.

left translation, 84

Lie algebra of, 86

Lie subgroup of, 92 ff.

normal subgroup, 115

1-parameter subgroup, 102

orientation, 140

products of, 83

relation between subgroups and subalgebras of the Lie algebra, 94 ff., 104

representations, 89, 152–153

right invariant vector fields, 135 (Ex. 16)

right translation, 84

second countability, 83

simply connected, 101

simply connected covering group, 99–101

structural constants, 89

subgroup (see Lie subgroup)

Lie subgroup, 92 ff.

closed, 93, 110 ff., 135 (Ex. 17)

closed subgroup topology, 97

equivalence of, 93, 95–97

normal, 115

1-parameter, 102

relation between Lie subgroups and subalgebras of the Lie algebra, 94 ff., 104

uniqueness of, 93, 95–97

Lifting, 34

Linear differential operator, 238

Linear isotropy group, 123

Local 1-parameter group of a vector field, 39

Locally Euclidean space, 5

with no differentiable structure, 23

with non-diffeomorphic structures, 23

Manifolds, 5 ff.

homogeneous, 120 ff.

Manifolds (cont)

integral of a distribution or differential ideal, 42, 74

integration on, 140 ff.

maximal integral, 48, 74

metrizability, 8

normality, 8

open submanifold, 7

orientable, 138

paracompactness, 8–9

product manifold, 7, 52 (Ex. 24)

Riemannian, 52 (Ex. 23), 149–151, 220 ff.

second axiom of countability, 6, 8 ff.

slices, 27

submanifold, 22, 26–27

Manifold structure, 6

Mappings

cartesian product of, 3

commutative diagram, 3

composition, 3

diffeomorphism, 22

factoring through submanifolds, 25–26, 47

function, 3

identity, 3

imbedding, 22

immersion, 22

non-singular, 16

one-to-one (injective), 3

onto (surjective), 3

restriction, 3

submanifold, 22

Matrices, 7, 83, 84, 86–88, 107–108, 125–132, 136 (Ex. 25)

exponential map, 105 ff., 134 (Exs. 10, 14, 15), 135 (Ex. 22)

polar decomposition, 131, 136 (Exs. 23, 24)

positive definite, 131

Maurer-Cartan forms, 88

Maximal integral manifold, 48, 74

Modular function, 152

Multi-index notation, 5, 227

Neighborhood, 4

Non-singular mapping, 16

Non-singular pairing, 58

Norms

L_{1}, 228, 243

Sobolev, 231

1-parameter group of a vector field, 39

1-parameter subgroup, 102

Orientation, 138 ff.

vector space, 79 (Ex. 13)

Orthogonal group, 33, 108, 119, 125–131 components, 130

Pairing, 58

Paracompactness, 8 for manifolds, 9

Partial derivatives, 4

Partition of unity

existence, 10

on manifolds, 8

subordinate to a cover, 8

for sheaves, 170

Periodic differential operator, 238 support of, 244

Periodic distribution, 253 (Ex. 11)

Periodic functions, n

norms on. 228

Periods of forms, 155, 217 (Ex. 21)

Peter-Paul inequality. 232

Peter-Weyl theorem, 257 (Ex. 20)

Poincaré duality, 226–227

Poincaré lemma, 155

Presheaf, 165 ff.

associated sheaf, 166 ff.

complete, 168

homomorphism, 166

isomorphism, 166

tensor product, 169

Quotient sheaf, 165

Product manifolds, 7, 52 (Ex. 24)

Real continuous singular homology, 227

Real differentiable singular homology, 154, 206

Real projective space, 128 orientation, 140, 157 (Ex. 2)

Real special linear group, 108

Regular domain, 145 ft.

Regularity theorem, 223, 242, 245 ff., 253 (Ex. 14)

Rellich lemma, 237

Representations of Lie groups, 89 orthogonal and unitary, 152–153

Resolution, 178

de Rham cohomology, 153 ff., 189 ff., 205–207, 217 (Ex. 21), 225–227 of Euclidean space, 156, 158 (Ex. 10) other examples, 158 (Exs. 10, 11), 159 (Exs. 16, 17), 160 (Exs. 18, 19) multiplicative structure, 211 supports, 215 of the unit circle, 153

de Rham theorem, 154–155, 205 ff., 214, 215

Riemannian manifold, 52 (Ex. 23), 220 ff. integration on, 149 ff.

volume, 149

volume form, 149, 158 (Ex. 6), 160 (Ex. 20)

Riemannian structure, 52 (Ex. 23)

Right invariant vector field, 135 (Ex. 16)

Right translation, 84

Schwartz inequality, 232

Second axiom of countability, 6, 8 ff.

Semi-locally 1-connected, 98

Set notation, 2-4

sign of a permutation, 56

Sheaf, 162 ff.

associated presheaf, 166 ff.

constant, 164

direct sum, 208

fine, 170

of germs of C<sup>ω</sup> functions, 164

of germs of discontinuous sections, 181

homomorphism, 164

isomorphism, 164

of K-modules, 163

mapping, 164

partition of unity, 170

projection, 163

quotient, 165

resolution, 178

section, 163

subsheaf, 164

stalk, 163

tensor product, 169

torsionless, 172

Sheaf cohomology theory, 176 ff.

existence, 178 ff.

homomorphism of, 180 ff.

multiplicative structure, 207 ff.

with supports, 215

uniqueness, 181 ff.

"p, q shuffle," 60

Simplex, 141, 191

boundary of, 142

continuous singular, 191

differentiable singular, 141

face of, 142

oriented, 146

regular, 146

standard, 141

Simply connected space, 98

Lie group, 99, 101

Singular cohomology, 191 ff., 205, 217 (Ex. 19)

multiplicative structure, 212

with supports, 215

Skew-Hermitian matrices, 107–108

Skew line on torus, 51 (Ex. 21)

Skew-symmetric matrices, 107–108

Skyscraper sheaf, 171

Slices, 27

Smooth (class C∞). 6

Sobolev lemma, 237, 258 (Ex. 22)

Sobolev spaces, 231 ft.

Special linear group, 107-108

Special orthogonal group, 108, 130

Special unitary group, 108, 130

Sphere, 7, 33

as homogeneous manifold, 125 ff.

orientation, 140

de Rham cohomology of, 153, 159

(Exs. 16, 17)

Star operator, 79 (Ex. 13), 220 ff.

Stiefel manifold, 129

Stokes' theorem, 144, 148, 151

Submanifolds, 22

equivalence of, 26

factoring maps through, 25–26, 47

C<sup>∞</sup> functions on, 29

as slices, 27–29

as subset, 26–27

topology and differentiable structure, 27

uniqueness, 27

Support

of a function, 4

of a sheaf homomorphism, 170

Surjective mapping, 3

Symbol of a differential operator, 251

Tangent bundle, 19–20

Tangent space, 12

Tangent vector, 11 ff.

from coordinate system, 14–15

to curves, 17

higher order, 20–22

Tensors, 55 ff.

decomposable, 56

homogeneous, 56

type $(r,s)$, 55

Tensor algebra, 55 ff.

dualities, 58 ff.

Tensor bundle of type $(r,s)$, 62

Tensor fields, 63 ff.

Lie derivative, 70

Tensor product

of cochain complexes, 207

of K-modules, 169

of presheaves, 169

Tensor product (cont)

of resolutions, 208

of sheaves, 169

universal mapping property, 55

of vector spaces, 54-55

Topological group, 110

Torsionless resolution, 178

Torus, 51 (Ex. 21), 83, 135 (Ex. 18)

Trace 0 matrices, 107-108

Transitive action, 123

Unitary group, 107-108, 130, 135 (Ex. 21)

Universal mapping property of exterior algebra, 57-58

of tensor algebra, 55

Vector fields, 34 ff.

complete, 39

along a curve, 34

local $C^{\infty}$ extension, 39–40

acting on functions, 35

integral curves, 36 ff.

as liftings into $T(M)$, 34

left invariant, 84 ff.

Lie bracket, 36

Lie derivative, 69 ff.

local 1-parameter group, 39

along a mapping, 39

1-parameter group, 39

$\varphi$-related, 41

Vector space

as a manifold, 7, 86

orientation, 79 (Ex. 13)

Volume, 149

Volume form, 149, 158 (Ex. 6), 120

Wave equation, 256 (Ex. 18)

Weak solution, 222

Wedge (exterior) product, 56, 60

