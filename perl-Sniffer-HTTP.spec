%define upstream_name	  Sniffer-HTTP
%define upstream_version 0.23

Name:		perl-%{upstream_name}
Summary:	Multi-connection sniffer driver
Version:	%perl_convert_version %{upstream_version}
Release:	1
URL:		http://search.cpan.org/~corion/Sniffer-HTTP-0.22/lib/Sniffer/HTTP.pm
Source0:	http://www.cpan.org/authors/id/C/CO/CORION/Sniffer-HTTP-%{upstream_version}.tar.gz
License:	Artistic
Group:		Development/Perl 

BuildRequires:	perl-devel
BuildRequires:	perl(NetPacket)
BuildRequires:	perl(Net::Pcap)
BuildRequires:	perl(Exporter::Lite)
BuildRequires:	perl(LWP::Simple)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Class::Accessor)
BuildArch:	noarch

%description
This driver gives you callbacks with the completely accumulated
HTTP::Requests or HTTP::Responses as sniffed from the TCP traffic.
You need to feed it the Ethernet, IP or TCP packets either from
a dump file or from Net::Pcap by unpacking them via NetPacket.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes MANIFEST META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun May 01 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.220.0-1mdv2011.0
+ Revision: 661354
- import perl-Sniffer-HTTP


