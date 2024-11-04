Name:		texlive-prooftrees
Version:	72665
Release:	1
Summary:	Forest-based proof trees (symbolic logic)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/prooftrees
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prooftrees.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prooftrees.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports drawing proof trees of the kind often used
in introductory logic classes, especially those aimed at
students without strong mathemtical backgrounds. Hodges (1991)
is one example of a text which uses this system. When teaching
such a system it is especially useful to annotate the tree with
line numbers, justifications and explanations of branch
closures. prooftrees provides a single environment, prooftree,
and a variety of tools for annotating, customising and
highlighting such trees. A cross-referencing system is provided
for trees which cite line numbers in justifications for proof
lines or branch closures. prooftrees is based on forest and,
hence, TikZ. The package requires version 2.0.2 of Forest for
expected results and will not work with version 1.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/prooftrees
%doc %{_texmfdistdir}/doc/latex/prooftrees

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
