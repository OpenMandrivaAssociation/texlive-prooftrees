%global tl_name prooftrees
%global tl_revision 78038

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9.3
Release:	%{tl_revision}.1
Summary:	Forest-based proof trees (symbolic logic)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/prooftrees
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prooftrees.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prooftrees.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prooftrees.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package supports drawing proof trees of the kind often used in
introductory logic classes, especially those aimed at students without
strong mathematical backgrounds. Hodges (1991) is one example of a text
which uses this system. When teaching such a system it is especially
useful to annotate the tree with line numbers, justifications and
explanations of branch closures. prooftrees provides a single
environment, prooftree, and a variety of tools for annotating,
customising and highlighting such trees. A cross-referencing system is
provided for trees which cite line numbers in justifications for proof
lines or branch closures. prooftrees is based on forest and, hence,
TikZ. The package requires version 2.1+ of forest for expected results.
It will not work with versions prior to 2.1.

