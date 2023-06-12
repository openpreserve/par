# RELEASE NOTES

PAR - Preservation Action Registries

PAR is made available under the Apache v2.0 license, see the file LICENSE for details.

## PAR 1.2.0

2023-06-08

- API definition now written in OpenAPI 3.1 not Swagger 2.x. [[#58][]] [[#61][]]
  Simple version change and updating of `example` to `examples` in the API definition.
- GitHub actions to replace Travis. [[#56][]]
- NotImplemented response. [[#59][]]
  This was achieved by adding a standard response component to the API definition, so:

```yaml
components:
responses:
NotImplemented:
    description: The method called is currently not implemented by this server.
    content: {}
Unauthorized:
    description: If no Authorization header has been supplied
    content: {}
Forbidden:
    description: If the supplied Authorization header does not reference a user
    with write access to this registry.
    content: {}
```

- Format signature encoding support. [[#62][]]
  Added an enumerated encoding property to the format signature entity:

```yaml
"encoding": {
    "default": "PRONOM",
    "enum": [
    "PRONOM",
    "ASCII",
    "HEX",
    "REGEX_PERL"
    ],
    "type": "string"
```

- API document publication. [[#63][]]
- Schema versioning and publication. [[#68][]]

[#58]: https://github.com/openpreserve/par/pull/58
[#56]: https://github.com/openpreserve/par/pull/56
[#59]: https://github.com/openpreserve/par/pull/59
[#61]: https://github.com/openpreserve/par/pull/61
[#62]: https://github.com/openpreserve/par/pull/62
[#63]: https://github.com/openpreserve/par/pull/63
[#68]: https://github.com/openpreserve/par/pull/68
