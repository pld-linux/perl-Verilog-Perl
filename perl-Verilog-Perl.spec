#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Verilog
%define	pnam	Perl
Summary:	perl(Verilog::Perl) - an perl way to handle Verilog files
#Summary(pl):	
Name:		perl-Verilog-Perl
Version:	2.372
Release:	0.1
License:	LGPL or Perl Artistic License
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b879520aa1f4b05c01f5cfa2bcdfaa12
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Verilog::Parser, Verilog::Preproc, and other perl modules usefull for
manipulation of verilog files. The Verilog::Parser package will tokenize a
Verilog file when the parse() method is called and invoke various callback
methods. This is useful for extracting information and editing files while
retaining all context. For netlist like extractions, see Verilog::Netlist.
Verilog::Preproc reads Verilog files, and preprocesses them according to the
Verilog 2001 specification. Programs can be easily converted from reading a
IO::File into reading preprocessed output from Verilog::Preproc.
Verilog::Netlist contains interconnect information about a whole design
database.


%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

# maybe bin/man1 should be moved to another package
%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/Verilog
%{perl_vendorarch}/Verilog/*.pm
%dir %{perl_vendorarch}/Verilog/Netlist
%{perl_vendorarch}/Verilog/Netlist/*.pm
%dir %{perl_vendorarch}/auto/Verilog/Preproc
%{perl_vendorarch}/auto/Verilog/Preproc/Preproc*
%{_mandir}/man3/*
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
