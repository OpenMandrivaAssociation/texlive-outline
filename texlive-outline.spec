%global tl_name outline
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	List environment for making outlines
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/outline
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/outline.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/outline.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines an outline environment, which provides facilities
similar to enumerate, but up to 6 levels deep.

