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

RAWCOMMENT: diagram 5.29(7)-(8) garbled in OCR; reconstruct against PDF

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
